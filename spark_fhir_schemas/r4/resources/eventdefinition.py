from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class EventDefinitionSchema:
    """
    The EventDefinition resource provides a reusable description of when a
    particular event can occur.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The EventDefinition resource provides a reusable description of when a
        particular event can occur.


        resourceType: This is a EventDefinition resource

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

        url: An absolute URI that is used to identify this event definition when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this event definition
            is (or will be) published. This URL can be the target of a canonical
            reference. It SHALL remain the same when the event definition is stored on
            different servers.

        identifier: A formal identifier that is used to identify this event definition when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the event definition
            when it is referenced in a specification, model, design or instance. This is
            an arbitrary value managed by the event definition author and is not expected
            to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
            a managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the event definition. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        title: A short, descriptive, user-friendly title for the event definition.

        subtitle: An explanatory or alternate title for the event definition giving additional
            information about its content.

        status: The status of this event definition. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this event definition is authored for testing
            purposes (or education/evaluation/marketing) and is not intended to be used
            for genuine usage.

        subjectCodeableConcept: A code or group definition that describes the intended subject of the event
            definition.

        subjectReference: A code or group definition that describes the intended subject of the event
            definition.

        date: The date  (and optionally time) when the event definition was published. The
            date must change when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the event definition changes.

        publisher: The name of the organization or individual that published the event
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the event definition from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate event
            definition instances.

        jurisdiction: A legal or geographic region in which the event definition is intended to be
            used.

        purpose: Explanation of why this event definition is needed and why it has been
            designed as it has.

        usage: A detailed description of how the event definition is used from a clinical
            perspective.

        copyright: A copyright statement relating to the event definition and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the event definition.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the event definition content was or is planned to be
            in active use.

        topic: Descriptive topics related to the module. Topics provide a high-level
            categorization of the module that can be useful for filtering and searching.

        author: An individiual or organization primarily involved in the creation and
            maintenance of the content.

        editor: An individual or organization primarily responsible for internal coherence of
            the content.

        reviewer: An individual or organization primarily responsible for review of some aspect
            of the content.

        endorser: An individual or organization responsible for officially endorsing the content
            for use in some setting.

        relatedArtifact: Related resources such as additional documentation, justification, or
            bibliographic references.

        trigger: The trigger element defines when the event occurs. If more than one trigger
            condition is specified, the event fires whenever any one of the trigger
            conditions is met.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.r4.simple_types.markdown import markdownSchema
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifactSchema
        from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinitionSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a EventDefinition resource
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
                # An absolute URI that is used to identify this event definition when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this event definition
                # is (or will be) published. This URL can be the target of a canonical
                # reference. It SHALL remain the same when the event definition is stored on
                # different servers.
                StructField(
                    "url", uriSchema.get_schema(recursion_depth + 1), True
                ),
                # A formal identifier that is used to identify this event definition when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The identifier that is used to identify this version of the event definition
                # when it is referenced in a specification, model, design or instance. This is
                # an arbitrary value managed by the event definition author and is not expected
                # to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
                # a managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the event definition. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the event definition.
                StructField("title", StringType(), True),
                # An explanatory or alternate title for the event definition giving additional
                # information about its content.
                StructField("subtitle", StringType(), True),
                # The status of this event definition. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this event definition is authored for testing
                # purposes (or education/evaluation/marketing) and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # A code or group definition that describes the intended subject of the event
                # definition.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # A code or group definition that describes the intended subject of the event
                # definition.
                StructField(
                    "subjectReference",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # The date  (and optionally time) when the event definition was published. The
                # date must change when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the event definition changes.
                StructField(
                    "date", dateTimeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The name of the organization or individual that published the event
                # definition.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A free text natural language description of the event definition from a
                # consumer's perspective.
                StructField(
                    "description",
                    markdownSchema.get_schema(recursion_depth + 1), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate event
                # definition instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A legal or geographic region in which the event definition is intended to be
                # used.
                StructField(
                    "jurisdiction",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Explanation of why this event definition is needed and why it has been
                # designed as it has.
                StructField(
                    "purpose", markdownSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A detailed description of how the event definition is used from a clinical
                # perspective.
                StructField("usage", StringType(), True),
                # A copyright statement relating to the event definition and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the event definition.
                StructField(
                    "copyright",
                    markdownSchema.get_schema(recursion_depth + 1), True
                ),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", DateType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval but does not change the original approval date.
                StructField("lastReviewDate", DateType(), True),
                # The period during which the event definition content was or is planned to be
                # in active use.
                StructField(
                    "effectivePeriod",
                    PeriodSchema.get_schema(recursion_depth + 1), True
                ),
                # Descriptive topics related to the module. Topics provide a high-level
                # categorization of the module that can be useful for filtering and searching.
                StructField(
                    "topic",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An individiual or organization primarily involved in the creation and
                # maintenance of the content.
                StructField(
                    "author",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An individual or organization primarily responsible for internal coherence of
                # the content.
                StructField(
                    "editor",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An individual or organization primarily responsible for review of some aspect
                # of the content.
                StructField(
                    "reviewer",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An individual or organization responsible for officially endorsing the content
                # for use in some setting.
                StructField(
                    "endorser",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Related resources such as additional documentation, justification, or
                # bibliographic references.
                StructField(
                    "relatedArtifact",
                    ArrayType(
                        RelatedArtifactSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The trigger element defines when the event occurs. If more than one trigger
                # condition is specified, the event fires whenever any one of the trigger
                # conditions is met.
                StructField(
                    "trigger",
                    ArrayType(
                        TriggerDefinitionSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
