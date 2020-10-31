from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.testscript_link import TestScript_Link
from spark_fhir_schemas.r4.complex_types.testscript_capability import TestScript_Capability


class TestScript_Metadata:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("link",ArrayType(TestScript_Link.get_schema()), True),
                StructField("capability",ArrayType(TestScript_Capability.get_schema()), True),
            ]
        )

        return schema
