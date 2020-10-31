from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An order or request for both supply of the medication and the instructions for
        administration of the medication to a patient. The resource is called
        "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
        to generalize the use across inpatient and outpatient settings, including care
        plans, etc., and to harmonize with workflow patterns.


        resourceType: This is a MedicationRequest resource

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

        identifier: Identifiers associated with this medication request that are defined by
            business processes and/or used to refer to it when a direct URL reference to
            the resource itself is not appropriate. They are business identifiers assigned
            to this resource by the performer or other systems and remain constant as the
            resource is updated and propagates from server to server.

        status: A code specifying the current state of the order.  Generally, this will be
            active or completed state.

        statusReason: Captures the reason for the current state of the MedicationRequest.

        intent: Whether the request is a proposal, plan, or an original order.

        category: Indicates the type of medication request (for example, where the medication is
            expected to be consumed or administered (i.e. inpatient or outpatient)).

        priority: Indicates how quickly the Medication Request should be addressed with respect
            to other requests.

        doNotPerform: If true indicates that the provider is asking for the medication request not
            to occur.

        reportedBoolean: Indicates if this record was captured as a secondary 'reported' record rather
            than as an original primary source-of-truth record.  It may also indicate the
            source of the report.

        reportedReference: Indicates if this record was captured as a secondary 'reported' record rather
            than as an original primary source-of-truth record.  It may also indicate the
            source of the report.

        medicationCodeableConcept: Identifies the medication being requested. This is a link to a resource that
            represents the medication which may be the details of the medication or simply
            an attribute carrying a code that identifies the medication from a known list
            of medications.

        medicationReference: Identifies the medication being requested. This is a link to a resource that
            represents the medication which may be the details of the medication or simply
            an attribute carrying a code that identifies the medication from a known list
            of medications.

        subject: A link to a resource representing the person or set of individuals to whom the
            medication will be given.

        encounter: The Encounter during which this [x] was created or to which the creation of
            this record is tightly associated.

        supportingInformation: Include additional information (for example, patient height and weight) that
            supports the ordering of the medication.

        authoredOn: The date (and perhaps time) when the prescription was initially written or
            authored on.

        requester: The individual, organization, or device that initiated the request and has
            responsibility for its activation.

        performer: The specified desired performer of the medication treatment (e.g. the
            performer of the medication administration).

        performerType: Indicates the type of performer of the administration of the medication.

        recorder: The person who entered the order on behalf of another individual for example
            in the case of a verbal or a telephone order.

        reasonCode: The reason or the indication for ordering or not ordering the medication.

        reasonReference: Condition or observation that supports why the medication was ordered.

        instantiatesCanonical: The URL pointing to a protocol, guideline, orderset, or other definition that
            is adhered to in whole or in part by this MedicationRequest.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            MedicationRequest.

        basedOn: A plan or request that is fulfilled in whole or in part by this medication
            request.

        groupIdentifier: A shared identifier common to all requests that were authorized more or less
            simultaneously by a single author, representing the identifier of the
            requisition or prescription.

        courseOfTherapyType: The description of the overall patte3rn of the administration of the
            medication to the patient.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be required for delivering the requested service.

        note: Extra information about the prescription that could not be conveyed by the
            other attributes.

        dosageInstruction: Indicates how the medication is to be used by the patient.

        dispenseRequest: Indicates the specific details for the dispense or medication supply part of a
            medication request (also known as a Medication Prescription or Medication
            Order).  Note that this information is not always sent with the order.  There
            may be in some settings (e.g. hospitals) institutional or system support for
            completing the dispense details in the pharmacy department.

        substitution: Indicates whether or not substitution can or should be part of the dispense.
            In some cases, substitution must happen, in other cases substitution must not
            happen. This block explains the prescriber's intent. If nothing is specified
            substitution may be done.

        priorPrescription: A link to a resource representing an earlier order related order or
            prescription.

        detectedIssue: Indicates an actual or potential clinical issue with or between one or more
            active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
            duplicate therapy, dosage alert etc.

        eventHistory: Links to Provenance records for past versions of this resource or fulfilling
            request or event resources that identify key state transitions or updates that
            are likely to be relevant to a user looking at the current version of the
            resource.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.dosage import Dosage
        from spark_fhir_schemas.r4.complex_types.medicationrequest_dispenserequest import MedicationRequest_DispenseRequest
        from spark_fhir_schemas.r4.complex_types.medicationrequest_substitution import MedicationRequest_Substitution
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MedicationRequest resource
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
                # Identifiers associated with this medication request that are defined by
                # business processes and/or used to refer to it when a direct URL reference to
                # the resource itself is not appropriate. They are business identifiers assigned
                # to this resource by the performer or other systems and remain constant as the
                # resource is updated and propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # A code specifying the current state of the order.  Generally, this will be
                # active or completed state.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Captures the reason for the current state of the MedicationRequest.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Whether the request is a proposal, plan, or an original order.
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates the type of medication request (for example, where the medication is
                # expected to be consumed or administered (i.e. inpatient or outpatient)).
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates how quickly the Medication Request should be addressed with respect
                # to other requests.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # If true indicates that the provider is asking for the medication request not
                # to occur.
                StructField("doNotPerform", BooleanType(), True),
                # Indicates if this record was captured as a secondary 'reported' record rather
                # than as an original primary source-of-truth record.  It may also indicate the
                # source of the report.
                StructField("reportedBoolean", BooleanType(), True),
                # Indicates if this record was captured as a secondary 'reported' record rather
                # than as an original primary source-of-truth record.  It may also indicate the
                # source of the report.
                StructField(
                    "reportedReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies the medication being requested. This is a link to a resource that
                # represents the medication which may be the details of the medication or simply
                # an attribute carrying a code that identifies the medication from a known list
                # of medications.
                StructField(
                    "medicationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identifies the medication being requested. This is a link to a resource that
                # represents the medication which may be the details of the medication or simply
                # an attribute carrying a code that identifies the medication from a known list
                # of medications.
                StructField(
                    "medicationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A link to a resource representing the person or set of individuals to whom the
                # medication will be given.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Encounter during which this [x] was created or to which the creation of
                # this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Include additional information (for example, patient height and weight) that
                # supports the ordering of the medication.
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The date (and perhaps time) when the prescription was initially written or
                # authored on.
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The individual, organization, or device that initiated the request and has
                # responsibility for its activation.
                StructField(
                    "requester", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The specified desired performer of the medication treatment (e.g. the
                # performer of the medication administration).
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the type of performer of the administration of the medication.
                StructField(
                    "performerType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The person who entered the order on behalf of another individual for example
                # in the case of a verbal or a telephone order.
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                # The reason or the indication for ordering or not ordering the medication.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Condition or observation that supports why the medication was ordered.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a protocol, guideline, orderset, or other definition that
                # is adhered to in whole or in part by this MedicationRequest.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # MedicationRequest.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # A plan or request that is fulfilled in whole or in part by this medication
                # request.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A shared identifier common to all requests that were authorized more or less
                # simultaneously by a single author, representing the identifier of the
                # requisition or prescription.
                StructField(
                    "groupIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The description of the overall patte3rn of the administration of the
                # medication to the patient.
                StructField(
                    "courseOfTherapyType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be required for delivering the requested service.
                StructField(
                    "insurance",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Extra information about the prescription that could not be conveyed by the
                # other attributes.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Indicates how the medication is to be used by the patient.
                StructField(
                    "dosageInstruction",
                    ArrayType(Dosage.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the specific details for the dispense or medication supply part of a
                # medication request (also known as a Medication Prescription or Medication
                # Order).  Note that this information is not always sent with the order.  There
                # may be in some settings (e.g. hospitals) institutional or system support for
                # completing the dispense details in the pharmacy department.
                StructField(
                    "dispenseRequest",
                    MedicationRequest_DispenseRequest.
                    get_schema(recursion_depth + 1), True
                ),
                # Indicates whether or not substitution can or should be part of the dispense.
                # In some cases, substitution must happen, in other cases substitution must not
                # happen. This block explains the prescriber's intent. If nothing is specified
                # substitution may be done.
                StructField(
                    "substitution",
                    MedicationRequest_Substitution.
                    get_schema(recursion_depth + 1), True
                ),
                # A link to a resource representing an earlier order related order or
                # prescription.
                StructField(
                    "priorPrescription",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Indicates an actual or potential clinical issue with or between one or more
                # active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
                # duplicate therapy, dosage alert etc.
                StructField(
                    "detectedIssue",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Links to Provenance records for past versions of this resource or fulfilling
                # request or event resources that identify key state transitions or updates that
                # are likely to be relevant to a user looking at the current version of the
                # resource.
                StructField(
                    "eventHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
