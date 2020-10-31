from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Immunization_Education:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
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
                StructField("documentType", StringType(), True),
                StructField(
                    "reference", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "publicationDate",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "presentationDate",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
