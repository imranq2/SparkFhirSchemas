from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class QuestionnaireResponse_Answer:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A structured set of questions and their answers. The questions are ordered and
        grouped into coherent subsets, corresponding to the structure of the grouping
        of the questionnaire being responded to.


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

        valueBoolean: The answer (or one of the answers) provided by the respondent to the question.

        valueDecimal: The answer (or one of the answers) provided by the respondent to the question.

        valueInteger: The answer (or one of the answers) provided by the respondent to the question.

        valueDate: The answer (or one of the answers) provided by the respondent to the question.

        valueDateTime: The answer (or one of the answers) provided by the respondent to the question.

        valueTime: The answer (or one of the answers) provided by the respondent to the question.

        valueString: The answer (or one of the answers) provided by the respondent to the question.

        valueUri: The answer (or one of the answers) provided by the respondent to the question.

        valueAttachment: The answer (or one of the answers) provided by the respondent to the question.

        valueCoding: The answer (or one of the answers) provided by the respondent to the question.

        valueQuantity: The answer (or one of the answers) provided by the respondent to the question.

        valueReference: The answer (or one of the answers) provided by the respondent to the question.

        item: Nested groups and/or questions found within this particular answer.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.questionnaireresponse_item import QuestionnaireResponse_Item
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
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueBoolean", BooleanType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueDecimal", IntegerType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueInteger", IntegerType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueDate", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueDateTime", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueTime", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueString", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueUri", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Nested groups and/or questions found within this particular answer.
                StructField(
                    "item",
                    ArrayType(
                        QuestionnaireResponse_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
