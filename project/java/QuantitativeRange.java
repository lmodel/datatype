package None;

import java.util.List;
import lombok.*;



/* version: 1.0 */


/**
  Class to encapsulate a quantitative range
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QuantitativeRange  {

  private BigDecimal min;
  private BigDecimal max;
  private String unit;
  private BigDecimal uncertainty;

}