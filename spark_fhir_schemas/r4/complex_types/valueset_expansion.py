from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet_Expansion:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.valueset_parameter import ValueSet_Parameter
        from spark_fhir_schemas.r4.complex_types.valueset_contains import ValueSet_Contains
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
                StructField(
                    "identifier", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "timestamp", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "total", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "offset", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "parameter",
                    ArrayType(
                        ValueSet_Parameter.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "contains",
                    ArrayType(
                        ValueSet_Contains.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
