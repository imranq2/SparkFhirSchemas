from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.time import time
from spark_fhir_schemas.r4.complex_types.time import time


class Location_HoursOfOperation:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("daysOfWeek",ArrayType(code.get_schema()), True),
                StructField("allDay", BooleanType(), True),
                StructField("openingTime", time.get_schema(), True),
                StructField("closingTime", time.get_schema(), True),
            ]
        )

        return schema
