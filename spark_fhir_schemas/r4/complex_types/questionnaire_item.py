from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Questionnaire_Item:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        linkId: An identifier that is unique within the Questionnaire allowing linkage to the
            equivalent item in a QuestionnaireResponse resource.

        definition: This element is a URI that refers to an [[[ElementDefinition]]] that provides
            information about this item, including information that might otherwise be
            included in the instance of the Questionnaire resource. A detailed description
            of the construction of the URI is shown in Comments, below. If this element is
            present then the following element values MAY be derived from the Element
            Definition if the corresponding elements of this Questionnaire resource
            instance have no value:

            * code (ElementDefinition.code)
            * type (ElementDefinition.type)
            * required (ElementDefinition.min)
            * repeats (ElementDefinition.max)
            * maxLength (ElementDefinition.maxLength)
            * answerValueSet (ElementDefinition.binding)
            * options (ElementDefinition.binding).

        code: A terminology code that corresponds to this group or question (e.g. a code
            from LOINC, which defines many questions and answers).

        prefix: A short label for a particular group, question or set of display text within
            the questionnaire used for reference by the individual completing the
            questionnaire.

        text: The name of a section, the text of a question or text content for a display
            item.

        type: The type of questionnaire item this is - whether text for display, a grouping
            of other items or a particular type of data to be captured (string, integer,
            coded choice, etc.).

        enableWhen: A constraint indicating that this item should only be enabled (displayed/allow
            answers to be captured) when the specified condition is true.

        enableBehavior: Controls how multiple enableWhen values are interpreted -  whether all or any
            must be true.

        required: An indication, if true, that the item must be present in a "completed"
            QuestionnaireResponse.  If false, the item may be skipped when answering the
            questionnaire.

        repeats: An indication, if true, that the item may occur multiple times in the
            response, collecting multiple answers for questions or multiple sets of
            answers for groups.

        readOnly: An indication, when true, that the value cannot be changed by a human
            respondent to the Questionnaire.

        maxLength: The maximum number of characters that are permitted in the answer to be
            considered a "valid" QuestionnaireResponse.

        answerValueSet: A reference to a value set containing a list of codes representing permitted
            answers for a "choice" or "open-choice" question.

        answerOption: One of the permitted answers for a "choice" or "open-choice" question.

        initial: One or more values that should be pre-populated in the answer when initially
            rendering the questionnaire for user input.

        item: Text, questions and other groups to be nested beneath a question or group.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.questionnaire_enablewhen import Questionnaire_EnableWhen
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.questionnaire_answeroption import Questionnaire_AnswerOption
        from spark_fhir_schemas.r4.complex_types.questionnaire_initial import Questionnaire_Initial
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # An identifier that is unique within the Questionnaire allowing linkage to the
                # equivalent item in a QuestionnaireResponse resource.
                StructField("linkId", StringType(), True),
                # This element is a URI that refers to an [[[ElementDefinition]]] that provides
                # information about this item, including information that might otherwise be
                # included in the instance of the Questionnaire resource. A detailed description
                # of the construction of the URI is shown in Comments, below. If this element is
                # present then the following element values MAY be derived from the Element
                # Definition if the corresponding elements of this Questionnaire resource
                # instance have no value:
                #
                # * code (ElementDefinition.code)
                # * type (ElementDefinition.type)
                # * required (ElementDefinition.min)
                # * repeats (ElementDefinition.max)
                # * maxLength (ElementDefinition.maxLength)
                # * answerValueSet (ElementDefinition.binding)
                # * options (ElementDefinition.binding).
                StructField(
                    "definition", uri.get_schema(recursion_depth + 1), True
                ),
                # A terminology code that corresponds to this group or question (e.g. a code
                # from LOINC, which defines many questions and answers).
                StructField(
                    "code", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                # A short label for a particular group, question or set of display text within
                # the questionnaire used for reference by the individual completing the
                # questionnaire.
                StructField("prefix", StringType(), True),
                # The name of a section, the text of a question or text content for a display
                # item.
                StructField("text", StringType(), True),
                # The type of questionnaire item this is - whether text for display, a grouping
                # of other items or a particular type of data to be captured (string, integer,
                # coded choice, etc.).
                StructField("type", StringType(), True),
                # A constraint indicating that this item should only be enabled (displayed/allow
                # answers to be captured) when the specified condition is true.
                StructField(
                    "enableWhen",
                    ArrayType(
                        Questionnaire_EnableWhen.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Controls how multiple enableWhen values are interpreted -  whether all or any
                # must be true.
                StructField("enableBehavior", StringType(), True),
                # An indication, if true, that the item must be present in a "completed"
                # QuestionnaireResponse.  If false, the item may be skipped when answering the
                # questionnaire.
                StructField("required", BooleanType(), True),
                # An indication, if true, that the item may occur multiple times in the
                # response, collecting multiple answers for questions or multiple sets of
                # answers for groups.
                StructField("repeats", BooleanType(), True),
                # An indication, when true, that the value cannot be changed by a human
                # respondent to the Questionnaire.
                StructField("readOnly", BooleanType(), True),
                # The maximum number of characters that are permitted in the answer to be
                # considered a "valid" QuestionnaireResponse.
                StructField(
                    "maxLength", integer.get_schema(recursion_depth + 1), True
                ),
                # A reference to a value set containing a list of codes representing permitted
                # answers for a "choice" or "open-choice" question.
                StructField(
                    "answerValueSet",
                    canonical.get_schema(recursion_depth + 1), True
                ),
                # One of the permitted answers for a "choice" or "open-choice" question.
                StructField(
                    "answerOption",
                    ArrayType(
                        Questionnaire_AnswerOption.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # One or more values that should be pre-populated in the answer when initially
                # rendering the questionnaire for user input.
                StructField(
                    "initial",
                    ArrayType(
                        Questionnaire_Initial.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Text, questions and other groups to be nested beneath a question or group.
                StructField(
                    "item",
                    ArrayType(
                        Questionnaire_Item.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
