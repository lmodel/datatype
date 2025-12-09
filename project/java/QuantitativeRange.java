package None;

import java.util.List;
import lombok.*;






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