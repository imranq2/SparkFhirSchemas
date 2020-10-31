from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class markdownSchema:
    """
    A string that may contain Github Flavored Markdown syntax for optional
    processing by a mark down presentation engine
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A string that may contain Github Flavored Markdown syntax for optional
        processing by a mark down presentation engine


        """
        return StringType()