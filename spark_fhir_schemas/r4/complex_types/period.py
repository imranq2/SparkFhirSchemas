from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Period:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A time period defined by a start and end date and optionally time.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        start: The start of the period. The boundary is inclusive.

        end: The end of the period. If the end of the period is missing, it means no end
            was known or planned at the time the instance was created. The start may be in
            the past, and the end date in the future, which means that period is
            expected/planned to end at that time.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
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
                # The start of the period. The boundary is inclusive.
                StructField(
                    "start", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The end of the period. If the end of the period is missing, it means no end
                # was known or planned at the time the instance was created. The start may be in
                # the past, and the end date in the future, which means that period is
                # expected/planned to end at that time.
                StructField(
                    "end", dateTime.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
