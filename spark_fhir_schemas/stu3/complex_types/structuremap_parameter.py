from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class StructureMap_ParameterSchema:
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


        valueId: Parameter value - variable or literal.

        valueString: Parameter value - variable or literal.

        valueBoolean: Parameter value - variable or literal.

        valueInteger: Parameter value - variable or literal.

        valueDecimal: Parameter value - variable or literal.

        """
        if (
            max_recursion_limit and
            nesting_list.count("StructureMap_Parameter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["StructureMap_Parameter"]
        schema = StructType(
            [
                # Parameter value - variable or literal.
                StructField("valueId", StringType(), True),
                # Parameter value - variable or literal.
                StructField("valueString", StringType(), True),
                # Parameter value - variable or literal.
                StructField("valueBoolean", BooleanType(), True),
                # Parameter value - variable or literal.
                StructField("valueInteger", IntegerType(), True),
                # Parameter value - variable or literal.
                StructField("valueDecimal", IntegerType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
