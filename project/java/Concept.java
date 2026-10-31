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
  Class to encapsulate a classifier, usually a values from a controlled vocabulary
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Concept  {

  private URI rdfValue;
  private URI vocabulary;


}