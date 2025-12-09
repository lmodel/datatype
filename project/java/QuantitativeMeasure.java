package None;

import java.util.List;
import lombok.*;






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