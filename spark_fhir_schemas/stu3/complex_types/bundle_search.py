from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Bundle_SearchSchema:
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


        mode: Why this entry is in the result set - whether it's included as a match or
            because of an _include requirement.

        score: When searching, the server's search ranking score for the entry.

        """
        if (
            max_recursion_limit
            and nesting_list.count("Bundle_Search") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Bundle_Search"]
        schema = StructType(
            [
                # Why this entry is in the result set - whether it's included as a match or
                # because of an _include requirement.
                StructField("mode", StringType(), True),
                # When searching, the server's search ranking score for the entry.
                StructField("score", IntegerType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
