#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the copy of the Datatype Ontology against AGLDWG/datatype-ont.

Four things can go wrong with ``upstream/`` without any change in this
repository:

- the Australian Government Linked Data Working Group (AGLDWG) changes the
  ontology on its ``master`` branch, or starts to tag its editions, so the
  schema falls behind;
- the copied files drift from the files they were taken from;
- the licence GitHub detects for AGLDWG/datatype-ont changes, which decides
  what this repository may copy;
- the ontology's namespace, which is the schema header's ``source``, stops
  redirecting to that branch, so the ontology may now live elsewhere.

The commit, the edition it holds and each copied file's git object hash are
pinned below. The script asks the GitHub API for the commit ``master``
names, the repository's tags, the licence GitHub detects and the file tree
at the pinned commit and, when ``master`` has moved, at its head. It
compares every copied file with its blob by git object hash, so nothing is
downloaded but listings. It also asks the namespace where it redirects,
without following the redirect.

It prints a Markdown report, and exits 1 when:

- ``master`` names another commit, or the repository has a tag;
- a copied file changed or is gone at the head of ``master``;
- a copied file differs from its pin, or the copy holds an unpinned file;
- the licence is no longer CC-BY-4.0, or GitHub detects none;
- the namespace redirects somewhere else, or does not redirect;
- a check could not finish, such as a refused, failed or cut-off request,
  or an answer larger than the script reads.

A file the AGLDWG adds beside the copied ones, in the folders the copy is
taken from, is reported for information only.

Text a server chose, such as a tag name, a redirect target or an error
message, is quoted as code in the report, so the issue the workflow opens
from it cannot mention anyone. Set ``GITHUB_TOKEN`` to raise the API rate
limit. The token goes to api.github.com alone, never on to a redirect or to
the namespace's host. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import sys
import urllib.error
import urllib.request
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "upstream"
API = "https://api.github.com/repos/AGLDWG/datatype-ont"
USER_AGENT = "lmodel-datatype-watch"

# The most the script reads of one answer. The largest, the file tree, is
# about 2 kB.
MAX_BYTES = 5_000_000

# The branch the AGLDWG publishes from, and the commit the copy is taken
# from: the head of master since 4 June 2021. Move the commit, PINNED_BLOBS,
# PINNED_EDITION and the schema header together when the copy is replaced.
PINNED_BRANCH = "master"
PINNED_COMMIT = "dd8f24120cd59f686086f58175de37807c569e18"

# The ontology states no owl:versionInfo or owl:versionIRI, so its
# dcterms:modified date names the edition. It is the schema header's
# `version`; tests/test_upstream.py holds the two equal, and this equal to
# the copied Turtle file's dcterms:modified.
PINNED_EDITION = "2019-10-03"

# The ontology's namespace and landing page, which is the schema header's
# `source`, and where its https address sends a request for Turtle.
PINNED_SOURCE = "http://linked.data.gov.au/def/datatype"
NAMESPACE = "https://linked.data.gov.au/def/datatype"
PINNED_REDIRECT = "https://raw.githack.com/AGLDWG/datatype-ont/master/rdf/datatype.ttl"

# The licence GitHub detects for AGLDWG/datatype-ont, from the LICENSE that
# the copy holds. NOTICE says how it relates to the CC0 the ontology states.
PINNED_LICENSE = "CC-BY-4.0"

# Each copied file, by its path in AGLDWG/datatype-ont and in the copy, and
# its git object hash at PINNED_COMMIT. tests/test_upstream.py checks the
# hashes offline.
PINNED_BLOBS = {
    "LICENSE": "06c608dcf4552094bc86dc48aaa90addb2886049",
    "rdf/datatype.ttl": "2d60f4cabf93a057b66d845f1574968f0e799ca0",
}

# The other files of the folders the copy is taken from. The RDF/XML and
# JSON-LD files are the same ontology in other syntaxes, the diagrams file
# is TopBraid Composer's, and the README is the repository's. A file the
# AGLDWG adds beside these is reported for information.
LEFT_OUT = {
    "README.md": "f087b8d25eb4525139397629364b78e660c47861",
    "rdf/datatype.diagrams": "aa776a75db81ba1e511fbc80e1725f32e6754d13",
    "rdf/datatype.jsonld": "c84aa5034a16d90b1edf776de49b5143dacb8999",
    "rdf/datatype.rdf": "83a9930613e89e42d0d7fa02ea03fe5ffa55a116",
}


def _watched(path: str) -> bool:
    """Whether a path sits in a folder the copy is taken from: the root and
    rdf/."""
    return "/" not in path or path.startswith("rdf/")


def _read(resp) -> bytes:
    body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"an answer is larger than {MAX_BYTES} bytes")
    return body


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API + "/"):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return _read(resp)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Hand a redirect back to the caller instead of following it."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _location(url: str) -> str | None:
    """Where a request for Turtle at url is redirected, or None when the
    server answers without a redirect. No token is sent."""
    req = urllib.request.Request(
        url, headers={"Accept": "text/turtle", "User-Agent": USER_AGENT}
    )
    opener = urllib.request.build_opener(_NoRedirect)
    try:
        with opener.open(req, timeout=60) as resp:
            _read(resp)
            return None
    except urllib.error.HTTPError as err:
        if err.code in (301, 302, 303, 307, 308):
            return err.headers.get("Location", "")
        raise


def _code(text: object) -> str:
    """Text a server chose, such as a tag name, as a code span, so it cannot
    mention a person or add a link in the issue."""
    return "`" + str(text).replace("`", "'") + "`"


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the trees API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def _tree(ref: str) -> dict[str, str]:
    """Every file of the repository at a commit, by path, with its object
    hash. Each tree is asked for once, and no caller changes what it
    returns."""
    body = json.loads(_get(f"{API}/git/trees/{ref}?recursive=1"))
    if body.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in body["tree"] if e["type"] == "blob"}


@cache
def _head() -> str:
    """The commit the branch names, asked once."""
    return json.loads(_get(f"{API}/git/ref/heads/{PINNED_BRANCH}"))["object"]["sha"]


def _added(tree: dict[str, str]) -> list[str]:
    """The files of the watched folders that are neither copied nor left out
    on purpose."""
    return sorted(
        path
        for path in tree
        if _watched(path) and path not in PINNED_BLOBS and path not in LEFT_OUT
    )


def check_edition() -> tuple[list[str], bool]:
    """Report whether master still names the pinned commit, and whether the
    repository has started to tag its editions."""
    report, attention = [], False
    head = _head()
    if head != PINNED_COMMIT:
        attention = True
        report.append(
            f"- **`{PINNED_BRANCH}` now names commit {_code(head[:12])}, not the pinned "
            f"`{PINNED_COMMIT[:12]}`.** Read what changed, replace the copy from that "
            "commit if the ontology moved on, and move the pins here and the schema header."
        )
    else:
        report.append(
            f"- `{PINNED_BRANCH}` still names the pinned commit `{PINNED_COMMIT[:12]}`, "
            f"which holds the ontology of {PINNED_EDITION}."
        )
    tags = [t["name"] for t in json.loads(_get(f"{API}/tags?per_page=100"))]
    if tags:
        attention = True
        report.append(
            "- **AGLDWG/datatype-ont now has the tags "
            + ", ".join(_code(t) for t in tags)
            + ".** Pin the edition to a tag from now on."
        )
    else:
        report.append("- No tag or release, as when pinned.")
    return report, attention


def check_licence() -> tuple[list[str], bool]:
    """Report whether GitHub still detects the pinned licence. GitHub
    answers 404, or names no licence, when it detects none."""
    try:
        found = (json.loads(_get(f"{API}/license")).get("license") or {}).get("spdx_id")
    except urllib.error.HTTPError as err:
        if err.code != 404:
            raise
        found = None
    if found != PINNED_LICENSE:
        shown = _code(found) if found else "no licence GitHub detects"
        return [
            f"- **AGLDWG/datatype-ont's licence now reads as {shown}, not "
            f"{PINNED_LICENSE}.** Check what it allows before the copy or the "
            "descriptions taken from it move on, and update NOTICE."
        ], True
    return [f"- Licence: {PINNED_LICENSE}, as pinned."], False


def check_copy() -> tuple[list[str], bool]:
    """Report whether the copy is the files pinned at the pinned commit, and
    whether the head of master changes or drops any of them."""
    report = [
        f"- Pinned commit: `{PINNED_COMMIT[:12]}` of `{PINNED_BRANCH}`, copied to `upstream/`."
    ]
    attention = False

    pinned_tree = _tree(PINNED_COMMIT)
    matching, differing = 0, []
    for name, pinned_sha in sorted(PINNED_BLOBS.items()):
        path = COPY / name
        if not path.is_file():
            differing.append(f"`{name}` is missing from the copy")
        elif pinned_tree.get(name) != pinned_sha:
            differing.append(f"`{name}` at commit `{PINNED_COMMIT[:12]}` is not the pinned blob")
        elif _blob_sha(path) != pinned_sha:
            differing.append(f"`{name}` differs from its file at `{PINNED_COMMIT[:12]}`")
        else:
            matching += 1
    extra = sorted(
        p.relative_to(COPY).as_posix()
        for p in COPY.rglob("*")
        if p.is_file() and p.relative_to(COPY).as_posix() not in PINNED_BLOBS
    )
    differing += [f"`{name}` is in the copy but not pinned" for name in extra]
    report.append(
        f"- {matching} of {len(PINNED_BLOBS)} copied files match the pinned commit byte for byte."
    )
    if differing:
        attention = True
        report.append(f"- **{len(differing)} problem(s) with the copy:**")
        report += [f"  - {d}" for d in differing]

    head = _head()
    added = _added(pinned_tree)
    if head != PINNED_COMMIT:
        head_tree = _tree(head)
        dropped = sorted(n for n in PINNED_BLOBS if n not in head_tree)
        changed = sorted(
            n for n, sha in PINNED_BLOBS.items() if n in head_tree and head_tree[n] != sha
        )
        for name in dropped:
            attention = True
            report.append(
                f"- **`{PINNED_BRANCH}` no longer holds `{name}`.** Find where the "
                "AGLDWG now publishes it, and move the pins."
            )
        for name in changed:
            attention = True
            report.append(
                f"- **`{PINNED_BRANCH}` changes `{name}`.** Replace `upstream/{name}` "
                "with the file at its head, move the pins here, and update the schema."
            )
        if not dropped and not changed:
            report.append(f"- The head of `{PINNED_BRANCH}` holds the copied files unchanged.")
        added = _added(head_tree)

    if added:
        report.append(
            f"- For information, `{PINNED_BRANCH}` also holds "
            + ", ".join(_code(n) for n in added)
            + ", which the copy neither holds nor leaves out on purpose."
        )
    return report, attention


def check_namespace() -> tuple[list[str], bool]:
    """Report whether the namespace still sends a request for Turtle to the
    copied file on master."""
    found = _location(NAMESPACE)
    if found != PINNED_REDIRECT:
        shown = f"redirects to {_code(found)}" if found is not None else "answers without a redirect"
        return [
            f"- **The namespace `{NAMESPACE}` now {shown}, not to `{PINNED_REDIRECT}`.** "
            "Find out whether the ontology has moved, and where its current edition is."
        ], True
    return [f"- The namespace still redirects a request for Turtle to `{PINNED_BRANCH}`."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("edition", check_edition),
    ("licence", check_licence),
    ("copy", check_copy),
    ("namespace", check_namespace),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--report", type=Path, help="Also write the Markdown report to this file")
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer,
        # ValueError an answer that is not JSON or is too large, and
        # LookupError, TypeError and AttributeError JSON of another shape.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            ValueError,
            LookupError,
            TypeError,
            AttributeError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
