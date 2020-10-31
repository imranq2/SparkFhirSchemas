from typing import Union

from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class boolean:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Value of "true" or "false"


        """
        return BooleanType()
