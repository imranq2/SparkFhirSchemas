from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ImplementationGuideSchema:
    """
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used to
    gather all the parts of an implementation guide into a logical whole and to
    publish a computable definition of all the parts.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.


        resourceType: This is a ImplementationGuide resource

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

        url: An absolute URI that is used to identify this implementation guide when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this implementation
            guide is (or will be) published. This URL can be the target of a canonical
            reference. It SHALL remain the same when the implementation guide is stored on
            different servers.

        version: The identifier that is used to identify this version of the implementation
            guide when it is referenced in a specification, model, design or instance.
            This is an arbitrary value managed by the implementation guide author and is
            not expected to be globally unique. For example, it might be a timestamp (e.g.
            yyyymmdd) if a managed version is not available. There is also no expectation
            that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the implementation guide. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the implementation guide.

        status: The status of this implementation guide. Enables tracking the life-cycle of
            the content.

        experimental: A Boolean value to indicate that this implementation guide is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the implementation guide was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the implementation guide changes.

        publisher: The name of the organization or individual that published the implementation
            guide.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the implementation guide from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate
            implementation guide instances.

        jurisdiction: A legal or geographic region in which the implementation guide is intended to
            be used.

        copyright: A copyright statement relating to the implementation guide and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the implementation guide.

        packageId: The NPM package name for this Implementation Guide, used in the NPM package
            distribution, which is the primary mechanism by which FHIR based tooling
            manages IG dependencies. This value must be globally unique, and should be
            assigned with care.

        license: The license that applies to this Implementation Guide, using an SPDX license
            code, or 'not-open-source'.

        fhirVersion: The version(s) of the FHIR specification that this ImplementationGuide targets
            - e.g. describes how to use. The value of this element is the formal version
            of the specification, without the revision number, e.g.
            [publication].[major].[minor], which is 4.0.1. for this version.

        dependsOn: Another implementation guide that this implementation depends on. Typically,
            an implementation guide uses value sets, profiles etc.defined in other
            implementation guides.

        global: A set of profiles that all resources covered by this implementation guide must
            conform to.

        definition: The information needed by an IG publisher tool to publish the whole
            implementation guide.

        manifest: Information about an assembled implementation guide, created by the
            publication tooling.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.r4.simple_types.markdown import markdownSchema
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.implementationguide_dependson import ImplementationGuide_DependsOnSchema
        from spark_fhir_schemas.r4.complex_types.implementationguide_global import ImplementationGuide_GlobalSchema
        from spark_fhir_schemas.r4.complex_types.implementationguide_definition import ImplementationGuide_DefinitionSchema
        from spark_fhir_schemas.r4.complex_types.implementationguide_manifest import ImplementationGuide_ManifestSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ImplementationGuide resource
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
                # An absolute URI that is used to identify this implementation guide when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this implementation
                # guide is (or will be) published. This URL can be the target of a canonical
                # reference. It SHALL remain the same when the implementation guide is stored on
                # different servers.
                StructField(
                    "url", uriSchema.get_schema(recursion_depth + 1), True
                ),
                # The identifier that is used to identify this version of the implementation
                # guide when it is referenced in a specification, model, design or instance.
                # This is an arbitrary value managed by the implementation guide author and is
                # not expected to be globally unique. For example, it might be a timestamp (e.g.
                # yyyymmdd) if a managed version is not available. There is also no expectation
                # that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the implementation guide. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the implementation guide.
                StructField("title", StringType(), True),
                # The status of this implementation guide. Enables tracking the life-cycle of
                # the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this implementation guide is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the implementation guide was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the implementation guide changes.
                StructField(
                    "date", dateTimeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The name of the organization or individual that published the implementation
                # guide.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A free text natural language description of the implementation guide from a
                # consumer's perspective.
                StructField(
                    "description",
                    markdownSchema.get_schema(recursion_depth + 1), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate
                # implementation guide instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A legal or geographic region in which the implementation guide is intended to
                # be used.
                StructField(
                    "jurisdiction",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A copyright statement relating to the implementation guide and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the implementation guide.
                StructField(
                    "copyright",
                    markdownSchema.get_schema(recursion_depth + 1), True
                ),
                # The NPM package name for this Implementation Guide, used in the NPM package
                # distribution, which is the primary mechanism by which FHIR based tooling
                # manages IG dependencies. This value must be globally unique, and should be
                # assigned with care.
                StructField(
                    "packageId", idSchema.get_schema(recursion_depth + 1), True
                ),
                # The license that applies to this Implementation Guide, using an SPDX license
                # code, or 'not-open-source'.
                StructField("license", StringType(), True),
                # The version(s) of the FHIR specification that this ImplementationGuide targets
                # - e.g. describes how to use. The value of this element is the formal version
                # of the specification, without the revision number, e.g.
                # [publication].[major].[minor], which is 4.0.1. for this version.
                # Another implementation guide that this implementation depends on. Typically,
                # an implementation guide uses value sets, profiles etc.defined in other
                # implementation guides.
                StructField(
                    "dependsOn",
                    ArrayType(
                        ImplementationGuide_DependsOnSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A set of profiles that all resources covered by this implementation guide must
                # conform to.
                StructField(
                    "global",
                    ArrayType(
                        ImplementationGuide_GlobalSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The information needed by an IG publisher tool to publish the whole
                # implementation guide.
                StructField(
                    "definition",
                    ImplementationGuide_DefinitionSchema.
                    get_schema(recursion_depth + 1), True
                ),
                # Information about an assembled implementation guide, created by the
                # publication tooling.
                StructField(
                    "manifest",
                    ImplementationGuide_ManifestSchema.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
