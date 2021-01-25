from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StructType
from pyspark.sql.types import TimestampType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class dateTimeSchema:
    """
    A date, date-time or partial date (e.g. just year or year + month).  If hours
    and minutes are specified, a time zone SHALL be populated. The format is a
    union of the schema types gYear, gYearMonth, date and dateTime. Seconds must
    be provided due to schema type constraints but may be zero-filled and may be
    ignored.                 Dates SHALL be valid dates.
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
        A date, date-time or partial date (e.g. just year or year + month).  If hours
        and minutes are specified, a time zone SHALL be populated. The format is a
        union of the schema types gYear, gYearMonth, date and dateTime. Seconds must
        be provided due to schema type constraints but may be zero-filled and may be
        ignored.                 Dates SHALL be valid dates.


        """
        return TimestampType()
