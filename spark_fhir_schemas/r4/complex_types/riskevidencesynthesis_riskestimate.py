from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RiskEvidenceSynthesis_RiskEstimate:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a
        population plus exposure state where the risk estimate is derived from a
        combination of research studies.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        description: Human-readable summary of risk estimate.

        type: Examples include proportion and mean.

        value: The point estimate of the risk estimate.

        unitOfMeasure: Specifies the UCUM unit for the outcome.

        denominatorCount: The sample size for the group that was measured for this risk estimate.

        numeratorCount: The number of group members with the outcome of interest.

        precisionEstimate: A description of the precision of the estimate for the effect.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.riskevidencesynthesis_precisionestimate import RiskEvidenceSynthesis_PrecisionEstimate
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Human-readable summary of risk estimate.
                StructField("description", StringType(), True),
                # Examples include proportion and mean.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The point estimate of the risk estimate.
                StructField(
                    "value", decimal.get_schema(recursion_depth + 1), True
                ),
                # Specifies the UCUM unit for the outcome.
                StructField(
                    "unitOfMeasure",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The sample size for the group that was measured for this risk estimate.
                StructField(
                    "denominatorCount",
                    integer.get_schema(recursion_depth + 1), True
                ),
                # The number of group members with the outcome of interest.
                StructField(
                    "numeratorCount", integer.get_schema(recursion_depth + 1),
                    True
                ),
                # A description of the precision of the estimate for the effect.
                StructField(
                    "precisionEstimate",
                    ArrayType(
                        RiskEvidenceSynthesis_PrecisionEstimate.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
