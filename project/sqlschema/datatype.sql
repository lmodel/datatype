-- # Class: Boolean Description: Class to encapsulate a true-or-false value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
-- # Class: Concept Description: Class to encapsulate a classifier, usually a values from a controlled vocabulary
--     * Slot: id
--     * Slot: rdf_value Description: The main value of a structured value, as RDF's own rdf:value property names it. The ontology restricts it on Concept and makes value, min, max and uncertainty its sub-properties.
--     * Slot: vocabulary Description: controlled vocabulary, taxonomy etc
-- # Class: Count Description: Class to encapsulate an integer value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
-- # Class: QuantitativeMeasure Description: Class to encapsulate a quantitative measure value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
--     * Slot: unit Description: Measurement scale
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
-- # Class: QuantitativeRange Description: Class to encapsulate a quantitative range
--     * Slot: id
--     * Slot: min Description: Minimum value of range
--     * Slot: max Description: Maximum value of a range
--     * Slot: unit Description: Measurement scale
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
-- # Class: Percent Description: Class to encapsulate a quantitative measure expressed as a percent value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
--     * Slot: unit Description: Measurement scale
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
-- # Class: PercentRange Description: Class to encapsulate a quantitative range expressed as in percent values
--     * Slot: id
--     * Slot: min Description: Minimum value of range
--     * Slot: max Description: Maximum value of a range
--     * Slot: unit Description: Measurement scale
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
-- # Class: Text Description: Class to encapsulate a textual value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)

CREATE TABLE "Boolean" (
	id INTEGER NOT NULL,
	value BOOLEAN NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Boolean_id" ON "Boolean" (id);

CREATE TABLE "Concept" (
	id INTEGER NOT NULL,
	rdf_value TEXT NOT NULL,
	vocabulary TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Concept_id" ON "Concept" (id);

CREATE TABLE "Count" (
	id INTEGER NOT NULL,
	value INTEGER NOT NULL,
	uncertainty NUMERIC,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Count_id" ON "Count" (id);

CREATE TABLE "QuantitativeMeasure" (
	id INTEGER NOT NULL,
	value NUMERIC NOT NULL,
	unit TEXT NOT NULL,
	uncertainty NUMERIC,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_QuantitativeMeasure_id" ON "QuantitativeMeasure" (id);

CREATE TABLE "QuantitativeRange" (
	id INTEGER NOT NULL,
	min NUMERIC NOT NULL,
	max NUMERIC NOT NULL,
	unit TEXT NOT NULL,
	uncertainty NUMERIC,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_QuantitativeRange_id" ON "QuantitativeRange" (id);

CREATE TABLE "Percent" (
	id INTEGER NOT NULL,
	value NUMERIC NOT NULL,
	unit TEXT NOT NULL,
	uncertainty NUMERIC,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Percent_id" ON "Percent" (id);

CREATE TABLE "PercentRange" (
	id INTEGER NOT NULL,
	min NUMERIC NOT NULL,
	max NUMERIC NOT NULL,
	unit TEXT NOT NULL,
	uncertainty NUMERIC,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PercentRange_id" ON "PercentRange" (id);

CREATE TABLE "Text" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Text_id" ON "Text" (id);
