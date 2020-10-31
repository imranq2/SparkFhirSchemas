from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Dosage_DoseAndRate:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "doseRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "doseQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "rateRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "rateRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "rateQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
