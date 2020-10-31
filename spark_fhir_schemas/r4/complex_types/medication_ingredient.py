from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Medication_Ingredient:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource is primarily used for the identification and definition of a
        medication for the purposes of prescribing, dispensing, and administering a
        medication as well as for making statements about medication use.


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

        itemCodeableConcept: The actual ingredient - either a substance (simple ingredient) or another
            medication of a medication.

        itemReference: The actual ingredient - either a substance (simple ingredient) or another
            medication of a medication.

        isActive: Indication of whether this ingredient affects the therapeutic action of the
            drug.

        strength: Specifies how many (or how much) of the items there are in this Medication.
            For example, 250 mg per tablet.  This is expressed as a ratio where the
            numerator is 250mg and the denominator is 1 tablet.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
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
                # The actual ingredient - either a substance (simple ingredient) or another
                # medication of a medication.
                StructField(
                    "itemCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The actual ingredient - either a substance (simple ingredient) or another
                # medication of a medication.
                StructField(
                    "itemReference", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Indication of whether this ingredient affects the therapeutic action of the
                # drug.
                StructField("isActive", BooleanType(), True),
                # Specifies how many (or how much) of the items there are in this Medication.
                # For example, 250 mg per tablet.  This is expressed as a ratio where the
                # numerator is 250mg and the denominator is 1 tablet.
                StructField(
                    "strength", Ratio.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
