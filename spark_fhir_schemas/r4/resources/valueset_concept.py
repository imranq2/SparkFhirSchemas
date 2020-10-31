from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.valueset_designation import ValueSet_Designation


class ValueSet_Concept:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", code.get_schema(), True),
                StructField("display", StringType(), True),
                StructField("designation",ArrayType(ValueSet_Designation.get_schema()), True),]
        )

        return schema
