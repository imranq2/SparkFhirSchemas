from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class StructureMap_RuleSchema:
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


        name: Name of the rule for internal references.

        source: Source inputs to the mapping.

        target: Content to create because of this mapping rule.

        rule: Rules contained in this rule.

        dependent: Which other rules to apply in the context of this rule.

        documentation: Documentation for this instance of data.

        """
        from spark_fhir_schemas.stu3.complex_types.structuremap_source import StructureMap_SourceSchema
        from spark_fhir_schemas.stu3.complex_types.structuremap_target import StructureMap_TargetSchema
        from spark_fhir_schemas.stu3.complex_types.structuremap_dependent import StructureMap_DependentSchema
        if (
            max_recursion_limit
            and nesting_list.count("StructureMap_Rule") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["StructureMap_Rule"]
        schema = StructType(
            [
                # Name of the rule for internal references.
                StructField("name", StringType(), True),
                # Source inputs to the mapping.
                StructField(
                    "source",
                    ArrayType(
                        StructureMap_SourceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Content to create because of this mapping rule.
                StructField(
                    "target",
                    ArrayType(
                        StructureMap_TargetSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Rules contained in this rule.
                StructField(
                    "rule",
                    ArrayType(
                        StructureMap_RuleSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Which other rules to apply in the context of this rule.
                StructField(
                    "dependent",
                    ArrayType(
                        StructureMap_DependentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
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