from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ValueSet_ComposeSchema:
    """
    A ValueSet resource instance specifies a set of codes drawn from one or more
    code systems, intended for use in a particular context. Value sets link
    between [[[CodeSystem]]] definitions and their use in [coded
    elements](terminologies.html).
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
        """
        A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        lockedDate: The Locked Date is  the effective date that is used to determine the version
            of all referenced Code Systems and Value Set Definitions included in the
            compose that are not already tied to a specific version.

        inactive: Whether inactive codes - codes that are not approved for current use - are in
            the value set. If inactive = true, inactive codes are to be included in the
            expansion, if inactive = false, the inactive codes will not be included in the
            expansion. If absent, the behavior is determined by the implementation, or by
            the applicable $expand parameters (but generally, inactive codes would be
            expected to be included).

        include: Include one or more codes from a code system or other value set(s).

        exclude: Exclude one or more codes from the value set based on code system filters
            and/or other value sets.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.valueset_include import ValueSet_IncludeSchema
        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Compose") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Compose"]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The Locked Date is  the effective date that is used to determine the version
                # of all referenced Code Systems and Value Set Definitions included in the
                # compose that are not already tied to a specific version.
                StructField("lockedDate", DateType(), True),
                # Whether inactive codes - codes that are not approved for current use - are in
                # the value set. If inactive = true, inactive codes are to be included in the
                # expansion, if inactive = false, the inactive codes will not be included in the
                # expansion. If absent, the behavior is determined by the implementation, or by
                # the applicable $expand parameters (but generally, inactive codes would be
                # expected to be included).
                StructField("inactive", BooleanType(), True),
                # Include one or more codes from a code system or other value set(s).
                StructField(
                    "include",
                    ArrayType(
                        ValueSet_IncludeSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Exclude one or more codes from the value set based on code system filters
                # and/or other value sets.
                StructField(
                    "exclude",
                    ArrayType(
                        ValueSet_IncludeSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
