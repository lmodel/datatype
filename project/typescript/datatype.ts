

/**
 * Class to encapsulate a true-or-false value
 */
export interface Boolean {
    /** simple value (a literal) */
    value: boolean,
}


/**
 * Class to encapsulate a classifier, usually a values from a controlled vocabulary
 */
export interface Concept {
    /** The main value of a structured value, as RDF's own rdf:value property names it. The ontology restricts it on Concept and makes value, min, max and uncertainty its sub-properties. */
    rdf_value: string,
    /** controlled vocabulary, taxonomy etc */
    vocabulary: string,
}


/**
 * Class to encapsulate an integer value
 */
export interface Count {
    /** simple value (a literal) */
    value: number,
    /** Uncertainty for a quantitative value */
    uncertainty?: string,
}


/**
 * Class to encapsulate a quantitative measure value
 */
export interface QuantitativeMeasure {
    /** simple value (a literal) */
    value: string,
    /** Measurement scale */
    unit: string,
    /** Uncertainty for a quantitative value */
    uncertainty?: string,
}


/**
 * Class to encapsulate a quantitative range
 */
export interface QuantitativeRange {
    /** Minimum value of range */
    min: string,
    /** Maximum value of a range */
    max: string,
    /** Measurement scale */
    unit: string,
    /** Uncertainty for a quantitative value */
    uncertainty?: string,
}


/**
 * Class to encapsulate a quantitative measure expressed as a percent value
 */
export interface Percent extends QuantitativeMeasure {
}


/**
 * Class to encapsulate a quantitative range expressed as in percent values
 */
export interface PercentRange extends QuantitativeRange {
}


/**
 * Class to encapsulate a textual value
 */
export interface Text {
    /** simple value (a literal) */
    value: string,
}



