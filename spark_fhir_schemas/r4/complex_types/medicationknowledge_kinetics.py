from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.duration import Duration


# noinspection PyPep8Naming
class MedicationKnowledge_Kinetics:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "areaUnderCurve", ArrayType(Quantity.get_schema()), True
                ),
                StructField(
                    "lethalDose50", ArrayType(Quantity.get_schema()), True
                ),
                StructField("halfLifePeriod", Duration.get_schema(), True),
            ]
        )

        return schema
