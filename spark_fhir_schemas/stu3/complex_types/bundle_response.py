from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Bundle_ResponseSchema:
    """
    A container for a collection of resources.
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
        A container for a collection of resources.


        status: The status code returned by processing this entry. The status SHALL start with
            a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description
            associated with the status code.

        location: The location header created by processing this operation.

        etag: The etag for the resource, it the operation for the entry produced a versioned
            resource (see [Resource Metadata and Versioning](http.html#versioning) and
            [Managing Resource Contention](http.html#concurrency)).

        lastModified: The date/time that the resource was modified on the server.

        outcome: An OperationOutcome containing hints and warnings produced as part of
            processing this entry in a batch or transaction.

        """
        from spark_fhir_schemas.stu3.simple_types.resourcelist import ResourceListSchema
        if (
            max_recursion_limit
            and nesting_list.count("Bundle_Response") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Bundle_Response"]
        schema = StructType(
            [
                # The status code returned by processing this entry. The status SHALL start with
                # a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description
                # associated with the status code.
                StructField("status", StringType(), True),
                # The location header created by processing this operation.
                StructField("location", StringType(), True),
                # The etag for the resource, it the operation for the entry produced a versioned
                # resource (see [Resource Metadata and Versioning](http.html#versioning) and
                # [Managing Resource Contention](http.html#concurrency)).
                StructField("etag", StringType(), True),
                # The date/time that the resource was modified on the server.
                StructField("lastModified", StringType(), True),
                # An OperationOutcome containing hints and warnings produced as part of
                # processing this entry in a batch or transaction.
                StructField(
                    "outcome",
                    ResourceListSchema.get_schema(
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
