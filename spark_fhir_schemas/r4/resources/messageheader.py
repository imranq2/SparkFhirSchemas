from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MessageHeader:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The header for a message exchange that is either requesting or responding to
        an action.  The reference(s) that are the subject of the action as well as
        other information related to the action are typically transmitted in a bundle
        in which the MessageHeader resource instance is the first resource in the
        bundle.


        resourceType: This is a MessageHeader resource

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

        eventCoding: Code that identifies the event this message represents and connects it with
            its definition. Events defined as part of the FHIR specification have the
            system value "http://terminology.hl7.org/CodeSystem/message-events".
            Alternatively uri to the EventDefinition.

        eventUri: Code that identifies the event this message represents and connects it with
            its definition. Events defined as part of the FHIR specification have the
            system value "http://terminology.hl7.org/CodeSystem/message-events".
            Alternatively uri to the EventDefinition.

        destination: The destination application which the message is intended for.

        sender: Identifies the sending system to allow the use of a trust relationship.

        enterer: The person or device that performed the data entry leading to this message.
            When there is more than one candidate, pick the most proximal to the message.
            Can provide other enterers in extensions.

        author: The logical author of the message - the person or device that decided the
            described event should happen. When there is more than one candidate, pick the
            most proximal to the MessageHeader. Can provide other authors in extensions.

        source: The source application from which this message originated.

        responsible: The person or organization that accepts overall responsibility for the
            contents of the message. The implication is that the message event happened
            under the policies of the responsible party.

        reason: Coded indication of the cause for the event - indicates  a reason for the
            occurrence of the event that is a focus of this message.

        response: Information about the message that this message is a response to.  Only
            present if this message is a response.

        focus: The actual data of the message - a reference to the root/focus class of the
            event.

        definition: Permanent link to the MessageDefinition for this message.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.messageheader_destination import MessageHeader_Destination
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.messageheader_source import MessageHeader_Source
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.messageheader_response import MessageHeader_Response
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MessageHeader resource
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
                # Code that identifies the event this message represents and connects it with
                # its definition. Events defined as part of the FHIR specification have the
                # system value "http://terminology.hl7.org/CodeSystem/message-events".
                # Alternatively uri to the EventDefinition.
                StructField(
                    "eventCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # Code that identifies the event this message represents and connects it with
                # its definition. Events defined as part of the FHIR specification have the
                # system value "http://terminology.hl7.org/CodeSystem/message-events".
                # Alternatively uri to the EventDefinition.
                StructField("eventUri", StringType(), True),
                # The destination application which the message is intended for.
                StructField(
                    "destination",
                    ArrayType(
                        MessageHeader_Destination.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies the sending system to allow the use of a trust relationship.
                StructField(
                    "sender", Reference.get_schema(recursion_depth + 1), True
                ),
                # The person or device that performed the data entry leading to this message.
                # When there is more than one candidate, pick the most proximal to the message.
                # Can provide other enterers in extensions.
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                # The logical author of the message - the person or device that decided the
                # described event should happen. When there is more than one candidate, pick the
                # most proximal to the MessageHeader. Can provide other authors in extensions.
                StructField(
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                # The source application from which this message originated.
                StructField(
                    "source",
                    MessageHeader_Source.get_schema(recursion_depth + 1), True
                ),
                # The person or organization that accepts overall responsibility for the
                # contents of the message. The implication is that the message event happened
                # under the policies of the responsible party.
                StructField(
                    "responsible", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Coded indication of the cause for the event - indicates  a reason for the
                # occurrence of the event that is a focus of this message.
                StructField(
                    "reason", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Information about the message that this message is a response to.  Only
                # present if this message is a response.
                StructField(
                    "response",
                    MessageHeader_Response.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual data of the message - a reference to the root/focus class of the
                # event.
                StructField(
                    "focus",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Permanent link to the MessageDefinition for this message.
                StructField(
                    "definition", canonical.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
