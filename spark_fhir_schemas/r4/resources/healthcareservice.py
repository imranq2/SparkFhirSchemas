from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class HealthcareService:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The details of a healthcare service available at a location.


        resourceType: This is a HealthcareService resource

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

        identifier: External identifiers for this item.

        active: This flag is used to mark the record to not be used. This is not used when a
            center is closed for maintenance, or for holidays, the notAvailable period is
            to be used for this.

        providedBy: The organization that provides this healthcare service.

        category: Identifies the broad category of service being performed or delivered.

        type: The specific type of service that may be delivered or performed.

        specialty: Collection of specialties handled by the service site. This is more of a
            medical term.

        location: The location(s) where this healthcare service may be provided.

        name: Further description of the service as it would be presented to a consumer
            while searching.

        comment: Any additional description of the service and/or any specific issues not
            covered by the other attributes, which can be displayed as further detail
            under the serviceName.

        extraDetails: Extra details about the service that can't be placed in the other fields.

        photo: If there is a photo/symbol associated with this HealthcareService, it may be
            included here to facilitate quick identification of the service in a list.

        telecom: List of contacts related to this specific healthcare service.

        coverageArea: The location(s) that this service is available to (not where the service is
            provided).

        serviceProvisionCode: The code(s) that detail the conditions under which the healthcare service is
            available/offered.

        eligibility: Does this service have specific eligibility requirements that need to be met
            in order to use the service?

        program: Programs that this service is applicable to.

        characteristic: Collection of characteristics (attributes).

        communication: Some services are specifically made available in multiple languages, this
            property permits a directory to declare the languages this is offered in.
            Typically this is only provided where a service operates in communities with
            mixed languages used.

        referralMethod: Ways that the service accepts referrals, if this is not provided then it is
            implied that no referral is required.

        appointmentRequired: Indicates whether or not a prospective consumer will require an appointment
            for a particular service at a site to be provided by the Organization.
            Indicates if an appointment is required for access to this service.

        availableTime: A collection of times that the Service Site is available.

        notAvailable: The HealthcareService is not available during this period of time due to the
            provided reason.

        availabilityExceptions: A description of site availability exceptions, e.g. public holiday
            availability. Succinctly describing all possible exceptions to normal site
            availability as details in the available Times and not available Times.

        endpoint: Technical endpoints providing access to services operated for the specific
            healthcare services defined at this resource.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.healthcareservice_eligibility import HealthcareService_Eligibility
        from spark_fhir_schemas.r4.complex_types.healthcareservice_availabletime import HealthcareService_AvailableTime
        from spark_fhir_schemas.r4.complex_types.healthcareservice_notavailable import HealthcareService_NotAvailable
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a HealthcareService resource
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
                # External identifiers for this item.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # This flag is used to mark the record to not be used. This is not used when a
                # center is closed for maintenance, or for holidays, the notAvailable period is
                # to be used for this.
                StructField("active", BooleanType(), True),
                # The organization that provides this healthcare service.
                StructField(
                    "providedBy", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Identifies the broad category of service being performed or delivered.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The specific type of service that may be delivered or performed.
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Collection of specialties handled by the service site. This is more of a
                # medical term.
                StructField(
                    "specialty",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The location(s) where this healthcare service may be provided.
                StructField(
                    "location",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Further description of the service as it would be presented to a consumer
                # while searching.
                StructField("name", StringType(), True),
                # Any additional description of the service and/or any specific issues not
                # covered by the other attributes, which can be displayed as further detail
                # under the serviceName.
                StructField("comment", StringType(), True),
                # Extra details about the service that can't be placed in the other fields.
                StructField(
                    "extraDetails", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # If there is a photo/symbol associated with this HealthcareService, it may be
                # included here to facilitate quick identification of the service in a list.
                StructField(
                    "photo", Attachment.get_schema(recursion_depth + 1), True
                ),
                # List of contacts related to this specific healthcare service.
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                # The location(s) that this service is available to (not where the service is
                # provided).
                StructField(
                    "coverageArea",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The code(s) that detail the conditions under which the healthcare service is
                # available/offered.
                StructField(
                    "serviceProvisionCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Does this service have specific eligibility requirements that need to be met
                # in order to use the service?
                StructField(
                    "eligibility",
                    ArrayType(
                        HealthcareService_Eligibility.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Programs that this service is applicable to.
                StructField(
                    "program",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Collection of characteristics (attributes).
                StructField(
                    "characteristic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Some services are specifically made available in multiple languages, this
                # property permits a directory to declare the languages this is offered in.
                # Typically this is only provided where a service operates in communities with
                # mixed languages used.
                StructField(
                    "communication",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Ways that the service accepts referrals, if this is not provided then it is
                # implied that no referral is required.
                StructField(
                    "referralMethod",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates whether or not a prospective consumer will require an appointment
                # for a particular service at a site to be provided by the Organization.
                # Indicates if an appointment is required for access to this service.
                StructField("appointmentRequired", BooleanType(), True),
                # A collection of times that the Service Site is available.
                StructField(
                    "availableTime",
                    ArrayType(
                        HealthcareService_AvailableTime.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The HealthcareService is not available during this period of time due to the
                # provided reason.
                StructField(
                    "notAvailable",
                    ArrayType(
                        HealthcareService_NotAvailable.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A description of site availability exceptions, e.g. public holiday
                # availability. Succinctly describing all possible exceptions to normal site
                # availability as details in the available Times and not available Times.
                StructField("availabilityExceptions", StringType(), True),
                # Technical endpoints providing access to services operated for the specific
                # healthcare services defined at this resource.
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
