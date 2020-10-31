from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Encounter_HospitalizationSchema:
    """
    An interaction between a patient and healthcare provider(s) for the purpose of
    providing healthcare service(s) or assessing the health status of a patient.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An interaction between a patient and healthcare provider(s) for the purpose of
        providing healthcare service(s) or assessing the health status of a patient.


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

        preAdmissionIdentifier: Pre-admission identifier.

        origin: The location/organization from which the patient came before admission.

        admitSource: From where patient was admitted (physician referral, transfer).

        reAdmission: Whether this hospitalization is a readmission and why if known.

        dietPreference: Diet preferences reported by the patient.

        specialCourtesy: Special courtesies (VIP, board member).

        specialArrangement: Any special requests that have been made for this hospitalization encounter,
            such as the provision of specific equipment or other things.

        destination: Location/organization to which the patient is discharged.

        dischargeDisposition: Category or kind of location after discharge.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Pre-admission identifier.
                StructField(
                    "preAdmissionIdentifier",
                    IdentifierSchema.get_schema(recursion_depth + 1), True
                ),
                # The location/organization from which the patient came before admission.
                StructField(
                    "origin", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # From where patient was admitted (physician referral, transfer).
                StructField(
                    "admitSource",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Whether this hospitalization is a readmission and why if known.
                StructField(
                    "reAdmission",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Diet preferences reported by the patient.
                StructField(
                    "dietPreference",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Special courtesies (VIP, board member).
                StructField(
                    "specialCourtesy",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Any special requests that have been made for this hospitalization encounter,
                # such as the provision of specific equipment or other things.
                StructField(
                    "specialArrangement",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Location/organization to which the patient is discharged.
                StructField(
                    "destination",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # Category or kind of location after discharge.
                StructField(
                    "dischargeDisposition",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
