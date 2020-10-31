from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Meta:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The metadata about a resource. This is content in the resource that is
        maintained by the infrastructure. Changes to the content might not always be
        associated with version changes to the resource.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        versionId: The version specific identifier, as it appears in the version portion of the
            URL. This value changes when the resource is created, updated, or deleted.

        lastUpdated: When the resource last changed - e.g. when the version changed.

        source: A uri that identifies the source system of the resource. This provides a
            minimal amount of [[[Provenance]]] information that can be used to track or
            differentiate the source of information in the resource. The source may
            identify another FHIR server, document, message, database, etc.

        profile: A list of profiles (references to [[[StructureDefinition]]] resources) that
            this resource claims to conform to. The URL is a reference to
            [[[StructureDefinition.url]]].

        security: Security labels applied to this resource. These tags connect specific
            resources to the overall security policy and infrastructure.

        tag: Tags applied to this resource. Tags are intended to be used to identify and
            relate resources to process and workflow, and applications are not required to
            consider the tags when interpreting the meaning of a resource.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The version specific identifier, as it appears in the version portion of the
                # URL. This value changes when the resource is created, updated, or deleted.
                StructField(
                    "versionId", id.get_schema(recursion_depth + 1), True
                ),
                # When the resource last changed - e.g. when the version changed.
                StructField(
                    "lastUpdated", instant.get_schema(recursion_depth + 1),
                    True
                ),
                # A uri that identifies the source system of the resource. This provides a
                # minimal amount of [[[Provenance]]] information that can be used to track or
                # differentiate the source of information in the resource. The source may
                # identify another FHIR server, document, message, database, etc.
                StructField(
                    "source", uri.get_schema(recursion_depth + 1), True
                ),
                # A list of profiles (references to [[[StructureDefinition]]] resources) that
                # this resource claims to conform to. The URL is a reference to
                # [[[StructureDefinition.url]]].
                StructField(
                    "profile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # Security labels applied to this resource. These tags connect specific
                # resources to the overall security policy and infrastructure.
                StructField(
                    "security",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                # Tags applied to this resource. Tags are intended to be used to identify and
                # relate resources to process and workflow, and applications are not required to
                # consider the tags when interpreting the meaning of a resource.
                StructField(
                    "tag", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
