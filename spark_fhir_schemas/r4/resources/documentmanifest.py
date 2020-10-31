from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DocumentManifest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A collection of documents compiled for a purpose together with metadata that
        applies to the collection.


        resourceType: This is a DocumentManifest resource

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

        masterIdentifier: A single identifier that uniquely identifies this manifest. Principally used
            to refer to the manifest in non-FHIR contexts.

        identifier: Other identifiers associated with the document manifest, including version
            independent  identifiers.

        status: The status of this document manifest.

        type: The code specifying the type of clinical activity that resulted in placing the
            associated content into the DocumentManifest.

        subject: Who or what the set of documents is about. The documents can be about a
            person, (patient or healthcare practitioner), a device (i.e. machine) or even
            a group of subjects (such as a document about a herd of farm animals, or a set
            of patients that share a common exposure). If the documents cross more than
            one subject, then more than one subject is allowed here (unusual use case).

        created: When the document manifest was created for submission to the server (not
            necessarily the same thing as the actual resource last modified time, since it
            may be modified, replicated, etc.).

        author: Identifies who is the author of the manifest. Manifest author is not
            necessarly the author of the references included.

        recipient: A patient, practitioner, or organization for which this set of documents is
            intended.

        source: Identifies the source system, application, or software that produced the
            document manifest.

        description: Human-readable description of the source document. This is sometimes known as
            the "title".

        content: The list of Resources that consist of the parts of this manifest.

        related: Related identifiers or resources associated with the DocumentManifest.

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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.documentmanifest_related import DocumentManifest_Related
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a DocumentManifest resource
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
                # A single identifier that uniquely identifies this manifest. Principally used
                # to refer to the manifest in non-FHIR contexts.
                StructField(
                    "masterIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # Other identifiers associated with the document manifest, including version
                # independent  identifiers.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The status of this document manifest.
                StructField("status", StringType(), True),
                # The code specifying the type of clinical activity that resulted in placing the
                # associated content into the DocumentManifest.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Who or what the set of documents is about. The documents can be about a
                # person, (patient or healthcare practitioner), a device (i.e. machine) or even
                # a group of subjects (such as a document about a herd of farm animals, or a set
                # of patients that share a common exposure). If the documents cross more than
                # one subject, then more than one subject is allowed here (unusual use case).
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # When the document manifest was created for submission to the server (not
                # necessarily the same thing as the actual resource last modified time, since it
                # may be modified, replicated, etc.).
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Identifies who is the author of the manifest. Manifest author is not
                # necessarly the author of the references included.
                StructField(
                    "author",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A patient, practitioner, or organization for which this set of documents is
                # intended.
                StructField(
                    "recipient",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the source system, application, or software that produced the
                # document manifest.
                StructField(
                    "source", uri.get_schema(recursion_depth + 1), True
                ),
                # Human-readable description of the source document. This is sometimes known as
                # the "title".
                StructField("description", StringType(), True),
                # The list of Resources that consist of the parts of this manifest.
                StructField(
                    "content",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Related identifiers or resources associated with the DocumentManifest.
                StructField(
                    "related",
                    ArrayType(
                        DocumentManifest_Related.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
