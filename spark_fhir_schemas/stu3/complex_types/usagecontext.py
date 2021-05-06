from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class UsageContextSchema:
    """
    Specifies clinical/business/etc metadata that can be used to retrieve, index
    and/or categorize an artifact. This metadata can either be specific to the
    applicable population (e.g., age category, DRG) or the specific context of
    care (e.g., venue, care setting, provider of care).
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
        Specifies clinical/business/etc metadata that can be used to retrieve, index
        and/or categorize an artifact. This metadata can either be specific to the
        applicable population (e.g., age category, DRG) or the specific context of
        care (e.g., venue, care setting, provider of care).


        code: A code that identifies the type of context being specified by this usage
            context.

        valueCodeableConcept: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        valueQuantity: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        valueRange: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        """
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        if (
            max_recursion_limit
            and nesting_list.count("UsageContext") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["UsageContext"]
        schema = StructType(
            [
                # A code that identifies the type of context being specified by this usage
                # context.
                StructField(
                    "code",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueRange",
                    RangeSchema.get_schema(
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
