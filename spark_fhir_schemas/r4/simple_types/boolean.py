from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class booleanSchema:
    """
    Value of "true" or "false"
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
        Value of "true" or "false"


        """
        return BooleanType()
