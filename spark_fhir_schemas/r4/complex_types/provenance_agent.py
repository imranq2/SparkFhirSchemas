from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Provenance_Agent:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                    "role",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "onBehalfOf", Reference.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
