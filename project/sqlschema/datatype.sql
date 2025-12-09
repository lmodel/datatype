-- # Class: Text Description: Class to encapsulate a textual value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
-- # Class: Boolean Description: Class to encapsulate a true-or-false value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
-- # Class: Concept Description: Class to encapsulate a classifier, usually a values from a controlled vocabulary
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
--     * Slot: vocabulary Description: controlled vocabulary, taxonomy etc
-- # Class: Count Description: Class to encapsulate an integer value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
-- # Class: Quantitative Measure Description: Class to encapsulate a quantitative measure value
--     * Slot: id
--     * Slot: value Description: simple value (a literal)
--     * Slot: unit Description: Measurement scale
--     * Slot: uncertainty Description: Uncertainty for a quantitative value
--     * Slot: standard Description: Measurement standard, scale, uom, reference system, controlled vocabulary, taxonomy etc
-- # Class: Quantitative Range Description: Class to encapsulate a quantitative range
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
--     * Slot: standard Description: Measurement standard, scale, uom, reference system, controlled vocabulary, taxonomy etc
-- # Class: Percent Range Description: Class to encapsulate a quantitative range expressed as in percent values
--     * Slot: id
--     * Slot: min Description: Minimum value of range
--     * Slot: max Description: Maximum value of a range
--     * Slot: unit Description: Measurement scale
--     * Slot: uncertainty Description: Uncertainty for a quantitative value

CREATE TABLE "Text" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Text_id" ON "Text" (id);
CREATE TABLE "Boolean" (
	id INTEGER NOT NULL,
	value BOOLEAN NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Boolean_id" ON "Boolean" (id);
CREATE TABLE "Concept" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	vocabulary TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Concept_id" ON "Concept" (id);
CREATE TABLE "Count" (
	id INTEGER NOT NULL,
	value INTEGER NOT NULL,
	uncertainty FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Count_id" ON "Count" (id);
CREATE TABLE "Quantitative Measure" (
	id INTEGER NOT NULL,
	value FLOAT NOT NULL,
	unit TEXT NOT NULL,
	uncertainty FLOAT,
	standard TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Quantitative Measure_id" ON "Quantitative Measure" (id);
CREATE TABLE "Quantitative Range" (
	id INTEGER NOT NULL,
	min FLOAT NOT NULL,
	max FLOAT NOT NULL,
	unit TEXT NOT NULL,
	uncertainty FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Quantitative Range_id" ON "Quantitative Range" (id);
CREATE TABLE "Percent" (
	id INTEGER NOT NULL,
	value FLOAT NOT NULL,
	unit FLOAT NOT NULL,
	uncertainty FLOAT,
	standard TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Percent_id" ON "Percent" (id);
CREATE TABLE "Percent Range" (
	id INTEGER NOT NULL,
	min FLOAT NOT NULL,
	max FLOAT NOT NULL,
	unit FLOAT NOT NULL,
	uncertainty FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Percent Range_id" ON "Percent Range" (id);
