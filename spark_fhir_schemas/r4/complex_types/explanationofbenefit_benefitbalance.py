from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ExplanationOfBenefit_BenefitBalance:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_financial import ExplanationOfBenefit_Financial
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("excluded", BooleanType(), True),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "network", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "unit", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "term", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "financial",
                    ArrayType(
                        ExplanationOfBenefit_Financial.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
