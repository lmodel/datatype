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
  Class to encapsulate a true-or-false value
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Boolean  {

  private boolean value;


}