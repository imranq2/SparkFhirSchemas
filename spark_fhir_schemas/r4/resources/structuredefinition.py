from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class StructureDefinitionSchema:
    """
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A definition of a FHIR structure. This resource is used to describe the
        underlying resources, data types defined in FHIR, and also for describing
        extensions and constraints on resources and data types.


        resourceType: This is a StructureDefinition resource

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

        url: An absolute URI that is used to identify this structure definition when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this structure
            definition is (or will be) published. This URL can be the target of a
            canonical reference. It SHALL remain the same when the structure definition is
            stored on different servers.

        identifier: A formal identifier that is used to identify this structure definition when it
            is represented in other formats, or referenced in a specification, model,
            design or an instance.

        version: The identifier that is used to identify this version of the structure
            definition when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the structure definition
            author and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
            no expectation that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the structure definition. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the structure definition.

        status: The status of this structure definition. Enables tracking the life-cycle of
            the content.

        experimental: A Boolean value to indicate that this structure definition is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the structure definition was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the structure definition changes.

        publisher: The name of the organization or individual that published the structure
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the structure definition from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate structure
            definition instances.

        jurisdiction: A legal or geographic region in which the structure definition is intended to
            be used.

        purpose: Explanation of why this structure definition is needed and why it has been
            designed as it has.

        copyright: A copyright statement relating to the structure definition and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the structure definition.

        keyword: A set of key words or terms from external terminologies that may be used to
            assist with indexing and searching of templates nby describing the use of this
            structure definition, or the content it describes.

        fhirVersion: The version of the FHIR specification on which this StructureDefinition is
            based - this is the formal version of the specification, without the revision
            number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.

        mapping: An external specification that the content is mapped to.

        kind: Defines the kind of structure that this definition is describing.

        abstract: Whether structure this definition describes is abstract or not  - that is,
            whether the structure is not intended to be instantiated. For Resources and
            Data types, abstract types will never be exchanged  between systems.

        context: Identifies the types of resource or data type elements to which the extension
            can be applied.

        contextInvariant: A set of rules as FHIRPath Invariants about when the extension can be used
            (e.g. co-occurrence variants for the extension). All the rules must be true.

        type: The type this structure describes. If the derivation kind is 'specialization'
            then this is the master definition for a type, and there is always one of
            these (a data type, an extension, a resource, including abstract ones).
            Otherwise the structure definition is a constraint on the stated type (and in
            this case, the type cannot be an abstract type).  References are URLs that are
            relative to http://hl7.org/fhir/StructureDefinition e.g. "string" is a
            reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are
            only allowed in logical models.

        baseDefinition: An absolute URI that is the base structure from which this type is derived,
            either by specialization or constraint.

        derivation: How the type relates to the baseDefinition.

        snapshot: A snapshot view is expressed in a standalone form that can be used and
            interpreted without considering the base StructureDefinition.

        differential: A differential view is expressed relative to the base StructureDefinition - a
            statement of differences that it applies.

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
        from spark_fhir_schemas.r4.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4.complex_types.structuredefinition_mapping import StructureDefinition_MappingSchema
        from spark_fhir_schemas.r4.complex_types.structuredefinition_context import StructureDefinition_ContextSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.structuredefinition_snapshot import StructureDefinition_SnapshotSchema
        from spark_fhir_schemas.r4.complex_types.structuredefinition_differential import StructureDefinition_DifferentialSchema
        if (
            max_recursion_limit and
            nesting_list.count("StructureDefinition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["StructureDefinition"]
        schema = StructType(
            [
                # This is a StructureDefinition resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # An absolute URI that is used to identify this structure definition when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this structure
                # definition is (or will be) published. This URL can be the target of a
                # canonical reference. It SHALL remain the same when the structure definition is
                # stored on different servers.
                StructField(
                    "url",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A formal identifier that is used to identify this structure definition when it
                # is represented in other formats, or referenced in a specification, model,
                # design or an instance.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The identifier that is used to identify this version of the structure
                # definition when it is referenced in a specification, model, design or
                # instance. This is an arbitrary value managed by the structure definition
                # author and is not expected to be globally unique. For example, it might be a
                # timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
                # no expectation that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the structure definition. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the structure definition.
                StructField("title", StringType(), True),
                # The status of this structure definition. Enables tracking the life-cycle of
                # the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this structure definition is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the structure definition was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the structure definition changes.
                StructField(
                    "date",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The name of the organization or individual that published the structure
                # definition.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A free text natural language description of the structure definition from a
                # consumer's perspective.
                StructField(
                    "description",
                    markdownSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate structure
                # definition instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A legal or geographic region in which the structure definition is intended to
                # be used.
                StructField(
                    "jurisdiction",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Explanation of why this structure definition is needed and why it has been
                # designed as it has.
                StructField(
                    "purpose",
                    markdownSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A copyright statement relating to the structure definition and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the structure definition.
                StructField(
                    "copyright",
                    markdownSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A set of key words or terms from external terminologies that may be used to
                # assist with indexing and searching of templates nby describing the use of this
                # structure definition, or the content it describes.
                StructField(
                    "keyword",
                    ArrayType(
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The version of the FHIR specification on which this StructureDefinition is
                # based - this is the formal version of the specification, without the revision
                # number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.
                StructField("fhirVersion", StringType(), True),
                # An external specification that the content is mapped to.
                StructField(
                    "mapping",
                    ArrayType(
                        StructureDefinition_MappingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Defines the kind of structure that this definition is describing.
                StructField("kind", StringType(), True),
                # Whether structure this definition describes is abstract or not  - that is,
                # whether the structure is not intended to be instantiated. For Resources and
                # Data types, abstract types will never be exchanged  between systems.
                StructField("abstract", BooleanType(), True),
                # Identifies the types of resource or data type elements to which the extension
                # can be applied.
                StructField(
                    "context",
                    ArrayType(
                        StructureDefinition_ContextSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A set of rules as FHIRPath Invariants about when the extension can be used
                # (e.g. co-occurrence variants for the extension). All the rules must be true.
                StructField("contextInvariant", ArrayType(StringType()), True),
                # The type this structure describes. If the derivation kind is 'specialization'
                # then this is the master definition for a type, and there is always one of
                # these (a data type, an extension, a resource, including abstract ones).
                # Otherwise the structure definition is a constraint on the stated type (and in
                # this case, the type cannot be an abstract type).  References are URLs that are
                # relative to http://hl7.org/fhir/StructureDefinition e.g. "string" is a
                # reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are
                # only allowed in logical models.
                StructField(
                    "type",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # An absolute URI that is the base structure from which this type is derived,
                # either by specialization or constraint.
                StructField(
                    "baseDefinition",
                    canonicalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # How the type relates to the baseDefinition.
                StructField("derivation", StringType(), True),
                # A snapshot view is expressed in a standalone form that can be used and
                # interpreted without considering the base StructureDefinition.
                StructField(
                    "snapshot",
                    StructureDefinition_SnapshotSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A differential view is expressed relative to the base StructureDefinition - a
                # statement of differences that it applies.
                StructField(
                    "differential",
                    StructureDefinition_DifferentialSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
