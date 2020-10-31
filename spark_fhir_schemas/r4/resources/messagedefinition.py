from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MessageDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Defines the characteristics of a message that can be shared between systems,
        including the type of event that initiates the message, the content to be
        transmitted and what response(s), if any, are permitted.


        resourceType: This is a MessageDefinition resource

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

        url: The business identifier that is used to reference the MessageDefinition and
            *is* expected to be consistent from server to server.

        identifier: A formal identifier that is used to identify this message definition when it
            is represented in other formats, or referenced in a specification, model,
            design or an instance.

        version: The identifier that is used to identify this version of the message definition
            when it is referenced in a specification, model, design or instance. This is
            an arbitrary value managed by the message definition author and is not
            expected to be globally unique. For example, it might be a timestamp (e.g.
            yyyymmdd) if a managed version is not available. There is also no expectation
            that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the message definition. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the message definition.

        replaces: A MessageDefinition that is superseded by this definition.

        status: The status of this message definition. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this message definition is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the message definition was published. The
            date must change when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the message definition changes.

        publisher: The name of the organization or individual that published the message
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the message definition from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate message
            definition instances.

        jurisdiction: A legal or geographic region in which the message definition is intended to be
            used.

        purpose: Explanation of why this message definition is needed and why it has been
            designed as it has.

        copyright: A copyright statement relating to the message definition and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the message definition.

        base: The MessageDefinition that is the basis for the contents of this resource.

        parent: Identifies a protocol or workflow that this MessageDefinition represents a
            step in.

        eventCoding: Event code or link to the EventDefinition.

        eventUri: Event code or link to the EventDefinition.

        category: The impact of the content of the message.

        focus: Identifies the resource (or resources) that are being addressed by the event.
            For example, the Encounter for an admit message or two Account records for a
            merge.

        responseRequired: Declare at a message definition level whether a response is required or only
            upon error or success, or never.

        allowedResponse: Indicates what types of messages may be sent as an application-level response
            to this message.

        graph: Canonical reference to a GraphDefinition. If a URL is provided, it is the
            canonical reference to a [[[GraphDefinition]]] that it controls what resources
            are to be added to the bundle when building the document. The GraphDefinition
            can also specify profiles that apply to the various resources.

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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.messagedefinition_focus import MessageDefinition_Focus
        from spark_fhir_schemas.r4.complex_types.messagedefinition_allowedresponse import MessageDefinition_AllowedResponse
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MessageDefinition resource
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
                # The business identifier that is used to reference the MessageDefinition and
                # *is* expected to be consistent from server to server.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # A formal identifier that is used to identify this message definition when it
                # is represented in other formats, or referenced in a specification, model,
                # design or an instance.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The identifier that is used to identify this version of the message definition
                # when it is referenced in a specification, model, design or instance. This is
                # an arbitrary value managed by the message definition author and is not
                # expected to be globally unique. For example, it might be a timestamp (e.g.
                # yyyymmdd) if a managed version is not available. There is also no expectation
                # that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the message definition. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the message definition.
                StructField("title", StringType(), True),
                # A MessageDefinition that is superseded by this definition.
                StructField(
                    "replaces",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The status of this message definition. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this message definition is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the message definition was published. The
                # date must change when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the message definition changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the message
                # definition.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the message definition from a
                # consumer's perspective.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate message
                # definition instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the message definition is intended to be
                # used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Explanation of why this message definition is needed and why it has been
                # designed as it has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # A copyright statement relating to the message definition and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the message definition.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # The MessageDefinition that is the basis for the contents of this resource.
                StructField(
                    "base", canonical.get_schema(recursion_depth + 1), True
                ),
                # Identifies a protocol or workflow that this MessageDefinition represents a
                # step in.
                StructField(
                    "parent",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # Event code or link to the EventDefinition.
                StructField(
                    "eventCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # Event code or link to the EventDefinition.
                StructField("eventUri", StringType(), True),
                # The impact of the content of the message.
                StructField("category", StringType(), True),
                # Identifies the resource (or resources) that are being addressed by the event.
                # For example, the Encounter for an admit message or two Account records for a
                # merge.
                StructField(
                    "focus",
                    ArrayType(
                        MessageDefinition_Focus.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Declare at a message definition level whether a response is required or only
                # upon error or success, or never.
                StructField("responseRequired", StringType(), True),
                # Indicates what types of messages may be sent as an application-level response
                # to this message.
                StructField(
                    "allowedResponse",
                    ArrayType(
                        MessageDefinition_AllowedResponse.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Canonical reference to a GraphDefinition. If a URL is provided, it is the
                # canonical reference to a [[[GraphDefinition]]] that it controls what resources
                # are to be added to the bundle when building the document. The GraphDefinition
                # can also specify profiles that apply to the various resources.
                StructField(
                    "graph",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
