from typing import List
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class xhtmlSchema:
    """
    xhtml - escaped html (see specfication)
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        xhtml - escaped html (see specfication)


        """
        return StringType()
