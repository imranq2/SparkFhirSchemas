from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AllergyIntolerance_Reaction:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Risk of harmful or undesirable, physiological response which is unique to an
        individual and associated with exposure to a substance.


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

        substance: Identification of the specific substance (or pharmaceutical product)
            considered to be responsible for the Adverse Reaction event. Note: the
            substance for a specific reaction may be different from the substance
            identified as the cause of the risk, but it must be consistent with it. For
            instance, it may be a more specific substance (e.g. a brand medication) or a
            composite product that includes the identified substance. It must be
            clinically safe to only process the 'code' and ignore the
            'reaction.substance'.  If a receiving system is unable to confirm that
            AllergyIntolerance.reaction.substance falls within the semantic scope of
            AllergyIntolerance.code, then the receiving system should ignore
            AllergyIntolerance.reaction.substance.

        manifestation: Clinical symptoms and/or signs that are observed or associated with the
            adverse reaction event.

        description: Text description about the reaction as a whole, including details of the
            manifestation if required.

        onset: Record of the date and/or time of the onset of the Reaction.

        severity: Clinical assessment of the severity of the reaction event as a whole,
            potentially considering multiple different manifestations.

        exposureRoute: Identification of the route by which the subject was exposed to the substance.

        note: Additional text about the adverse reaction event not captured in other fields.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
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
                # Identification of the specific substance (or pharmaceutical product)
                # considered to be responsible for the Adverse Reaction event. Note: the
                # substance for a specific reaction may be different from the substance
                # identified as the cause of the risk, but it must be consistent with it. For
                # instance, it may be a more specific substance (e.g. a brand medication) or a
                # composite product that includes the identified substance. It must be
                # clinically safe to only process the 'code' and ignore the
                # 'reaction.substance'.  If a receiving system is unable to confirm that
                # AllergyIntolerance.reaction.substance falls within the semantic scope of
                # AllergyIntolerance.code, then the receiving system should ignore
                # AllergyIntolerance.reaction.substance.
                StructField(
                    "substance",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Clinical symptoms and/or signs that are observed or associated with the
                # adverse reaction event.
                StructField(
                    "manifestation",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Text description about the reaction as a whole, including details of the
                # manifestation if required.
                StructField("description", StringType(), True),
                # Record of the date and/or time of the onset of the Reaction.
                StructField(
                    "onset", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Clinical assessment of the severity of the reaction event as a whole,
                # potentially considering multiple different manifestations.
                StructField("severity", StringType(), True),
                # Identification of the route by which the subject was exposed to the substance.
                StructField(
                    "exposureRoute",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Additional text about the adverse reaction event not captured in other fields.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
