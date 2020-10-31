from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept


class ClaimResponse_Error:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("itemSequence", positiveInt.get_schema(), True),
                StructField("detailSequence", positiveInt.get_schema(), True),
                StructField("subDetailSequence", positiveInt.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),]
        )

        return schema
