from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Distance:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A length - a value with a unit that is a physical distance.


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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The value of the measured amount. The value includes an implicit precision in
                # the presentation of the value.
                StructField(
                    "value", decimal.get_schema(recursion_depth + 1), True
                ),
                # How the value should be understood and represented - whether the actual value
                # is greater or less than the stated value due to measurement issues; e.g. if
                # the comparator is "<" , then the real value is < stated value.
                StructField("comparator", StringType(), True),
                # A human-readable form of the unit.
                StructField("unit", StringType(), True),
                # The identification of the system that provides the coded form of the unit.
                StructField(
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                # A computer processable form of the unit in some unit representation system.
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
