from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class StructureMap_InputSchema:
    """
    A Map of relationships between 2 structures that can be used to transform
    data.
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
        A Map of relationships between 2 structures that can be used to transform
        data.


        name: Name for this instance of data.

        type: Type for this instance of data.

        mode: Mode for this instance of data.

        documentation: Documentation for this instance of data.

        """
        if (
            max_recursion_limit
            and nesting_list.count("StructureMap_Input") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["StructureMap_Input"]
        schema = StructType(
            [
                # Name for this instance of data.
                StructField("name", StringType(), True),
                # Type for this instance of data.
                StructField("type", StringType(), True),
                # Mode for this instance of data.
                StructField("mode", StringType(), True),
                # Documentation for this instance of data.
                StructField("documentation", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
