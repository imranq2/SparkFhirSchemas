from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CommunicationRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A request to convey information; e.g. the CDS system proposes that an alert be
        sent to a responsible provider, the CDS system proposes that the public health
        agency be notified about a reportable condition.


        resourceType: This is a CommunicationRequest resource

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

        identifier: Business identifiers assigned to this communication request by the performer
            or other systems which remain constant as the resource is updated and
            propagates from server to server.

        basedOn: A plan or proposal that is fulfilled in whole or in part by this request.

        replaces: Completed or terminated request(s) whose function is taken by this new
            request.

        groupIdentifier: A shared identifier common to all requests that were authorized more or less
            simultaneously by a single author, representing the identifier of the
            requisition, prescription or similar form.

        status: The status of the proposal or order.

        statusReason: Captures the reason for the current state of the CommunicationRequest.

        category: The type of message to be sent such as alert, notification, reminder,
            instruction, etc.

        priority: Characterizes how quickly the proposed act must be initiated. Includes
            concepts such as stat, urgent, routine.

        doNotPerform: If true indicates that the CommunicationRequest is asking for the specified
            action to *not* occur.

        medium: A channel that was used for this communication (e.g. email, fax).

        subject: The patient or group that is the focus of this communication request.

        about: Other resources that pertain to this communication request and to which this
            communication request should be associated.

        encounter: The Encounter during which this CommunicationRequest was created or to which
            the creation of this record is tightly associated.

        payload: Text, attachment(s), or resource(s) to be communicated to the recipient.

        occurrenceDateTime: The time when this communication is to occur.

        occurrencePeriod: The time when this communication is to occur.

        authoredOn: For draft requests, indicates the date of initial creation.  For requests with
            other statuses, indicates the date of activation.

        requester: The device, individual, or organization who initiated the request and has
            responsibility for its activation.

        recipient: The entity (e.g. person, organization, clinical information system, device,
            group, or care team) which is the intended target of the communication.

        sender: The entity (e.g. person, organization, clinical information system, or device)
            which is to be the source of the communication.

        reasonCode: Describes why the request is being made in coded or textual form.

        reasonReference: Indicates another resource whose existence justifies this request.

        note: Comments made about the request by the requester, sender, recipient, subject
            or other participants.

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
        from spark_fhir_schemas.r4.complex_types.communicationrequest_payload import CommunicationRequest_Payload
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a CommunicationRequest resource
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
                # Business identifiers assigned to this communication request by the performer
                # or other systems which remain constant as the resource is updated and
                # propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # A plan or proposal that is fulfilled in whole or in part by this request.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Completed or terminated request(s) whose function is taken by this new
                # request.
                StructField(
                    "replaces",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A shared identifier common to all requests that were authorized more or less
                # simultaneously by a single author, representing the identifier of the
                # requisition, prescription or similar form.
                StructField(
                    "groupIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The status of the proposal or order.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Captures the reason for the current state of the CommunicationRequest.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The type of message to be sent such as alert, notification, reminder,
                # instruction, etc.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Characterizes how quickly the proposed act must be initiated. Includes
                # concepts such as stat, urgent, routine.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # If true indicates that the CommunicationRequest is asking for the specified
                # action to *not* occur.
                StructField("doNotPerform", BooleanType(), True),
                # A channel that was used for this communication (e.g. email, fax).
                StructField(
                    "medium",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The patient or group that is the focus of this communication request.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # Other resources that pertain to this communication request and to which this
                # communication request should be associated.
                StructField(
                    "about",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The Encounter during which this CommunicationRequest was created or to which
                # the creation of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Text, attachment(s), or resource(s) to be communicated to the recipient.
                StructField(
                    "payload",
                    ArrayType(
                        CommunicationRequest_Payload.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The time when this communication is to occur.
                StructField("occurrenceDateTime", StringType(), True),
                # The time when this communication is to occur.
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # For draft requests, indicates the date of initial creation.  For requests with
                # other statuses, indicates the date of activation.
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The device, individual, or organization who initiated the request and has
                # responsibility for its activation.
                StructField(
                    "requester", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The entity (e.g. person, organization, clinical information system, device,
                # group, or care team) which is the intended target of the communication.
                StructField(
                    "recipient",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The entity (e.g. person, organization, clinical information system, or device)
                # which is to be the source of the communication.
                StructField(
                    "sender", Reference.get_schema(recursion_depth + 1), True
                ),
                # Describes why the request is being made in coded or textual form.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource whose existence justifies this request.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Comments made about the request by the requester, sender, recipient, subject
                # or other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
