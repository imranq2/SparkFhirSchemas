from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NamingSystem_UniqueIdSchema:
    """
    A curated namespace that issues unique symbols within that namespace for the
    identification of concepts, people, devices, etc.  Represents a "System" used
    within the Identifier and Coding data types.
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
        A curated namespace that issues unique symbols within that namespace for the
        identification of concepts, people, devices, etc.  Represents a "System" used
        within the Identifier and Coding data types.


        type: Identifies the unique identifier scheme used for this particular identifier.

        value: The string that should be sent over the wire to identify the code system or
            identifier system.

        preferred: Indicates whether this identifier is the "preferred" identifier of this type.

        comment: Notes about the past or intended usage of this identifier.

        period: Identifies the period of time over which this identifier is considered
            appropriate to refer to the naming system.  Outside of this window, the
            identifier might be non-deterministic.

        """
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        if (
            max_recursion_limit and
            nesting_list.count("NamingSystem_UniqueId") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["NamingSystem_UniqueId"]
        schema = StructType(
            [
                # Identifies the unique identifier scheme used for this particular identifier.
                StructField("type", StringType(), True),
                # The string that should be sent over the wire to identify the code system or
                # identifier system.
                StructField("value", StringType(), True),
                # Indicates whether this identifier is the "preferred" identifier of this type.
                StructField("preferred", BooleanType(), True),
                # Notes about the past or intended usage of this identifier.
                StructField("comment", StringType(), True),
                # Identifies the period of time over which this identifier is considered
                # appropriate to refer to the naming system.  Outside of this window, the
                # identifier might be non-deterministic.
                StructField(
                    "period",
                    PeriodSchema.get_schema(
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
