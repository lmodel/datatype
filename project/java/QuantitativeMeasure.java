package None;

import java.util.List;
import lombok.*;



/* version: 1.0 */


/**
  Class to encapsulate a quantitative measure value
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QuantitativeMeasure  {

  private BigDecimal value;
  private String unit;
  private BigDecimal uncertainty;
  private String standard;

}