from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class BiologicallyDerivedProduct_Processing:
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
                StructField("description", StringType(), True),
                StructField("procedure", CodeableConcept.get_schema(), True),
                StructField("additive", Reference.get_schema(), True),
                StructField("timeDateTime", StringType(), True),
                StructField("timePeriod", Period.get_schema(), True),
            ]
        )

        return schema
