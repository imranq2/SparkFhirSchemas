from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.testscript_requestheader import TestScript_RequestHeader
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.string import string


class TestScript_Operation:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", Coding.get_schema(), True),
                StructField("resource", code.get_schema(), True),
                StructField("label", StringType(), True),
                StructField("description", StringType(), True),
                StructField("accept", code.get_schema(), True),
                StructField("contentType", code.get_schema(), True),
                StructField("destination", integer.get_schema(), True),
                StructField("encodeRequestUrl", BooleanType(), True),
                StructField("method", StringType(), True),
                StructField("origin", integer.get_schema(), True),
                StructField("params", StringType(), True),
                StructField("requestHeader",ArrayType(TestScript_RequestHeader.get_schema()), True),
                StructField("requestId", id.get_schema(), True),
                StructField("responseId", id.get_schema(), True),
                StructField("sourceId", id.get_schema(), True),
                StructField("targetId", id.get_schema(), True),
                StructField("url", StringType(), True),]
        )

        return schema
