from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NutritionOrder_AdministrationSchema:
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
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
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


        schedule: The time period and frequency at which the enteral formula should be delivered
            to the patient.

        quantity: The volume of formula to provide to the patient per the specified
            administration schedule.

        rateSimpleQuantity: The rate of administration of formula via a feeding pump, e.g. 60 mL per hour,
            according to the specified schedule.

        rateRatio: The rate of administration of formula via a feeding pump, e.g. 60 mL per hour,
            according to the specified schedule.

        """
        from spark_fhir_schemas.stu3.complex_types.timing import TimingSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.ratio import RatioSchema
        if (
            max_recursion_limit
            and nesting_list.count("NutritionOrder_Administration") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "NutritionOrder_Administration"
        ]
        schema = StructType(
            [
                # The time period and frequency at which the enteral formula should be delivered
                # to the patient.
                StructField(
                    "schedule",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The volume of formula to provide to the patient per the specified
                # administration schedule.
                StructField(
                    "quantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The rate of administration of formula via a feeding pump, e.g. 60 mL per hour,
                # according to the specified schedule.
                StructField(
                    "rateSimpleQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The rate of administration of formula via a feeding pump, e.g. 60 mL per hour,
                # according to the specified schedule.
                StructField(
                    "rateRatio",
                    RatioSchema.get_schema(
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
