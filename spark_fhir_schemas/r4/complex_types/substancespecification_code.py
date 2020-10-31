from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SubstanceSpecification_Code:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
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
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "statusDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("comment", StringType(), True),
                StructField(
                    "source",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )

        return schema
