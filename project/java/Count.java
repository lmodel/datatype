package None;

import java.util.List;
import lombok.*;






/**
  Class to encapsulate an integer value
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Count  {

  private int value;
  private BigDecimal uncertainty;

}