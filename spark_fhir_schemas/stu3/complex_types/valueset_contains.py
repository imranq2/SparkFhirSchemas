from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ValueSet_ContainsSchema:
    """
    A value set specifies a set of codes drawn from one or more code systems.
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
        A value set specifies a set of codes drawn from one or more code systems.


        system: An absolute URI which is the code system in which the code for this item in
            the expansion is defined.

        abstract: If true, this entry is included in the expansion for navigational purposes,
            and the user cannot select the code directly as a proper value.

        inactive: If the concept is inactive in the code system that defines it. Inactive codes
            are those that are no longer to be used, but are maintained by the code system
            for understanding legacy data.

        version: The version of this code system that defined this code and/or display. This
            should only be used with code systems that do not enforce concept permanence.

        code: The code for this item in the expansion hierarchy. If this code is missing the
            entry in the hierarchy is a place holder (abstract) and does not represent a
            valid code in the value set.

        display: The recommended display for this item in the expansion.

        designation: Additional representations for this item - other languages, aliases,
            specialized purposes, used for particular purposes, etc. These are relevant
            when the conditions of the expansion do not fix to a single correct
            representation.

        contains: Other codes and entries contained under this entry in the hierarchy.

        """
        from spark_fhir_schemas.stu3.complex_types.valueset_designation import ValueSet_DesignationSchema
        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Contains") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Contains"]
        schema = StructType(
            [
                # An absolute URI which is the code system in which the code for this item in
                # the expansion is defined.
                StructField("system", StringType(), True),
                # If true, this entry is included in the expansion for navigational purposes,
                # and the user cannot select the code directly as a proper value.
                StructField("abstract", BooleanType(), True),
                # If the concept is inactive in the code system that defines it. Inactive codes
                # are those that are no longer to be used, but are maintained by the code system
                # for understanding legacy data.
                StructField("inactive", BooleanType(), True),
                # The version of this code system that defined this code and/or display. This
                # should only be used with code systems that do not enforce concept permanence.
                StructField("version", StringType(), True),
                # The code for this item in the expansion hierarchy. If this code is missing the
                # entry in the hierarchy is a place holder (abstract) and does not represent a
                # valid code in the value set.
                StructField("code", StringType(), True),
                # The recommended display for this item in the expansion.
                StructField("display", StringType(), True),
                # Additional representations for this item - other languages, aliases,
                # specialized purposes, used for particular purposes, etc. These are relevant
                # when the conditions of the expansion do not fix to a single correct
                # representation.
                StructField(
                    "designation",
                    ArrayType(
                        ValueSet_DesignationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Other codes and entries contained under this entry in the hierarchy.
                StructField(
                    "contains",
                    ArrayType(
                        ValueSet_ContainsSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
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
