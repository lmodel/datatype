package None;

import java.util.List;
import lombok.*;



/* version: 1.0 */


/**
  Class to encapsulate a classifier, usually a values from a controlled vocabulary
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Concept  {

  private String value;
  private String vocabulary;

}