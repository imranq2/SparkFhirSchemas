from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ExampleScenario_Operation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.examplescenario_containedinstance import ExampleScenario_ContainedInstance
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
                StructField("number", StringType(), True),
                StructField("type", StringType(), True),
                StructField("name", StringType(), True),
                StructField("initiator", StringType(), True),
                StructField("receiver", StringType(), True),
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("initiatorActive", BooleanType(), True),
                StructField("receiverActive", BooleanType(), True),
                StructField(
                    "request",
                    ExampleScenario_ContainedInstance.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "response",
                    ExampleScenario_ContainedInstance.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
