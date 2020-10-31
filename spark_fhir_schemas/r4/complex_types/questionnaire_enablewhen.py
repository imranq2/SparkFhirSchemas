from typing import List
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
class Questionnaire_EnableWhenSchema:
    """
    A structured set of questions intended to guide the collection of answers from
    end-users. Questionnaires provide detailed control over order, presentation,
    phraseology and grouping to allow coherent, consistent data collection.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
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

        question: The linkId for the question whose answer (or lack of answer) governs whether
            this item is enabled.

        operator: Specifies the criteria by which the question is enabled.

        answerBoolean: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerDecimal: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerInteger: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerDate: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerDateTime: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerTime: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerString: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerCoding: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerQuantity: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerReference: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        if recursion_list.count(
            "Questionnaire_EnableWhen"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + [
            "Questionnaire_EnableWhen"
        ]
        schema = StructType(
            [
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The linkId for the question whose answer (or lack of answer) governs whether
                # this item is enabled.
                StructField("question", StringType(), True),
                # Specifies the criteria by which the question is enabled.
                StructField("operator", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerBoolean", BooleanType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerDecimal", IntegerType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerInteger", IntegerType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerDate", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerDateTime", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerTime", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerString", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField(
                    "answerCoding",
                    CodingSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField(
                    "answerQuantity",
                    QuantitySchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField(
                    "answerReference",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
            ]
        )
        return schema
