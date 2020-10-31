from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence_Roc:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Raw data describing a biological sequence.


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

        score: Invidual data point representing the GQ (genotype quality) score threshold.

        numTP: The number of true positives if the GQ score threshold was set to "score"
            field value.

        numFP: The number of false positives if the GQ score threshold was set to "score"
            field value.

        numFN: The number of false negatives if the GQ score threshold was set to "score"
            field value.

        precision: Calculated precision if the GQ score threshold was set to "score" field value.

        sensitivity: Calculated sensitivity if the GQ score threshold was set to "score" field
            value.

        fMeasure: Calculated fScore if the GQ score threshold was set to "score" field value.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
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
                # Invidual data point representing the GQ (genotype quality) score threshold.
                StructField(
                    "score",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                # The number of true positives if the GQ score threshold was set to "score"
                # field value.
                StructField(
                    "numTP",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                # The number of false positives if the GQ score threshold was set to "score"
                # field value.
                StructField(
                    "numFP",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                # The number of false negatives if the GQ score threshold was set to "score"
                # field value.
                StructField(
                    "numFN",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                # Calculated precision if the GQ score threshold was set to "score" field value.
                StructField(
                    "precision",
                    ArrayType(decimal.get_schema(recursion_depth + 1)), True
                ),
                # Calculated sensitivity if the GQ score threshold was set to "score" field
                # value.
                StructField(
                    "sensitivity",
                    ArrayType(decimal.get_schema(recursion_depth + 1)), True
                ),
                # Calculated fScore if the GQ score threshold was set to "score" field value.
                StructField(
                    "fMeasure",
                    ArrayType(decimal.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
