from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Questionnaire_ItemSchema:
    """
    A structured set of questions intended to guide the collection of answers from
    end-users. Questionnaires provide detailed control over order, presentation,
    phraseology and grouping to allow coherent, consistent data collection.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.


        linkId: An identifier that is unique within the Questionnaire allowing linkage to the
            equivalent item in a QuestionnaireResponse resource.

        definition: A reference to an [[[ElementDefinition]]] that provides the details for the
            item. If a definition is provided, then the following element values can be
            inferred from the definition:

            * code (ElementDefinition.code)
            * type (ElementDefinition.type)
            * required (ElementDefinition.min)
            * repeats (ElementDefinition.max)
            * maxLength (ElementDefinition.maxLength)
            * options (ElementDefinition.binding)

            Any information provided in these elements on a Questionnaire Item overrides
            the information from the definition.

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

        required: An indication, if true, that the item must be present in a "completed"
            QuestionnaireResponse.  If false, the item may be skipped when answering the
            questionnaire.

        repeats: An indication, if true, that the item may occur multiple times in the
            response, collecting multiple answers answers for questions or multiple sets
            of answers for groups.

        readOnly: An indication, when true, that the value cannot be changed by a human
            respondent to the Questionnaire.

        maxLength: The maximum number of characters that are permitted in the answer to be
            considered a "valid" QuestionnaireResponse.

        options: A reference to a value set containing a list of codes representing permitted
            answers for a "choice" or "open-choice" question.

        option: One of the permitted answers for a "choice" or "open-choice" question.

        initialBoolean: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialDecimal: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialInteger: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialDate: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialDateTime: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialTime: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialString: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialUri: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialAttachment: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialCoding: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialQuantity: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        initialReference: The value that should be defaulted when initially rendering the questionnaire
            for user input.

        item: Text, questions and other groups to be nested beneath a question or group.

        """
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.questionnaire_enablewhen import Questionnaire_EnableWhenSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.questionnaire_option import Questionnaire_OptionSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        if (
            max_recursion_limit
            and nesting_list.count("Questionnaire_Item") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Questionnaire_Item"]
        schema = StructType(
            [
                # An identifier that is unique within the Questionnaire allowing linkage to the
                # equivalent item in a QuestionnaireResponse resource.
                StructField("linkId", StringType(), True),
                # A reference to an [[[ElementDefinition]]] that provides the details for the
                # item. If a definition is provided, then the following element values can be
                # inferred from the definition:
                #
                # * code (ElementDefinition.code)
                # * type (ElementDefinition.type)
                # * required (ElementDefinition.min)
                # * repeats (ElementDefinition.max)
                # * maxLength (ElementDefinition.maxLength)
                # * options (ElementDefinition.binding)
                #
                # Any information provided in these elements on a Questionnaire Item overrides
                # the information from the definition.
                StructField("definition", StringType(), True),
                # A terminology code that corresponds to this group or question (e.g. a code
                # from LOINC, which defines many questions and answers).
                StructField(
                    "code",
                    ArrayType(
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
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
                        Questionnaire_EnableWhenSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # An indication, if true, that the item must be present in a "completed"
                # QuestionnaireResponse.  If false, the item may be skipped when answering the
                # questionnaire.
                StructField("required", BooleanType(), True),
                # An indication, if true, that the item may occur multiple times in the
                # response, collecting multiple answers answers for questions or multiple sets
                # of answers for groups.
                StructField("repeats", BooleanType(), True),
                # An indication, when true, that the value cannot be changed by a human
                # respondent to the Questionnaire.
                StructField("readOnly", BooleanType(), True),
                # The maximum number of characters that are permitted in the answer to be
                # considered a "valid" QuestionnaireResponse.
                StructField("maxLength", IntegerType(), True),
                # A reference to a value set containing a list of codes representing permitted
                # answers for a "choice" or "open-choice" question.
                StructField(
                    "options",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # One of the permitted answers for a "choice" or "open-choice" question.
                StructField(
                    "option",
                    ArrayType(
                        Questionnaire_OptionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialBoolean", BooleanType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialDecimal", IntegerType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialInteger", IntegerType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialDate", StringType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialDateTime", StringType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialTime", StringType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialString", StringType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField("initialUri", StringType(), True),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField(
                    "initialAttachment",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField(
                    "initialCoding",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField(
                    "initialQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The value that should be defaulted when initially rendering the questionnaire
                # for user input.
                StructField(
                    "initialReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Text, questions and other groups to be nested beneath a question or group.
                StructField(
                    "item",
                    ArrayType(
                        Questionnaire_ItemSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema