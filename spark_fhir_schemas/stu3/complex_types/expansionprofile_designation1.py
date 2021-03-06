from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ExpansionProfile_Designation1Schema:
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
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
        Resource to define constraints on the Expansion of a FHIR ValueSet.


        language: The language this designation is defined for.

        use: Which kinds of designation to include in the expansion.

        """
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        if (
            max_recursion_limit
            and nesting_list.count("ExpansionProfile_Designation1") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ExpansionProfile_Designation1"
        ]
        schema = StructType(
            [
                # The language this designation is defined for.
                StructField("language", StringType(), True),
                # Which kinds of designation to include in the expansion.
                StructField(
                    "use",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
