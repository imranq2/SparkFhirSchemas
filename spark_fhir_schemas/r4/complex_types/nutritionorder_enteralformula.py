from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.nutritionorder_administration import NutritionOrder_Administration
from spark_fhir_schemas.r4.complex_types.quantity import Quantity


class NutritionOrder_EnteralFormula:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("baseFormulaType", CodeableConcept.get_schema(), True),
                StructField("baseFormulaProductName", StringType(), True),
                StructField("additiveType", CodeableConcept.get_schema(), True),
                StructField("additiveProductName", StringType(), True),
                StructField("caloricDensity", Quantity.get_schema(), True),
                StructField("routeofAdministration", CodeableConcept.get_schema(), True),
                StructField("administration",ArrayType(NutritionOrder_Administration.get_schema()), True),
                StructField("maxVolumeToDeliver", Quantity.get_schema(), True),
                StructField("administrationInstruction", StringType(), True),
            ]
        )

        return schema
