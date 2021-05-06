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
class CodeSystem_Property1Schema:
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


        code: A code that is a reference to CodeSystem.property.code.

        valueCode: The value of this property.

        valueCoding: The value of this property.

        valueString: The value of this property.

        valueInteger: The value of this property.

        valueBoolean: The value of this property.

        valueDateTime: The value of this property.

        """
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        if (
            max_recursion_limit and
            nesting_list.count("CodeSystem_Property1") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CodeSystem_Property1"]
        schema = StructType(
            [
                # A code that is a reference to CodeSystem.property.code.
                StructField("code", StringType(), True),
                # The value of this property.
                StructField("valueCode", StringType(), True),
                # The value of this property.
                StructField(
                    "valueCoding",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The value of this property.
                StructField("valueString", StringType(), True),
                # The value of this property.
                StructField("valueInteger", IntegerType(), True),
                # The value of this property.
                StructField("valueBoolean", BooleanType(), True),
                # The value of this property.
                StructField("valueDateTime", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema