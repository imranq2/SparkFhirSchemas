from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class OperationDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A formal computable definition of an operation (on the RESTful interface) or a
        named query (using the search interaction).


        resourceType: This is a OperationDefinition resource

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

        url: An absolute URI that is used to identify this operation definition when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this operation
            definition is (or will be) published. This URL can be the target of a
            canonical reference. It SHALL remain the same when the operation definition is
            stored on different servers.

        version: The identifier that is used to identify this version of the operation
            definition when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the operation definition
            author and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
            no expectation that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the operation definition. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the operation definition.

        status: The status of this operation definition. Enables tracking the life-cycle of
            the content.

        kind: Whether this is an operation or a named query.

        experimental: A Boolean value to indicate that this operation definition is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the operation definition was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the operation definition changes.

        publisher: The name of the organization or individual that published the operation
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the operation definition from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate operation
            definition instances.

        jurisdiction: A legal or geographic region in which the operation definition is intended to
            be used.

        purpose: Explanation of why this operation definition is needed and why it has been
            designed as it has.

        affectsState: Whether the operation affects state. Side effects such as producing audit
            trail entries do not count as 'affecting  state'.

        code: The name used to invoke the operation.

        comment: Additional information about how to use this operation or named query.

        base: Indicates that this operation definition is a constraining profile on the
            base.

        resource: The types on which this operation can be executed.

        system: Indicates whether this operation or named query can be invoked at the system
            level (e.g. without needing to choose a resource type for the context).

        type: Indicates whether this operation or named query can be invoked at the resource
            type level for any given resource type level (e.g. without needing to choose a
            specific resource id for the context).

        instance: Indicates whether this operation can be invoked on a particular instance of
            one of the given types.

        inputProfile: Additional validation information for the in parameters - a single profile
            that covers all the parameters. The profile is a constraint on the parameters
            resource as a whole.

        outputProfile: Additional validation information for the out parameters - a single profile
            that covers all the parameters. The profile is a constraint on the parameters
            resource.

        parameter: The parameters for the operation/query.

        overload: Defines an appropriate combination of parameters to use when invoking this
            operation, to help code generators when generating overloaded parameter sets
            for this operation.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.operationdefinition_parameter import OperationDefinition_Parameter
        from spark_fhir_schemas.r4.complex_types.operationdefinition_overload import OperationDefinition_Overload
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a OperationDefinition resource
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
                # An absolute URI that is used to identify this operation definition when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this operation
                # definition is (or will be) published. This URL can be the target of a
                # canonical reference. It SHALL remain the same when the operation definition is
                # stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # The identifier that is used to identify this version of the operation
                # definition when it is referenced in a specification, model, design or
                # instance. This is an arbitrary value managed by the operation definition
                # author and is not expected to be globally unique. For example, it might be a
                # timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
                # no expectation that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the operation definition. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the operation definition.
                StructField("title", StringType(), True),
                # The status of this operation definition. Enables tracking the life-cycle of
                # the content.
                StructField("status", StringType(), True),
                # Whether this is an operation or a named query.
                StructField("kind", StringType(), True),
                # A Boolean value to indicate that this operation definition is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the operation definition was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the operation definition changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the operation
                # definition.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the operation definition from a
                # consumer's perspective.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate operation
                # definition instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the operation definition is intended to
                # be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Explanation of why this operation definition is needed and why it has been
                # designed as it has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # Whether the operation affects state. Side effects such as producing audit
                # trail entries do not count as 'affecting  state'.
                StructField("affectsState", BooleanType(), True),
                # The name used to invoke the operation.
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                # Additional information about how to use this operation or named query.
                StructField(
                    "comment", markdown.get_schema(recursion_depth + 1), True
                ),
                # Indicates that this operation definition is a constraining profile on the
                # base.
                StructField(
                    "base", canonical.get_schema(recursion_depth + 1), True
                ),
                # The types on which this operation can be executed.
                StructField(
                    "resource",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                # Indicates whether this operation or named query can be invoked at the system
                # level (e.g. without needing to choose a resource type for the context).
                StructField("system", BooleanType(), True),
                # Indicates whether this operation or named query can be invoked at the resource
                # type level for any given resource type level (e.g. without needing to choose a
                # specific resource id for the context).
                StructField("type", BooleanType(), True),
                # Indicates whether this operation can be invoked on a particular instance of
                # one of the given types.
                StructField("instance", BooleanType(), True),
                # Additional validation information for the in parameters - a single profile
                # that covers all the parameters. The profile is a constraint on the parameters
                # resource as a whole.
                StructField(
                    "inputProfile", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                # Additional validation information for the out parameters - a single profile
                # that covers all the parameters. The profile is a constraint on the parameters
                # resource.
                StructField(
                    "outputProfile", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                # The parameters for the operation/query.
                StructField(
                    "parameter",
                    ArrayType(
                        OperationDefinition_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Defines an appropriate combination of parameters to use when invoking this
                # operation, to help code generators when generating overloaded parameter sets
                # for this operation.
                StructField(
                    "overload",
                    ArrayType(
                        OperationDefinition_Overload.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
