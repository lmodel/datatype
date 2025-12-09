

/**
 * Class to encapsulate a textual value
 */
export interface Text {
    /** simple value (a literal) */
    value: string,
}


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
    /** simple value (a literal) */
    value: string,
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
    uncertainty?: number,
}


/**
 * Class to encapsulate a quantitative measure value
 */
export interface QuantitativeMeasure {
    /** simple value (a literal) */
    value: number,
    /** Measurement scale */
    unit: string,
    /** Uncertainty for a quantitative value */
    uncertainty?: number,
    /** Measurement standard, scale, uom, reference system, controlled vocabulary, taxonomy etc */
    standard?: string,
}


/**
 * Class to encapsulate a quantitative range
 */
export interface QuantitativeRange {
    /** Minimum value of range */
    min: number,
    /** Maximum value of a range */
    max: number,
    /** Measurement scale */
    unit: string,
    /** Uncertainty for a quantitative value */
    uncertainty?: number,
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



