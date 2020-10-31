from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.period import Period


class ContactPoint:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("system", StringType(), True),
                StructField("value", StringType(), True),
                StructField("use", StringType(), True),
                StructField("rank", positiveInt.get_schema(), True),
                StructField("period", Period.get_schema(), True),]
        )

        return schema
