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
class QuantitySchema:
    """
    A measured amount (or an amount that can potentially be measured). Note that
    measured amounts include amounts that are not precisely quantified, including
    amounts involving arbitrary units and floating currencies.
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
        A measured amount (or an amount that can potentially be measured). Note that
        measured amounts include amounts that are not precisely quantified, including
        amounts involving arbitrary units and floating currencies.


        value: The value of the measured amount. The value includes an implicit precision in
            the presentation of the value.

        comparator: How the value should be understood and represented - whether the actual value
            is greater or less than the stated value due to measurement issues; e.g. if
            the comparator is "<" , then the real value is < stated value.

        unit: A human-readable form of the unit.

        system: The identification of the system that provides the coded form of the unit.

        code: A computer processable form of the unit in some unit representation system.

        """
        if (
            max_recursion_limit
            and nesting_list.count("Quantity") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Quantity"]
        schema = StructType(
            [
                # The value of the measured amount. The value includes an implicit precision in
                # the presentation of the value.
                StructField("value", IntegerType(), True),
                # How the value should be understood and represented - whether the actual value
                # is greater or less than the stated value due to measurement issues; e.g. if
                # the comparator is "<" , then the real value is < stated value.
                StructField("comparator", StringType(), True),
                # A human-readable form of the unit.
                StructField("unit", StringType(), True),
                # The identification of the system that provides the coded form of the unit.
                StructField("system", StringType(), True),
                # A computer processable form of the unit in some unit representation system.
                StructField("code", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
