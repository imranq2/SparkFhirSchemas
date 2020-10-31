from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ServiceRequestSchema:
    """
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A record of a request for service such as diagnostic investigations,
        treatments, or operations to be performed.


        resourceType: This is a ServiceRequest resource

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

        identifier: Identifiers assigned to this order instance by the orderer and/or the receiver
            and/or order fulfiller.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this ServiceRequest.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            ServiceRequest.

        basedOn: Plan/proposal/order fulfilled by this request.

        replaces: The request takes the place of the referenced completed or terminated
            request(s).

        requisition: A shared identifier common to all service requests that were authorized more
            or less simultaneously by a single author, representing the composite or group
            identifier.

        status: The status of the order.

        intent: Whether the request is a proposal, plan, an original order or a reflex order.

        category: A code that classifies the service for searching, sorting and display purposes
            (e.g. "Surgical Procedure").

        priority: Indicates how quickly the ServiceRequest should be addressed with respect to
            other requests.

        doNotPerform: Set this to true if the record is saying that the service/procedure should NOT
            be performed.

        code: A code that identifies a particular service (i.e., procedure, diagnostic
            investigation, or panel of investigations) that have been requested.

        orderDetail: Additional details and instructions about the how the services are to be
            delivered.   For example, and order for a urinary catheter may have an order
            detail for an external or indwelling catheter, or an order for a bandage may
            require additional instructions specifying how the bandage should be applied.

        quantityQuantity: An amount of service being requested which can be a quantity ( for example
            $1,500 home modification), a ratio ( for example, 20 half day visits per
            month), or a range (2.0 to 1.8 Gy per fraction).

        quantityRatio: An amount of service being requested which can be a quantity ( for example
            $1,500 home modification), a ratio ( for example, 20 half day visits per
            month), or a range (2.0 to 1.8 Gy per fraction).

        quantityRange: An amount of service being requested which can be a quantity ( for example
            $1,500 home modification), a ratio ( for example, 20 half day visits per
            month), or a range (2.0 to 1.8 Gy per fraction).

        subject: On whom or what the service is to be performed. This is usually a human
            patient, but can also be requested on animals, groups of humans or animals,
            devices such as dialysis machines, or even locations (typically for
            environmental scans).

        encounter: An encounter that provides additional information about the healthcare context
            in which this request is made.

        occurrenceDateTime: The date/time at which the requested service should occur.

        occurrencePeriod: The date/time at which the requested service should occur.

        occurrenceTiming: The date/time at which the requested service should occur.

        asNeededBoolean: If a CodeableConcept is present, it indicates the pre-condition for performing
            the service.  For example "pain", "on flare-up", etc.

        asNeededCodeableConcept: If a CodeableConcept is present, it indicates the pre-condition for performing
            the service.  For example "pain", "on flare-up", etc.

        authoredOn: When the request transitioned to being actionable.

        requester: The individual who initiated the request and has responsibility for its
            activation.

        performerType: Desired type of performer for doing the requested service.

        performer: The desired performer for doing the requested service.  For example, the
            surgeon, dermatopathologist, endoscopist, etc.

        locationCode: The preferred location(s) where the procedure should actually happen in coded
            or free text form. E.g. at home or nursing day care center.

        locationReference: A reference to the the preferred location(s) where the procedure should
            actually happen. E.g. at home or nursing day care center.

        reasonCode: An explanation or justification for why this service is being requested in
            coded or textual form.   This is often for billing purposes.  May relate to
            the resources referred to in `supportingInfo`.

        reasonReference: Indicates another resource that provides a justification for why this service
            is being requested.   May relate to the resources referred to in
            `supportingInfo`.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be needed for delivering the requested service.

        supportingInfo: Additional clinical information about the patient or specimen that may
            influence the services or their interpretations.     This information includes
            diagnosis, clinical findings and other observations.  In laboratory ordering
            these are typically referred to as "ask at order entry questions (AOEs)".
            This includes observations explicitly requested by the producer (filler) to
            provide context or supporting information needed to complete the order. For
            example,  reporting the amount of inspired oxygen for blood gas measurements.

        specimen: One or more specimens that the laboratory procedure will use.

        bodySite: Anatomic location where the procedure should be performed. This is the target
            site.

        note: Any other notes and comments made about the service request. For example,
            internal billing notes.

        patientInstruction: Instructions in terms that are understood by the patient or consumer.

        relevantHistory: Key events in the history of the request.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.ratio import RatioSchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.timing import TimingSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ServiceRequest resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id", idSchema.get_schema(recursion_depth + 1), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", MetaSchema.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uriSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", codeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", NarrativeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Identifiers assigned to this order instance by the orderer and/or the receiver
                # and/or order fulfiller.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this ServiceRequest.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonicalSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # ServiceRequest.
                StructField(
                    "instantiatesUri",
                    ArrayType(uriSchema.get_schema(recursion_depth + 1)), True
                ),
                # Plan/proposal/order fulfilled by this request.
                StructField(
                    "basedOn",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The request takes the place of the referenced completed or terminated
                # request(s).
                StructField(
                    "replaces",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # A shared identifier common to all service requests that were authorized more
                # or less simultaneously by a single author, representing the composite or group
                # identifier.
                StructField(
                    "requisition",
                    IdentifierSchema.get_schema(recursion_depth + 1), True
                ),
                # The status of the order.
                StructField(
                    "status", codeSchema.get_schema(recursion_depth + 1), True
                ),
                # Whether the request is a proposal, plan, an original order or a reflex order.
                StructField(
                    "intent", codeSchema.get_schema(recursion_depth + 1), True
                ),
                # A code that classifies the service for searching, sorting and display purposes
                # (e.g. "Surgical Procedure").
                StructField(
                    "category",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Indicates how quickly the ServiceRequest should be addressed with respect to
                # other requests.
                StructField(
                    "priority", codeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # Set this to true if the record is saying that the service/procedure should NOT
                # be performed.
                StructField("doNotPerform", BooleanType(), True),
                # A code that identifies a particular service (i.e., procedure, diagnostic
                # investigation, or panel of investigations) that have been requested.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Additional details and instructions about the how the services are to be
                # delivered.   For example, and order for a urinary catheter may have an order
                # detail for an external or indwelling catheter, or an order for a bandage may
                # require additional instructions specifying how the bandage should be applied.
                StructField(
                    "orderDetail",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An amount of service being requested which can be a quantity ( for example
                # $1,500 home modification), a ratio ( for example, 20 half day visits per
                # month), or a range (2.0 to 1.8 Gy per fraction).
                StructField(
                    "quantityQuantity",
                    QuantitySchema.get_schema(recursion_depth + 1), True
                ),
                # An amount of service being requested which can be a quantity ( for example
                # $1,500 home modification), a ratio ( for example, 20 half day visits per
                # month), or a range (2.0 to 1.8 Gy per fraction).
                StructField(
                    "quantityRatio",
                    RatioSchema.get_schema(recursion_depth + 1), True
                ),
                # An amount of service being requested which can be a quantity ( for example
                # $1,500 home modification), a ratio ( for example, 20 half day visits per
                # month), or a range (2.0 to 1.8 Gy per fraction).
                StructField(
                    "quantityRange",
                    RangeSchema.get_schema(recursion_depth + 1), True
                ),
                # On whom or what the service is to be performed. This is usually a human
                # patient, but can also be requested on animals, groups of humans or animals,
                # devices such as dialysis machines, or even locations (typically for
                # environmental scans).
                StructField(
                    "subject", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # An encounter that provides additional information about the healthcare context
                # in which this request is made.
                StructField(
                    "encounter",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # The date/time at which the requested service should occur.
                StructField("occurrenceDateTime", StringType(), True),
                # The date/time at which the requested service should occur.
                StructField(
                    "occurrencePeriod",
                    PeriodSchema.get_schema(recursion_depth + 1), True
                ),
                # The date/time at which the requested service should occur.
                StructField(
                    "occurrenceTiming",
                    TimingSchema.get_schema(recursion_depth + 1), True
                ),
                # If a CodeableConcept is present, it indicates the pre-condition for performing
                # the service.  For example "pain", "on flare-up", etc.
                StructField("asNeededBoolean", BooleanType(), True),
                # If a CodeableConcept is present, it indicates the pre-condition for performing
                # the service.  For example "pain", "on flare-up", etc.
                StructField(
                    "asNeededCodeableConcept",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # When the request transitioned to being actionable.
                StructField(
                    "authoredOn",
                    dateTimeSchema.get_schema(recursion_depth + 1), True
                ),
                # The individual who initiated the request and has responsibility for its
                # activation.
                StructField(
                    "requester",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # Desired type of performer for doing the requested service.
                StructField(
                    "performerType",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The desired performer for doing the requested service.  For example, the
                # surgeon, dermatopathologist, endoscopist, etc.
                StructField(
                    "performer",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The preferred location(s) where the procedure should actually happen in coded
                # or free text form. E.g. at home or nursing day care center.
                StructField(
                    "locationCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A reference to the the preferred location(s) where the procedure should
                # actually happen. E.g. at home or nursing day care center.
                StructField(
                    "locationReference",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # An explanation or justification for why this service is being requested in
                # coded or textual form.   This is often for billing purposes.  May relate to
                # the resources referred to in `supportingInfo`.
                StructField(
                    "reasonCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Indicates another resource that provides a justification for why this service
                # is being requested.   May relate to the resources referred to in
                # `supportingInfo`.
                StructField(
                    "reasonReference",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be needed for delivering the requested service.
                StructField(
                    "insurance",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Additional clinical information about the patient or specimen that may
                # influence the services or their interpretations.     This information includes
                # diagnosis, clinical findings and other observations.  In laboratory ordering
                # these are typically referred to as "ask at order entry questions (AOEs)".
                # This includes observations explicitly requested by the producer (filler) to
                # provide context or supporting information needed to complete the order. For
                # example,  reporting the amount of inspired oxygen for blood gas measurements.
                StructField(
                    "supportingInfo",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # One or more specimens that the laboratory procedure will use.
                StructField(
                    "specimen",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Anatomic location where the procedure should be performed. This is the target
                # site.
                StructField(
                    "bodySite",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Any other notes and comments made about the service request. For example,
                # internal billing notes.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Instructions in terms that are understood by the patient or consumer.
                StructField("patientInstruction", StringType(), True),
                # Key events in the history of the request.
                StructField(
                    "relevantHistory",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
