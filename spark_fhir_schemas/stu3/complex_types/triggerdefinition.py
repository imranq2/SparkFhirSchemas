from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class TriggerDefinitionSchema:
    """
    A description of a triggering event.
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
        A description of a triggering event.


        type: The type of triggering event.

        eventName: The name of the event (if this is a named-event trigger).

        eventTimingTiming: The timing of the event (if this is a period trigger).

        eventTimingReference: The timing of the event (if this is a period trigger).

        eventTimingDate: The timing of the event (if this is a period trigger).

        eventTimingDateTime: The timing of the event (if this is a period trigger).

        eventData: The triggering data of the event (if this is a data trigger).

        """
        from spark_fhir_schemas.stu3.complex_types.timing import TimingSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.datarequirement import DataRequirementSchema
        if (
            max_recursion_limit
            and nesting_list.count("TriggerDefinition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TriggerDefinition"]
        schema = StructType(
            [
                # The type of triggering event.
                StructField("type", StringType(), True),
                # The name of the event (if this is a named-event trigger).
                StructField("eventName", StringType(), True),
                # The timing of the event (if this is a period trigger).
                StructField(
                    "eventTimingTiming",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The timing of the event (if this is a period trigger).
                StructField(
                    "eventTimingReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The timing of the event (if this is a period trigger).
                StructField("eventTimingDate", StringType(), True),
                # The timing of the event (if this is a period trigger).
                StructField("eventTimingDateTime", StringType(), True),
                # The triggering data of the event (if this is a data trigger).
                StructField(
                    "eventData",
                    DataRequirementSchema.get_schema(
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
