from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TestScript_Action1:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.testscript_operation import TestScript_Operation
        from spark_fhir_schemas.r4.complex_types.testscript_assert import TestScript_Assert
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
                    "operation",
                    TestScript_Operation.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "assert",
                    TestScript_Assert.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
