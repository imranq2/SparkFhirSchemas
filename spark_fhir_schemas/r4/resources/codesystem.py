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
class CodeSystemSchema:
    """
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and optionally
    define a part or all of its content.
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
        The CodeSystem resource is used to declare the existence of and describe a
        code system or code system supplement and its key properties, and optionally
        define a part or all of its content.


        resourceType: This is a CodeSystem resource

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

        url: An absolute URI that is used to identify this code system when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this code system is (or
            will be) published. This URL can be the target of a canonical reference. It
            SHALL remain the same when the code system is stored on different servers.
            This is used in [Coding](datatypes.html#Coding).system.

        identifier: A formal identifier that is used to identify this code system when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the code system when
            it is referenced in a specification, model, design or instance. This is an
            arbitrary value managed by the code system author and is not expected to be
            globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
            managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence. This is used in
            [Coding](datatypes.html#Coding).version.

        name: A natural language name identifying the code system. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        title: A short, descriptive, user-friendly title for the code system.

        status: The date (and optionally time) when the code system resource was created or
            revised.

        experimental: A Boolean value to indicate that this code system is authored for testing
            purposes (or education/evaluation/marketing) and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the code system was published. The date
            must change when the business version changes and it must change if the status
            code changes. In addition, it should change when the substantive content of
            the code system changes.

        publisher: The name of the organization or individual that published the code system.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the code system from a consumer's
            perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate code system
            instances.

        jurisdiction: A legal or geographic region in which the code system is intended to be used.

        purpose: Explanation of why this code system is needed and why it has been designed as
            it has.

        copyright: A copyright statement relating to the code system and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the code system.

        caseSensitive: If code comparison is case sensitive when codes within this system are
            compared to each other.

        valueSet: Canonical reference to the value set that contains the entire code system.

        hierarchyMeaning: The meaning of the hierarchy of concepts as represented in this resource.

        compositional: The code system defines a compositional (post-coordination) grammar.

        versionNeeded: This flag is used to signify that the code system does not commit to concept
            permanence across versions. If true, a version must be specified when
            referencing this code system.

        content: The extent of the content of the code system (the concepts and codes it
            defines) are represented in this resource instance.

        supplements: The canonical URL of the code system that this code system supplement is
            adding designations and properties to.

        count: The total number of concepts defined by the code system. Where the code system
            has a compositional grammar, the basis of this count is defined by the system
            steward.

        filter: A filter that can be used in a value set compose statement when selecting
            concepts using a filter.

        property: A property defines an additional slot through which additional information can
            be provided about a concept.

        concept: Concepts that are in the code system. The concept definitions are inherently
            hierarchical, but the definitions must be consulted to determine what the
            meanings of the hierarchical relationships are.

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
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedIntSchema
        from spark_fhir_schemas.r4.complex_types.codesystem_filter import CodeSystem_FilterSchema
        from spark_fhir_schemas.r4.complex_types.codesystem_property import CodeSystem_PropertySchema
        from spark_fhir_schemas.r4.complex_types.codesystem_concept import CodeSystem_ConceptSchema
        if (
            max_recursion_limit
            and nesting_list.count("CodeSystem") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CodeSystem"]
        schema = StructType(
            [
                # This is a CodeSystem resource
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
                # An absolute URI that is used to identify this code system when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this code system is (or
                # will be) published. This URL can be the target of a canonical reference. It
                # SHALL remain the same when the code system is stored on different servers.
                # This is used in [Coding](datatypes.html#Coding).system.
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
                # A formal identifier that is used to identify this code system when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
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
                # The identifier that is used to identify this version of the code system when
                # it is referenced in a specification, model, design or instance. This is an
                # arbitrary value managed by the code system author and is not expected to be
                # globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
                # managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence. This is used in
                # [Coding](datatypes.html#Coding).version.
                StructField("version", StringType(), True),
                # A natural language name identifying the code system. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the code system.
                StructField("title", StringType(), True),
                # The date (and optionally time) when the code system resource was created or
                # revised.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this code system is authored for testing
                # purposes (or education/evaluation/marketing) and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the code system was published. The date
                # must change when the business version changes and it must change if the status
                # code changes. In addition, it should change when the substantive content of
                # the code system changes.
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
                # The name of the organization or individual that published the code system.
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
                # A free text natural language description of the code system from a consumer's
                # perspective.
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
                # may be used to assist with indexing and searching for appropriate code system
                # instances.
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
                # A legal or geographic region in which the code system is intended to be used.
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
                # Explanation of why this code system is needed and why it has been designed as
                # it has.
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
                # A copyright statement relating to the code system and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the code system.
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
                # If code comparison is case sensitive when codes within this system are
                # compared to each other.
                StructField("caseSensitive", BooleanType(), True),
                # Canonical reference to the value set that contains the entire code system.
                StructField(
                    "valueSet",
                    canonicalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The meaning of the hierarchy of concepts as represented in this resource.
                StructField("hierarchyMeaning", StringType(), True),
                # The code system defines a compositional (post-coordination) grammar.
                StructField("compositional", BooleanType(), True),
                # This flag is used to signify that the code system does not commit to concept
                # permanence across versions. If true, a version must be specified when
                # referencing this code system.
                StructField("versionNeeded", BooleanType(), True),
                # The extent of the content of the code system (the concepts and codes it
                # defines) are represented in this resource instance.
                StructField("content", StringType(), True),
                # The canonical URL of the code system that this code system supplement is
                # adding designations and properties to.
                StructField(
                    "supplements",
                    canonicalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The total number of concepts defined by the code system. Where the code system
                # has a compositional grammar, the basis of this count is defined by the system
                # steward.
                StructField(
                    "count",
                    unsignedIntSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A filter that can be used in a value set compose statement when selecting
                # concepts using a filter.
                StructField(
                    "filter",
                    ArrayType(
                        CodeSystem_FilterSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A property defines an additional slot through which additional information can
                # be provided about a concept.
                StructField(
                    "property",
                    ArrayType(
                        CodeSystem_PropertySchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Concepts that are in the code system. The concept definitions are inherently
                # hierarchical, but the definitions must be consulted to determine what the
                # meanings of the hierarchical relationships are.
                StructField(
                    "concept",
                    ArrayType(
                        CodeSystem_ConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
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
