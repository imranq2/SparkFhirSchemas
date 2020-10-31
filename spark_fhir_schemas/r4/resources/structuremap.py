from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class StructureMapSchema:
    """
    A Map of relationships between 2 structures that can be used to transform
    data.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A Map of relationships between 2 structures that can be used to transform
        data.


        resourceType: This is a StructureMap resource

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

        url: An absolute URI that is used to identify this structure map when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this structure map is
            (or will be) published. This URL can be the target of a canonical reference.
            It SHALL remain the same when the structure map is stored on different
            servers.

        identifier: A formal identifier that is used to identify this structure map when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the structure map when
            it is referenced in a specification, model, design or instance. This is an
            arbitrary value managed by the structure map author and is not expected to be
            globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
            managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the structure map. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        title: A short, descriptive, user-friendly title for the structure map.

        status: The status of this structure map. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this structure map is authored for testing
            purposes (or education/evaluation/marketing) and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the structure map was published. The date
            must change when the business version changes and it must change if the status
            code changes. In addition, it should change when the substantive content of
            the structure map changes.

        publisher: The name of the organization or individual that published the structure map.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the structure map from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate structure
            map instances.

        jurisdiction: A legal or geographic region in which the structure map is intended to be
            used.

        purpose: Explanation of why this structure map is needed and why it has been designed
            as it has.

        copyright: A copyright statement relating to the structure map and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the structure map.

        structure: A structure definition used by this map. The structure definition may describe
            instances that are converted, or the instances that are produced.

        import: Other maps used by this map (canonical URLs).

        group: Organizes the mapping into manageable chunks for human review/ease of
            maintenance.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.r4.simple_types.markdown import markdownSchema
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.structuremap_structure import StructureMap_StructureSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.structuremap_group import StructureMap_GroupSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                # This is a StructureMap resource
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
                # An absolute URI that is used to identify this structure map when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this structure map is
                # (or will be) published. This URL can be the target of a canonical reference.
                # It SHALL remain the same when the structure map is stored on different
                # servers.
                StructField(
                    "url", uriSchema.get_schema(recursion_depth + 1), True
                ),
                # A formal identifier that is used to identify this structure map when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The identifier that is used to identify this version of the structure map when
                # it is referenced in a specification, model, design or instance. This is an
                # arbitrary value managed by the structure map author and is not expected to be
                # globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
                # managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the structure map. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the structure map.
                StructField("title", StringType(), True),
                # The status of this structure map. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this structure map is authored for testing
                # purposes (or education/evaluation/marketing) and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the structure map was published. The date
                # must change when the business version changes and it must change if the status
                # code changes. In addition, it should change when the substantive content of
                # the structure map changes.
                StructField(
                    "date", dateTimeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The name of the organization or individual that published the structure map.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A free text natural language description of the structure map from a
                # consumer's perspective.
                StructField(
                    "description",
                    markdownSchema.get_schema(recursion_depth + 1), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate structure
                # map instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A legal or geographic region in which the structure map is intended to be
                # used.
                StructField(
                    "jurisdiction",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Explanation of why this structure map is needed and why it has been designed
                # as it has.
                StructField(
                    "purpose", markdownSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A copyright statement relating to the structure map and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the structure map.
                StructField(
                    "copyright",
                    markdownSchema.get_schema(recursion_depth + 1), True
                ),
                # A structure definition used by this map. The structure definition may describe
                # instances that are converted, or the instances that are produced.
                StructField(
                    "structure",
                    ArrayType(
                        StructureMap_StructureSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Other maps used by this map (canonical URLs).
                StructField(
                    "import",
                    ArrayType(canonicalSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Organizes the mapping into manageable chunks for human review/ease of
                # maintenance.
                StructField(
                    "group",
                    ArrayType(
                        StructureMap_GroupSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
