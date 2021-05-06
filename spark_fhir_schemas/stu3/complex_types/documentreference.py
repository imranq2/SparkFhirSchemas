from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DocumentReferenceSchema:
    """
    A reference to a document.
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
        A reference to a document.


        resourceType: This is a DocumentReference resource

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

        class: A categorization for the type of document referenced - helps for indexing and
            searching. This may be implied by or derived from the code specified in the
            DocumentReference.type.

        subject: Who or what the document is about. The document can be about a person,
            (patient or healthcare practitioner), a device (e.g. a machine) or even a
            group of subjects (such as a document about a herd of farm animals, or a set
            of patients that share a common exposure).

        created: When the document was created.

        indexed: When the document reference was created.

        author: Identifies who is responsible for adding the information to the document.

        authenticator: Which person or organization authenticates that this document is valid.

        custodian: Identifies the organization or group who is responsible for ongoing
            maintenance of and access to the document.

        relatesTo: Relationships that this document has with other document references that
            already exist.

        description: Human-readable description of the source document. This is sometimes known as
            the "title".

        securityLabel: A set of Security-Tag codes specifying the level of privacy/security of the
            Document. Note that DocumentReference.meta.security contains the security
            labels of the "reference" to the document, while
            DocumentReference.securityLabel contains a snapshot of the security labels on
            the document the reference refers to.

        content: The document and format referenced. There may be multiple content element
            repetitions, each with a different format.

        context: The clinical context in which the document was prepared.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.documentreference_relatesto import DocumentReference_RelatesToSchema
        from spark_fhir_schemas.stu3.complex_types.documentreference_content import DocumentReference_ContentSchema
        from spark_fhir_schemas.stu3.complex_types.documentreference_context import DocumentReference_ContextSchema
        if (
            max_recursion_limit
            and nesting_list.count("DocumentReference") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DocumentReference"]
        schema = StructType(
            [
                # This is a DocumentReference resource
                StructField("resourceType", StringType(), True),
                # Document identifier as assigned by the source of the document. This identifier
                # is specific to this version of the document. This unique identifier may be
                # used elsewhere to identify this version of the document.
                StructField(
                    "masterIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Other identifiers associated with the document, including version independent
                # identifiers.
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
                # The status of this document reference.
                StructField("status", StringType(), True),
                # The status of the underlying document.
                StructField("docStatus", StringType(), True),
                # Specifies the particular kind of document referenced  (e.g. History and
                # Physical, Discharge Summary, Progress Note). This usually equates to the
                # purpose of making the document referenced.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A categorization for the type of document referenced - helps for indexing and
                # searching. This may be implied by or derived from the code specified in the
                # DocumentReference.type.
                StructField(
                    "class",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Who or what the document is about. The document can be about a person,
                # (patient or healthcare practitioner), a device (e.g. a machine) or even a
                # group of subjects (such as a document about a herd of farm animals, or a set
                # of patients that share a common exposure).
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # When the document was created.
                StructField("created", StringType(), True),
                # When the document reference was created.
                StructField("indexed", StringType(), True),
                # Identifies who is responsible for adding the information to the document.
                StructField(
                    "author",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Which person or organization authenticates that this document is valid.
                StructField(
                    "authenticator",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Identifies the organization or group who is responsible for ongoing
                # maintenance of and access to the document.
                StructField(
                    "custodian",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Relationships that this document has with other document references that
                # already exist.
                StructField(
                    "relatesTo",
                    ArrayType(
                        DocumentReference_RelatesToSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Human-readable description of the source document. This is sometimes known as
                # the "title".
                StructField("description", StringType(), True),
                # A set of Security-Tag codes specifying the level of privacy/security of the
                # Document. Note that DocumentReference.meta.security contains the security
                # labels of the "reference" to the document, while
                # DocumentReference.securityLabel contains a snapshot of the security labels on
                # the document the reference refers to.
                StructField(
                    "securityLabel",
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
                # The document and format referenced. There may be multiple content element
                # repetitions, each with a different format.
                StructField(
                    "content",
                    ArrayType(
                        DocumentReference_ContentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The clinical context in which the document was prepared.
                StructField(
                    "context",
                    DocumentReference_ContextSchema.get_schema(
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
