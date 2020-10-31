from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Count:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.code import code
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
                    "value", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField("comparator", StringType(), True),
                StructField("unit", StringType(), True),
                StructField(
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
