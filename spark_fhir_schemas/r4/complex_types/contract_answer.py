from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_Answer:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


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

        valueBoolean: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueDecimal: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueInteger: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueDate: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueDateTime: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueTime: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueString: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueUri: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueAttachment: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueCoding: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueQuantity: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueReference: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueBoolean", BooleanType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueDecimal", IntegerType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueInteger", IntegerType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueDate", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueDateTime", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueTime", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueString", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueUri", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
