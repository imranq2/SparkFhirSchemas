from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TerminologyCapabilities_Version:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_filter import TerminologyCapabilities_Filter
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("code", StringType(), True),
                StructField("isDefault", BooleanType(), True),
                StructField("compositional", BooleanType(), True),
                StructField(
                    "language",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "filter",
                    ArrayType(
                        TerminologyCapabilities_Filter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "property",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
