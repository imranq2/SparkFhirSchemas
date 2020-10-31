from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.examplescenario_containedinstance import ExampleScenario_ContainedInstance
from spark_fhir_schemas.r4.resources.examplescenario_containedinstance import ExampleScenario_ContainedInstance


class ExampleScenario_Operation:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("number", StringType(), True),
                StructField("type", StringType(), True),
                StructField("name", StringType(), True),
                StructField("initiator", StringType(), True),
                StructField("receiver", StringType(), True),
                StructField("description", markdown.get_schema(), True),
                StructField("initiatorActive", BooleanType(), True),
                StructField("receiverActive", BooleanType(), True),
                StructField("request", ExampleScenario_ContainedInstance.get_schema(), True),
                StructField("response", ExampleScenario_ContainedInstance.get_schema(), True),]
        )

        return schema
