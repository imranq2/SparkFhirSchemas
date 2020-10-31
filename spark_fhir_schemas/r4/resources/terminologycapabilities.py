from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TerminologyCapabilities:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A TerminologyCapabilities resource documents a set of capabilities (behaviors)
        of a FHIR Terminology Server that may be used as a statement of actual server
        functionality or a statement of required or desired server implementation.


        resourceType: This is a TerminologyCapabilities resource

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

        url: An absolute URI that is used to identify this terminology capabilities when it
            is referenced in a specification, model, design or an instance; also called
            its canonical identifier. This SHOULD be globally unique and SHOULD be a
            literal address at which at which an authoritative instance of this
            terminology capabilities is (or will be) published. This URL can be the target
            of a canonical reference. It SHALL remain the same when the terminology
            capabilities is stored on different servers.

        version: The identifier that is used to identify this version of the terminology
            capabilities when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the terminology capabilities
            author and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
            no expectation that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the terminology capabilities. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.

        title: A short, descriptive, user-friendly title for the terminology capabilities.

        status: The status of this terminology capabilities. Enables tracking the life-cycle
            of the content.

        experimental: A Boolean value to indicate that this terminology capabilities is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the terminology capabilities was
            published. The date must change when the business version changes and it must
            change if the status code changes. In addition, it should change when the
            substantive content of the terminology capabilities changes.

        publisher: The name of the organization or individual that published the terminology
            capabilities.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the terminology capabilities from
            a consumer's perspective. Typically, this is used when the capability
            statement describes a desired rather than an actual solution, for example as a
            formal expression of requirements as part of an RFP.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate terminology
            capabilities instances.

        jurisdiction: A legal or geographic region in which the terminology capabilities is intended
            to be used.

        purpose: Explanation of why this terminology capabilities is needed and why it has been
            designed as it has.

        copyright: A copyright statement relating to the terminology capabilities and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the terminology capabilities.

        kind: The way that this statement is intended to be used, to describe an actual
            running instance of software, a particular product (kind, not instance of
            software) or a class of implementation (e.g. a desired purchase).

        software: Software that is covered by this terminology capability statement.  It is used
            when the statement describes the capabilities of a particular software
            version, independent of an installation.

        implementation: Identifies a specific implementation instance that is described by the
            terminology capability statement - i.e. a particular installation, rather than
            the capabilities of a software program.

        lockedDate: Whether the server supports lockedDate.

        codeSystem: Identifies a code system that is supported by the server. If there is a no
            code system URL, then this declares the general assumptions a client can make
            about support for any CodeSystem resource.

        expansion: Information about the [ValueSet/$expand](valueset-operation-expand.html)
            operation.

        codeSearch: The degree to which the server supports the code search parameter on ValueSet,
            if it is supported.

        validateCode: Information about the [ValueSet/$validate-code](valueset-operation-validate-
            code.html) operation.

        translation: Information about the [ConceptMap/$translate](conceptmap-operation-
            translate.html) operation.

        closure: Whether the $closure operation is supported.

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
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_software import TerminologyCapabilities_Software
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_implementation import TerminologyCapabilities_Implementation
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_codesystem import TerminologyCapabilities_CodeSystem
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_expansion import TerminologyCapabilities_Expansion
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_validatecode import TerminologyCapabilities_ValidateCode
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_translation import TerminologyCapabilities_Translation
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_closure import TerminologyCapabilities_Closure
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a TerminologyCapabilities resource
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
                # An absolute URI that is used to identify this terminology capabilities when it
                # is referenced in a specification, model, design or an instance; also called
                # its canonical identifier. This SHOULD be globally unique and SHOULD be a
                # literal address at which at which an authoritative instance of this
                # terminology capabilities is (or will be) published. This URL can be the target
                # of a canonical reference. It SHALL remain the same when the terminology
                # capabilities is stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # The identifier that is used to identify this version of the terminology
                # capabilities when it is referenced in a specification, model, design or
                # instance. This is an arbitrary value managed by the terminology capabilities
                # author and is not expected to be globally unique. For example, it might be a
                # timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
                # no expectation that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the terminology capabilities. This name
                # should be usable as an identifier for the module by machine processing
                # applications such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the terminology capabilities.
                StructField("title", StringType(), True),
                # The status of this terminology capabilities. Enables tracking the life-cycle
                # of the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this terminology capabilities is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the terminology capabilities was
                # published. The date must change when the business version changes and it must
                # change if the status code changes. In addition, it should change when the
                # substantive content of the terminology capabilities changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the terminology
                # capabilities.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the terminology capabilities from
                # a consumer's perspective. Typically, this is used when the capability
                # statement describes a desired rather than an actual solution, for example as a
                # formal expression of requirements as part of an RFP.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate terminology
                # capabilities instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the terminology capabilities is intended
                # to be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Explanation of why this terminology capabilities is needed and why it has been
                # designed as it has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # A copyright statement relating to the terminology capabilities and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the terminology capabilities.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # The way that this statement is intended to be used, to describe an actual
                # running instance of software, a particular product (kind, not instance of
                # software) or a class of implementation (e.g. a desired purchase).
                StructField(
                    "kind", code.get_schema(recursion_depth + 1), True
                ),
                # Software that is covered by this terminology capability statement.  It is used
                # when the statement describes the capabilities of a particular software
                # version, independent of an installation.
                StructField(
                    "software",
                    TerminologyCapabilities_Software.
                    get_schema(recursion_depth + 1), True
                ),
                # Identifies a specific implementation instance that is described by the
                # terminology capability statement - i.e. a particular installation, rather than
                # the capabilities of a software program.
                StructField(
                    "implementation",
                    TerminologyCapabilities_Implementation.
                    get_schema(recursion_depth + 1), True
                ),
                # Whether the server supports lockedDate.
                StructField("lockedDate", BooleanType(), True),
                # Identifies a code system that is supported by the server. If there is a no
                # code system URL, then this declares the general assumptions a client can make
                # about support for any CodeSystem resource.
                StructField(
                    "codeSystem",
                    ArrayType(
                        TerminologyCapabilities_CodeSystem.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Information about the [ValueSet/$expand](valueset-operation-expand.html)
                # operation.
                StructField(
                    "expansion",
                    TerminologyCapabilities_Expansion.
                    get_schema(recursion_depth + 1), True
                ),
                # The degree to which the server supports the code search parameter on ValueSet,
                # if it is supported.
                StructField("codeSearch", StringType(), True),
                # Information about the [ValueSet/$validate-code](valueset-operation-validate-
                # code.html) operation.
                StructField(
                    "validateCode",
                    TerminologyCapabilities_ValidateCode.
                    get_schema(recursion_depth + 1), True
                ),
                # Information about the [ConceptMap/$translate](conceptmap-operation-
                # translate.html) operation.
                StructField(
                    "translation",
                    TerminologyCapabilities_Translation.
                    get_schema(recursion_depth + 1), True
                ),
                # Whether the $closure operation is supported.
                StructField(
                    "closure",
                    TerminologyCapabilities_Closure.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
