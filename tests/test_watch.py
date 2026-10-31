"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py asks the GitHub API about
AGLDWG/datatype-ont, and the ontology's namespace where it redirects.
These tests replace its two network calls, `_get` and `_location`, with
tables of answers, so they run offline. They show what the report says when
master moves, a tag appears, the head of master drops or changes a copied
file, the changed Turtle file states a new edition or licence, the licence
GitHub detects changes or the namespace redirects elsewhere. They also show
it when the network fails or cuts an answer off, an answer is not what its
hash says, or the AGLDWG adds a file.
"""

import base64
import http.client
import importlib.util
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
TURTLE = (ROOT / "upstream" / "rdf" / "datatype.ttl").read_bytes()
HEAD = "4" * 40


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's cached answers."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tree(watch, extra=()):
    """A tree listing that holds the copied files, the files left out on
    purpose, a folder and any `extra` (path, sha) pairs."""
    entries = [
        {"path": path, "type": "blob", "sha": sha}
        for path, sha in {**watch.PINNED_BLOBS, **watch.LEFT_OUT}.items()
    ]
    entries.append({"path": "rdf", "type": "tree", "sha": "5" * 40})
    entries.append({"path": "html/datatype.html", "type": "blob", "sha": "6" * 40})
    entries += [{"path": p, "type": "blob", "sha": s} for p, s in extra]
    return {"tree": entries, "truncated": False}


def _answers(watch, head=None, tags=()):
    """What the API answers when nothing has changed since the pin, with
    `head` as the commit master names and `tags` as the repository's tags,
    keyed by the address the script asks."""
    api = watch.API
    head = head or watch.PINNED_COMMIT
    answers = {
        f"{api}/git/ref/heads/master": {"object": {"type": "commit", "sha": head}},
        f"{api}/tags?per_page=100": [{"name": n} for n in tags],
        f"{api}/license": {"license": {"spdx_id": "CC-BY-4.0"}},
    }
    for ref in {watch.PINNED_COMMIT, head}:
        answers[f"{api}/git/trees/{ref}?recursive=1"] = _tree(watch)
    return answers


def _with_turtle(watch, turtle: bytes):
    """What the API answers when master has moved to HEAD and changes the
    Turtle file to `turtle`, which it serves as a base64 blob."""
    answers = _answers(watch, head=HEAD)
    sha = watch._git_sha(turtle)
    tree = answers[f"{watch.API}/git/trees/{HEAD}?recursive=1"]
    tree["tree"] = [
        {**e, "sha": sha} if e["path"] == watch.ONTOLOGY_FILE else e
        for e in tree["tree"]
    ]
    answers[f"{watch.API}/git/blobs/{sha}"] = {
        "sha": sha,
        "encoding": "base64",
        "content": base64.b64encode(turtle).decode(),
    }
    return answers


def _stub(watch, answers, location=None):
    """Make `_get` answer from the table: an exception is raised, a missing
    address is a 404, and anything else is returned as JSON. `_location`
    answers with `location`, the pinned redirect by default, or raises it."""

    def get(url):
        if url not in answers:
            raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return json.dumps(answer).encode()

    def where(url):
        assert url == watch.NAMESPACE
        if isinstance(location, Exception):
            raise location
        return watch.PINNED_REDIRECT if location is None else location

    watch._get = get
    watch._location = where


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With master at the pin, no tag, the pinned licence, every blob as
    pinned and the namespace's redirect unchanged, the watch exits 0."""
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "`master` still names the pinned commit `dd8f24120cd5`" in text
    assert "No tag or release, as when pinned." in text
    assert "Licence: CC-BY-4.0, as pinned." in text
    count = len(watch.PINNED_BLOBS)
    assert f"{count} of {count} copied files match" in text
    assert "The namespace still redirects a request for Turtle to `master`." in text
    assert (
        "holds the pinned `rdf/datatype.ttl`, which states `dcterms:modified` 2019-10-03"
        in text
    )
    assert "For information" not in text


def test_a_moved_master_is_reported(watch, tmp_path):
    """A new commit on master sets attention even when it leaves the copied
    files unchanged, since the AGLDWG may have changed a file the copy
    leaves out."""
    _stub(watch, _answers(watch, head=HEAD))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`master` now names commit `444444444444`, not the pinned" in text
    assert "The head of `master` holds the copied files unchanged." in text


def test_a_tag_is_reported(watch, tmp_path):
    """A first tag means the AGLDWG now names its editions, so the pin
    should move to one."""
    _stub(watch, _answers(watch, tags=("v1.0",)))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**AGLDWG/datatype-ont now has the tags `v1.0`." in text


def test_a_head_that_drops_and_changes_files(watch, tmp_path):
    """A head of master without a copied file, or with a changed one, is
    reported as such, not as a crash."""
    answers = _answers(watch, head=HEAD)
    tree = answers[f"{watch.API}/git/trees/{HEAD}?recursive=1"]
    tree["tree"] = [
        {**e, "sha": "2" * 40} if e["path"] == "LICENSE" else e
        for e in tree["tree"]
        if e["path"] != "rdf/datatype.ttl"
    ]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`master` no longer holds `rdf/datatype.ttl`.**" in text
    assert "**`master` changes `LICENSE`.**" in text


def test_a_changed_licence_is_reported(watch, tmp_path):
    """A licence GitHub no longer reads as CC-BY-4.0 sets attention."""
    answers = _answers(watch)
    answers[f"{watch.API}/license"] = {"license": {"spdx_id": "CC0-1.0"}}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**AGLDWG/datatype-ont's licence now reads as `CC0-1.0`, not CC-BY-4.0.**"
        in text
    )


def test_no_licence_is_reported(watch, tmp_path):
    """GitHub's 404, or a null licence, when it detects none is a finding,
    not a check that could not finish."""
    for answer in (None, {"license": None}):
        fresh = _answers(watch)
        if answer is None:
            del fresh[f"{watch.API}/license"]
        else:
            fresh[f"{watch.API}/license"] = answer
        _stub(watch, fresh)
        code, text = _run(watch, tmp_path)
        assert code == 1
        assert "licence now reads as no licence GitHub detects" in text
        assert "licence check could not finish" not in text


def test_a_moved_namespace_is_reported(watch, tmp_path):
    """A namespace that redirects elsewhere, or not at all, sets attention,
    and the target the server chose is quoted as code."""
    _stub(watch, _answers(watch), location="https://example.org/@someone`x")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now redirects to `https://example.org/@someone'x`, not to" in text
    assert "@someone`" not in text
    _stub(watch, _answers(watch), location=None)
    watch._location = lambda url: None
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now answers without a redirect, not to" in text


def test_a_network_failure_still_writes_a_report(watch, tmp_path):
    """A check that cannot reach the API is reported as unfinished, sets
    attention, and leaves the other checks to run."""
    answers = _answers(watch)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"] = (
        urllib.error.URLError("Connection refused")
    )
    _stub(watch, answers, location=urllib.error.URLError("Name or service not known"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The copy check could not finish: `<urlopen error Connection refused>`.**"
        in text
    )
    assert "**The namespace check could not finish: `<urlopen error Name" in text
    assert "Licence: CC-BY-4.0, as pinned." in text
    assert "`master` still names the pinned commit" in text


def test_a_truncated_tree_is_reported_as_unfinished(watch, tmp_path):
    """A listing GitHub cut short cannot prove a file is gone, so the check
    stops instead of reporting it dropped."""
    answers = _answers(watch)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"]["truncated"] = (
        True
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The copy check could not finish: `the tree at" in text


def test_a_cut_off_or_odd_answer_could_not_finish(watch, tmp_path):
    """An answer cut off mid-read, or JSON of another shape, is a check that
    could not finish, and each check that reads it reports so."""
    answers = _answers(watch)
    answers[f"{watch.API}/license"] = http.client.IncompleteRead(b"{")
    answers[f"{watch.API}/git/ref/heads/master"] = ["not", "a", "ref"]
    _stub(watch, answers, location=EOFError("cut off"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The licence check could not finish: `IncompleteRead" in text
    assert "**The edition check could not finish: `" in text
    assert "**The copy check could not finish: `" in text
    assert "**The namespace check could not finish: `cut off`.**" in text


def test_the_apis_text_is_quoted(watch, tmp_path):
    """A tag name the API gives is quoted as code, so it cannot mention a
    person in the issue, and a backtick in it cannot end the quotation."""
    _stub(watch, _answers(watch, tags=("v1 @someone`x",)))
    text = _run(watch, tmp_path)[1]
    assert "`v1 @someone'x`" in text
    assert "@someone`" not in text


def test_an_answer_over_the_cap_is_refused(watch, monkeypatch):
    """The script reads at most MAX_BYTES of an answer, and one larger
    stops the check."""

    class Answer:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self, size):
            return b"x" * size

    monkeypatch.setattr(watch.urllib.request, "urlopen", lambda req, timeout: Answer())
    with pytest.raises(ValueError, match="larger than"):
        watch._get(f"{watch.API}/tags?per_page=100")


def test_a_file_the_agldwg_adds_is_information_only(watch, tmp_path):
    """A file in a watched folder that the copy neither holds nor leaves out
    on purpose is reported, and is not a reason to fail. A file outside
    them, such as the HTML page, is not."""
    answers = _answers(watch)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"] = _tree(
        watch, [("rdf/datatype-extra.ttl", "3" * 40)]
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "For information" in text and "`rdf/datatype-extra.ttl`" in text
    assert "html/datatype.html" not in text


def test_the_token_never_follows_a_redirect(watch, monkeypatch):
    """The token goes in an unredirected header, and only to the API."""
    seen = []

    class Answer:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self, size=-1):
            return b"{}"

    def urlopen(req, timeout):
        seen.append(req)
        return Answer()

    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    monkeypatch.setattr(watch.urllib.request, "urlopen", urlopen)
    watch._get(f"{watch.API}/tags?per_page=100")
    watch._get("https://api.github.com/repos/AGLDWG/datatype-ont-elsewhere/tags")
    assert seen[0].unredirected_hdrs == {"Authorization": "Bearer secret"}
    assert "Authorization" not in seen[0].headers
    assert seen[1].unredirected_hdrs == {}


def test_the_namespace_check_sends_no_token_and_follows_no_redirect(watch, monkeypatch):
    """The namespace's host gets no token, and its redirect is read, not
    followed."""
    seen = []

    class Opener:
        def open(self, req, timeout):
            seen.append(req)
            raise urllib.error.HTTPError(
                req.full_url, 302, "Found", {"Location": "https://example.org/x"}, None
            )

    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    monkeypatch.setattr(
        watch.urllib.request, "build_opener", lambda *handlers: Opener()
    )
    assert watch._location(watch.NAMESPACE) == "https://example.org/x"
    assert seen[0].unredirected_hdrs == {}
    assert "Authorization" not in seen[0].headers
    assert seen[0].headers["Accept"] == "text/turtle"


def test_the_patterns_read_the_pinned_copy(watch):
    """The patterns that stand in for a Turtle parser read the copied file's
    date and licence as the pins name them."""
    assert watch.stated(TURTLE) == (
        [watch.PINNED_EDITION],
        [watch.PINNED_ONTOLOGY_LICENSE],
    )


def test_a_new_edition_is_reported(watch, tmp_path):
    """A changed Turtle file with a new dcterms:modified date names a new
    edition, and the date, which the file chose, is quoted as code."""
    turtle = TURTLE.replace(b'"2019-10-03"', b'"2026-01-01 @someone`x"')
    _stub(watch, _with_turtle(watch, turtle))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The changed `rdf/datatype.ttl` states `dcterms:modified` "
        "`2026-01-01 @someone'x`, not the pinned 2019-10-03.**"
    ) in text
    assert "@someone`" not in text
    assert "It still states the `dcterms:license`" in text


def test_a_change_with_the_same_date_names_no_new_edition(watch, tmp_path):
    """A changed Turtle file that keeps its date is reported as a change,
    since master moved, and as no new edition."""
    turtle = TURTLE.replace(b"Class to encapsulate a textual value", b"A text")
    _stub(watch, _with_turtle(watch, turtle))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`master` changes `rdf/datatype.ttl`.**" in text
    assert (
        "The changed `rdf/datatype.ttl` still states `dcterms:modified` "
        "2019-10-03, so the change names no new edition."
    ) in text
    assert "It still states the `dcterms:license`" in text


def test_a_changed_ontology_licence_is_reported(watch, tmp_path):
    """A changed Turtle file that states another dcterms:license sets
    attention, whatever GitHub detects from the LICENSE file."""
    turtle = TURTLE.replace(
        b"http://creativecommons.org/publicdomain/zero/1.0/",
        b"https://creativecommons.org/licenses/by-nc/4.0/",
    )
    _stub(watch, _with_turtle(watch, turtle))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The changed `rdf/datatype.ttl` states the `dcterms:license` "
        "`https://creativecommons.org/licenses/by-nc/4.0/`, not "
    ) in text
    assert "still states `dcterms:modified` 2019-10-03" in text


def test_a_turtle_file_the_watch_cannot_read_is_reported(watch, tmp_path):
    """A changed Turtle file whose date and licence the patterns cannot
    find is reported, not passed."""
    _stub(watch, _with_turtle(watch, b"@prefix data: <x> .\n"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "states `dcterms:modified` none the watch can read" in text
    assert "states the `dcterms:license` none the watch can read" in text


def test_a_blob_that_is_not_its_hash_could_not_finish(watch, tmp_path):
    """A blob whose bytes do not hash to the tree's hash is not read."""
    answers = _with_turtle(watch, TURTLE.replace(b"2019-10-03", b"2026-01-01"))
    for url, answer in answers.items():
        if "/git/blobs/" in url:
            answer["content"] = base64.b64encode(TURTLE).decode()
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The statements check could not finish: `the blob " in text
    assert "does not match its hash`.**" in text
    assert "2026-01-01" not in text


def test_a_head_that_is_no_hash_goes_in_no_url(watch, tmp_path):
    """A commit name the API gives that is not a git object hash stops the
    checks that would put it in a URL."""
    answers = _answers(watch)
    answers[f"{watch.API}/git/ref/heads/master"] = {"object": {"sha": "../x?y"}}
    asked = []
    _stub(watch, answers)
    get = watch._get
    watch._get = lambda url: asked.append(url) or get(url)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The edition check could not finish: `the API names '../x?y', not" in text
    assert "**The copy check could not finish: `" in text
    assert "**The statements check could not finish: `" in text
    assert not [url for url in asked if "../x" in url]


def test_a_broken_copy_is_reported(watch, tmp_path, monkeypatch):
    """A copied file that is missing, edited or not pinned, and a pinned
    commit whose file is not the pinned blob, are each reported."""
    copy = tmp_path / "upstream"
    (copy / "rdf").mkdir(parents=True)
    (copy / "rdf" / "datatype.ttl").write_bytes(TURTLE + b"# edited\n")
    (copy / "rdf" / "extra.ttl").write_text("", encoding="utf-8")
    monkeypatch.setattr(watch, "COPY", copy)
    answers = _answers(watch)
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "0 of 2 copied files match the pinned commit" in text
    assert "**3 problem(s) with the copy:**" in text
    assert "  - `LICENSE` is missing from the copy" in text
    assert "  - `rdf/datatype.ttl` differs from its file at `dd8f24120cd5`" in text
    assert "  - `rdf/extra.ttl` is in the copy but not pinned" in text

    tree = answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"]
    for entry in tree["tree"]:
        if entry["path"] == "rdf/datatype.ttl":
            entry["sha"] = "7" * 40
    watch._tree.cache_clear()
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "  - `rdf/datatype.ttl` at commit `dd8f24120cd5` is not the pinned blob"
    ) in text
