from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.coding import Coding


# noinspection PyPep8Naming
class DataRequirement_CodeFilter:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("path", StringType(), True),
                StructField("searchParam", StringType(), True),
                StructField("valueSet", canonical.get_schema(), True),
                StructField("code", ArrayType(Coding.get_schema()), True),
            ]
        )

        return schema
