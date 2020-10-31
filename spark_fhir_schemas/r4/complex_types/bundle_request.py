from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Bundle_Request:
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

        method: In a transaction or batch, this is the HTTP action to be executed for this
            entry. In a history bundle, this indicates the HTTP action that occurred.

        url: The URL for this entry, relative to the root (the address to which the request
            is posted).

        ifNoneMatch: If the ETag values match, return a 304 Not Modified status. See the API
            documentation for ["Conditional Read"](http.html#cread).

        ifModifiedSince: Only perform the operation if the last updated date matches. See the API
            documentation for ["Conditional Read"](http.html#cread).

        ifMatch: Only perform the operation if the Etag value matches. For more information,
            see the API section ["Managing Resource Contention"](http.html#concurrency).

        ifNoneExist: Instruct the server not to perform the create if a specified resource already
            exists. For further information, see the API documentation for ["Conditional
            Create"](http.html#ccreate). This is just the query portion of the URL - what
            follows the "?" (not including the "?").

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.instant import instant
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
                # In a transaction or batch, this is the HTTP action to be executed for this
                # entry. In a history bundle, this indicates the HTTP action that occurred.
                StructField("method", StringType(), True),
                # The URL for this entry, relative to the root (the address to which the request
                # is posted).
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # If the ETag values match, return a 304 Not Modified status. See the API
                # documentation for ["Conditional Read"](http.html#cread).
                StructField("ifNoneMatch", StringType(), True),
                # Only perform the operation if the last updated date matches. See the API
                # documentation for ["Conditional Read"](http.html#cread).
                StructField(
                    "ifModifiedSince", instant.get_schema(recursion_depth + 1),
                    True
                ),
                # Only perform the operation if the Etag value matches. For more information,
                # see the API section ["Managing Resource Contention"](http.html#concurrency).
                StructField("ifMatch", StringType(), True),
                # Instruct the server not to perform the create if a specified resource already
                # exists. For further information, see the API documentation for ["Conditional
                # Create"](http.html#ccreate). This is just the query portion of the URL - what
                # follows the "?" (not including the "?").
                StructField("ifNoneExist", StringType(), True),
            ]
        )
        return schema
