from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.measure_population import Measure_Population
from spark_fhir_schemas.r4.complex_types.measure_stratifier import Measure_Stratifier


class Measure_Group:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("description", StringType(), True),
                StructField("population",ArrayType(Measure_Population.get_schema()), True),
                StructField("stratifier",ArrayType(Measure_Stratifier.get_schema()), True),
            ]
        )

        return schema
