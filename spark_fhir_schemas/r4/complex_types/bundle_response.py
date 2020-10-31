from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Bundle_Response:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A container for a collection of resources.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        status: The status code returned by processing this entry. The status SHALL start with
            a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description
            associated with the status code.

        location: The location header created by processing this operation, populated if the
            operation returns a location.

        etag: The Etag for the resource, if the operation for the entry produced a versioned
            resource (see [Resource Metadata and Versioning](http.html#versioning) and
            [Managing Resource Contention](http.html#concurrency)).

        lastModified: The date/time that the resource was modified on the server.

        outcome: An OperationOutcome containing hints and warnings produced as part of
            processing this entry in a batch or transaction.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
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
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The status code returned by processing this entry. The status SHALL start with
                # a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description
                # associated with the status code.
                StructField("status", StringType(), True),
                # The location header created by processing this operation, populated if the
                # operation returns a location.
                StructField(
                    "location", uri.get_schema(recursion_depth + 1), True
                ),
                # The Etag for the resource, if the operation for the entry produced a versioned
                # resource (see [Resource Metadata and Versioning](http.html#versioning) and
                # [Managing Resource Contention](http.html#concurrency)).
                StructField("etag", StringType(), True),
                # The date/time that the resource was modified on the server.
                StructField(
                    "lastModified", instant.get_schema(recursion_depth + 1),
                    True
                ),
                # An OperationOutcome containing hints and warnings produced as part of
                # processing this entry in a batch or transaction.
                StructField(
                    "outcome", ResourceList.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
