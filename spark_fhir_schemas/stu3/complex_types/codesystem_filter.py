from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CodeSystem_FilterSchema:
    """
    A code system resource specifies a set of codes drawn from one or more code
    systems.
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
        A code system resource specifies a set of codes drawn from one or more code
        systems.


        code: The code that identifies this filter when it is used in the instance.

        description: A description of how or why the filter is used.

        operator: A list of operators that can be used with the filter.

        value: A description of what the value for the filter should be.

        """
        if (
            max_recursion_limit
            and nesting_list.count("CodeSystem_Filter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CodeSystem_Filter"]
        schema = StructType(
            [
                # The code that identifies this filter when it is used in the instance.
                StructField("code", StringType(), True),
                # A description of how or why the filter is used.
                StructField("description", StringType(), True),
                # A list of operators that can be used with the filter.
                # A description of what the value for the filter should be.
                StructField("value", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
