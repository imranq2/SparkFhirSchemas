from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.datetime import dateTime


class MarketingStatus:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("country", CodeableConcept.get_schema(), True),
                StructField("jurisdiction", CodeableConcept.get_schema(), True),
                StructField("status", CodeableConcept.get_schema(), True),
                StructField("dateRange", Period.get_schema(), True),
                StructField("restoreDate", dateTime.get_schema(), True),]
        )

        return schema
