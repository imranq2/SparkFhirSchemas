from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Patient:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Demographics and other administrative information about an individual or
        animal receiving care or other health-related services.


        resourceType: This is a Patient resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: An identifier for this patient.

        active: Whether this patient record is in active use.
            Many systems use this property to mark as non-current patients, such as those
            that have not been seen for a period of time based on an organization's
            business rules.

            It is often used to filter patient lists to exclude inactive patients

            Deceased patients may also be marked as inactive for the same reasons, but may
            be active for some time after death.

        name: A name associated with the individual.

        telecom: A contact detail (e.g. a telephone number or an email address) by which the
            individual may be contacted.

        gender: Administrative Gender - the gender that the patient is considered to have for
            administration and record keeping purposes.

        birthDate: The date of birth for the individual.

        deceasedBoolean: Indicates if the individual is deceased or not.

        deceasedDateTime: Indicates if the individual is deceased or not.

        address: An address for the individual.

        maritalStatus: This field contains a patient's most recent marital (civil) status.

        multipleBirthBoolean: Indicates whether the patient is part of a multiple (boolean) or indicates the
            actual birth order (integer).

        multipleBirthInteger: Indicates whether the patient is part of a multiple (boolean) or indicates the
            actual birth order (integer).

        photo: Image of the patient.

        contact: A contact party (e.g. guardian, partner, friend) for the patient.

        communication: A language which may be used to communicate with the patient about his or her
            health.

        generalPractitioner: Patient's nominated care provider.

        managingOrganization: Organization that is the custodian of the patient record.

        link: Link to another patient resource that concerns the same actual patient.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.humanname import HumanName
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.patient_contact import Patient_Contact
        from spark_fhir_schemas.r4.complex_types.patient_communication import Patient_Communication
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.patient_link import Patient_Link
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Patient resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # An identifier for this patient.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Whether this patient record is in active use.
                # Many systems use this property to mark as non-current patients, such as those
                # that have not been seen for a period of time based on an organization's
                # business rules.
                #
                # It is often used to filter patient lists to exclude inactive patients
                #
                # Deceased patients may also be marked as inactive for the same reasons, but may
                # be active for some time after death.
                StructField("active", BooleanType(), True),
                # A name associated with the individual.
                StructField(
                    "name",
                    ArrayType(HumanName.get_schema(recursion_depth + 1)), True
                ),
                # A contact detail (e.g. a telephone number or an email address) by which the
                # individual may be contacted.
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                # Administrative Gender - the gender that the patient is considered to have for
                # administration and record keeping purposes.
                StructField("gender", StringType(), True),
                # The date of birth for the individual.
                StructField("birthDate", DateType(), True),
                # Indicates if the individual is deceased or not.
                StructField("deceasedBoolean", BooleanType(), True),
                # Indicates if the individual is deceased or not.
                StructField("deceasedDateTime", StringType(), True),
                # An address for the individual.
                StructField(
                    "address",
                    ArrayType(Address.get_schema(recursion_depth + 1)), True
                ),
                # This field contains a patient's most recent marital (civil) status.
                StructField(
                    "maritalStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates whether the patient is part of a multiple (boolean) or indicates the
                # actual birth order (integer).
                StructField("multipleBirthBoolean", BooleanType(), True),
                # Indicates whether the patient is part of a multiple (boolean) or indicates the
                # actual birth order (integer).
                StructField("multipleBirthInteger", IntegerType(), True),
                # Image of the patient.
                StructField(
                    "photo",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
                # A contact party (e.g. guardian, partner, friend) for the patient.
                StructField(
                    "contact",
                    ArrayType(Patient_Contact.get_schema(recursion_depth + 1)),
                    True
                ),
                # A language which may be used to communicate with the patient about his or her
                # health.
                StructField(
                    "communication",
                    ArrayType(
                        Patient_Communication.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Patient's nominated care provider.
                StructField(
                    "generalPractitioner",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Organization that is the custodian of the patient record.
                StructField(
                    "managingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Link to another patient resource that concerns the same actual patient.
                StructField(
                    "link",
                    ArrayType(Patient_Link.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
