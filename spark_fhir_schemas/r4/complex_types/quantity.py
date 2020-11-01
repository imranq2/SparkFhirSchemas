from typing import List
from typing import Union

from pyspark.sql.types import DataType
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
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        A measured amount (or an amount that can potentially be measured). Note that
        measured amounts include amounts that are not precisely quantified, including
        amounts involving arbitrary units and floating currencies.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        value: The value of the measured amount. The value includes an implicit precision in
            the presentation of the value.

        comparator: How the value should be understood and represented - whether the actual value
            is greater or less than the stated value due to measurement issues; e.g. if
            the comparator is "<" , then the real value is < stated value.

        unit: A human-readable form of the unit.

        system: The identification of the system that provides the coded form of the unit.

        code: A computer processable form of the unit in some unit representation system.

        """
        from spark_fhir_schemas.r4.simple_types.decimal import decimalSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        if recursion_list.count(
            "Quantity"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["Quantity"]
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

                # >>> Hiding extension Extension

                # The value of the measured amount. The value includes an implicit precision in
                # the presentation of the value.
                StructField(
                    "value",
                    decimalSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # How the value should be understood and represented - whether the actual value
                # is greater or less than the stated value due to measurement issues; e.g. if
                # the comparator is "<" , then the real value is < stated value.
                StructField("comparator", StringType(), True),
                # A human-readable form of the unit.
                StructField("unit", StringType(), True),
                # The identification of the system that provides the coded form of the unit.
                StructField(
                    "system",
                    uriSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A computer processable form of the unit in some unit representation system.
                StructField(
                    "code",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
            ]
        )
        return schema
