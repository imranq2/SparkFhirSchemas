from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.quantity import Quantity


class SubstanceSpecification_Moiety:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("role", CodeableConcept.get_schema(), True),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("stereochemistry", CodeableConcept.get_schema(), True),
                StructField("opticalActivity", CodeableConcept.get_schema(), True),
                StructField("molecularFormula", StringType(), True),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountString", StringType(), True),]
        )

        return schema
