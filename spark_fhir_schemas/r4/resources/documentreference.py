from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DocumentReference:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A reference to a document of any kind for any purpose. Provides metadata about
        the document so that the document can be discovered and managed. The scope of
        a document is any seralized object with a mime-type, so includes formal
        patient centric documents (CDA), cliical notes, scanned paper, and non-patient
        specific documents like policy text.


        resourceType: This is a DocumentReference resource

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

        masterIdentifier: Document identifier as assigned by the source of the document. This identifier
            is specific to this version of the document. This unique identifier may be
            used elsewhere to identify this version of the document.

        identifier: Other identifiers associated with the document, including version independent
            identifiers.

        status: The status of this document reference.

        docStatus: The status of the underlying document.

        type: Specifies the particular kind of document referenced  (e.g. History and
            Physical, Discharge Summary, Progress Note). This usually equates to the
            purpose of making the document referenced.

        category: A categorization for the type of document referenced - helps for indexing and
            searching. This may be implied by or derived from the code specified in the
            DocumentReference.type.

        subject: Who or what the document is about. The document can be about a person,
            (patient or healthcare practitioner), a device (e.g. a machine) or even a
            group of subjects (such as a document about a herd of farm animals, or a set
            of patients that share a common exposure).

        date: When the document reference was created.

        author: Identifies who is responsible for adding the information to the document.

        authenticator: Which person or organization authenticates that this document is valid.

        custodian: Identifies the organization or group who is responsible for ongoing
            maintenance of and access to the document.

        relatesTo: Relationships that this document has with other document references that
            already exist.

        description: Human-readable description of the source document.

        securityLabel: A set of Security-Tag codes specifying the level of privacy/security of the
            Document. Note that DocumentReference.meta.security contains the security
            labels of the "reference" to the document, while
            DocumentReference.securityLabel contains a snapshot of the security labels on
            the document the reference refers to.

        content: The document and format referenced. There may be multiple content element
            repetitions, each with a different format.

        context: The clinical context in which the document was prepared.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.documentreference_relatesto import DocumentReference_RelatesTo
        from spark_fhir_schemas.r4.complex_types.documentreference_content import DocumentReference_Content
        from spark_fhir_schemas.r4.complex_types.documentreference_context import DocumentReference_Context
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a DocumentReference resource
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
                # Document identifier as assigned by the source of the document. This identifier
                # is specific to this version of the document. This unique identifier may be
                # used elsewhere to identify this version of the document.
                StructField(
                    "masterIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # Other identifiers associated with the document, including version independent
                # identifiers.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The status of this document reference.
                StructField("status", StringType(), True),
                # The status of the underlying document.
                StructField(
                    "docStatus", code.get_schema(recursion_depth + 1), True
                ),
                # Specifies the particular kind of document referenced  (e.g. History and
                # Physical, Discharge Summary, Progress Note). This usually equates to the
                # purpose of making the document referenced.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A categorization for the type of document referenced - helps for indexing and
                # searching. This may be implied by or derived from the code specified in the
                # DocumentReference.type.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Who or what the document is about. The document can be about a person,
                # (patient or healthcare practitioner), a device (e.g. a machine) or even a
                # group of subjects (such as a document about a herd of farm animals, or a set
                # of patients that share a common exposure).
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # When the document reference was created.
                StructField(
                    "date", instant.get_schema(recursion_depth + 1), True
                ),
                # Identifies who is responsible for adding the information to the document.
                StructField(
                    "author",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Which person or organization authenticates that this document is valid.
                StructField(
                    "authenticator", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Identifies the organization or group who is responsible for ongoing
                # maintenance of and access to the document.
                StructField(
                    "custodian", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Relationships that this document has with other document references that
                # already exist.
                StructField(
                    "relatesTo",
                    ArrayType(
                        DocumentReference_RelatesTo.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Human-readable description of the source document.
                StructField("description", StringType(), True),
                # A set of Security-Tag codes specifying the level of privacy/security of the
                # Document. Note that DocumentReference.meta.security contains the security
                # labels of the "reference" to the document, while
                # DocumentReference.securityLabel contains a snapshot of the security labels on
                # the document the reference refers to.
                StructField(
                    "securityLabel",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The document and format referenced. There may be multiple content element
                # repetitions, each with a different format.
                StructField(
                    "content",
                    ArrayType(
                        DocumentReference_Content.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The clinical context in which the document was prepared.
                StructField(
                    "context",
                    DocumentReference_Context.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
