from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DeviceRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Represents a request for a patient to employ a medical device. The device may
        be an implantable device, or an external assistive device, such as a walker.


        resourceType: This is a DeviceRequest resource

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

        identifier: Identifiers assigned to this order by the orderer or by the receiver.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this DeviceRequest.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this DeviceRequest.

        basedOn: Plan/proposal/order fulfilled by this request.

        priorRequest: The request takes the place of the referenced completed or terminated
            request(s).

        groupIdentifier: Composite request this is part of.

        status: The status of the request.

        intent: Whether the request is a proposal, plan, an original order or a reflex order.

        priority: Indicates how quickly the {{title}} should be addressed with respect to other
            requests.

        codeReference: The details of the device to be used.

        codeCodeableConcept: The details of the device to be used.

        parameter: Specific parameters for the ordered item.  For example, the prism value for
            lenses.

        subject: The patient who will use the device.

        encounter: An encounter that provides additional context in which this request is made.

        occurrenceDateTime: The timing schedule for the use of the device. The Schedule data type allows
            many different expressions, for example. "Every 8 hours"; "Three times a day";
            "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17
            Oct 2013 and 1 Nov 2013".

        occurrencePeriod: The timing schedule for the use of the device. The Schedule data type allows
            many different expressions, for example. "Every 8 hours"; "Three times a day";
            "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17
            Oct 2013 and 1 Nov 2013".

        occurrenceTiming: The timing schedule for the use of the device. The Schedule data type allows
            many different expressions, for example. "Every 8 hours"; "Three times a day";
            "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17
            Oct 2013 and 1 Nov 2013".

        authoredOn: When the request transitioned to being actionable.

        requester: The individual who initiated the request and has responsibility for its
            activation.

        performerType: Desired type of performer for doing the diagnostic testing.

        performer: The desired performer for doing the diagnostic testing.

        reasonCode: Reason or justification for the use of this device.

        reasonReference: Reason or justification for the use of this device.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be required for delivering the requested service.

        supportingInfo: Additional clinical information about the patient that may influence the
            request fulfilment.  For example, this may include where on the subject's body
            the device will be used (i.e. the target site).

        note: Details about this request that were not represented at all or sufficiently in
            one of the attributes provided in a class. These may include for example a
            comment, an instruction, or a note associated with the statement.

        relevantHistory: Key events in the history of the request.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.devicerequest_parameter import DeviceRequest_Parameter
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a DeviceRequest resource
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
                # Identifiers assigned to this order by the orderer or by the receiver.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this DeviceRequest.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this DeviceRequest.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # Plan/proposal/order fulfilled by this request.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The request takes the place of the referenced completed or terminated
                # request(s).
                StructField(
                    "priorRequest",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Composite request this is part of.
                StructField(
                    "groupIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The status of the request.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Whether the request is a proposal, plan, an original order or a reflex order.
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates how quickly the {{title}} should be addressed with respect to other
                # requests.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # The details of the device to be used.
                StructField(
                    "codeReference", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The details of the device to be used.
                StructField(
                    "codeCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Specific parameters for the ordered item.  For example, the prism value for
                # lenses.
                StructField(
                    "parameter",
                    ArrayType(
                        DeviceRequest_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The patient who will use the device.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # An encounter that provides additional context in which this request is made.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The timing schedule for the use of the device. The Schedule data type allows
                # many different expressions, for example. "Every 8 hours"; "Three times a day";
                # "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17
                # Oct 2013 and 1 Nov 2013".
                StructField("occurrenceDateTime", StringType(), True),
                # The timing schedule for the use of the device. The Schedule data type allows
                # many different expressions, for example. "Every 8 hours"; "Three times a day";
                # "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17
                # Oct 2013 and 1 Nov 2013".
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The timing schedule for the use of the device. The Schedule data type allows
                # many different expressions, for example. "Every 8 hours"; "Three times a day";
                # "1/2 an hour before breakfast for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17
                # Oct 2013 and 1 Nov 2013".
                StructField(
                    "occurrenceTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # When the request transitioned to being actionable.
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The individual who initiated the request and has responsibility for its
                # activation.
                StructField(
                    "requester", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Desired type of performer for doing the diagnostic testing.
                StructField(
                    "performerType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The desired performer for doing the diagnostic testing.
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Reason or justification for the use of this device.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Reason or justification for the use of this device.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be required for delivering the requested service.
                StructField(
                    "insurance",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Additional clinical information about the patient that may influence the
                # request fulfilment.  For example, this may include where on the subject's body
                # the device will be used (i.e. the target site).
                StructField(
                    "supportingInfo",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Details about this request that were not represented at all or sufficiently in
                # one of the attributes provided in a class. These may include for example a
                # comment, an instruction, or a note associated with the statement.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Key events in the history of the request.
                StructField(
                    "relevantHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
