from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.url import url
from spark_fhir_schemas.r4.resources.implementationguide_resource1 import ImplementationGuide_Resource1
from spark_fhir_schemas.r4.resources.implementationguide_page1 import ImplementationGuide_Page1
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string


class ImplementationGuide_Manifest:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("rendering", url.get_schema(), True),
                StructField("resource",ArrayType(ImplementationGuide_Resource1.get_schema()), True),
                StructField("page",ArrayType(ImplementationGuide_Page1.get_schema()), True),
                StructField("image",ArrayType(string.get_schema()), True),
                StructField("other",ArrayType(string.get_schema()), True),]
        )

        return schema
