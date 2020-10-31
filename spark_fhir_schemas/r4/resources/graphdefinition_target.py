from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.graphdefinition_compartment import GraphDefinition_Compartment
from spark_fhir_schemas.r4.resources.graphdefinition_link import GraphDefinition_Link


class GraphDefinition_Target:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", code.get_schema(), True),
                StructField("params", StringType(), True),
                StructField("profile", canonical.get_schema(), True),
                StructField("compartment",ArrayType(GraphDefinition_Compartment.get_schema()), True),
                StructField("link",ArrayType(GraphDefinition_Link.get_schema()), True),]
        )

        return schema
