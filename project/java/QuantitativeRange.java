package example;

/* metamodel_version: 1.12.0 */
/* version: 2019-10-03 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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
  private URI unit;
  private BigDecimal uncertainty;


}