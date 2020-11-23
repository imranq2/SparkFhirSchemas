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
class DataRequirement_DateFilterSchema:
    """
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
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
        Describes a required data item for evaluation in terms of the type of data,
        and optional code or date-based filters of the data.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        path: The date-valued attribute of the filter. The specified path SHALL be a
            FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
            consist only of identifiers, constant indexers, and .resolve(). The path is
            allowed to contain qualifiers (.) to traverse sub-elements, as well as
            indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
            FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
            must be an integer constant. The path must resolve to an element of type date,
            dateTime, Period, Schedule, or Timing.

        searchParam: A date parameter that refers to a search parameter defined on the specified
            type of the DataRequirement, and which searches on elements of type date,
            dateTime, Period, Schedule, or Timing.

        valueDateTime: The value of the filter. If period is specified, the filter will return only
            those data items that fall within the bounds determined by the Period,
            inclusive of the period boundaries. If dateTime is specified, the filter will
            return only those data items that are equal to the specified dateTime. If a
            Duration is specified, the filter will return only those data items that fall
            within Duration before now.

        valuePeriod: The value of the filter. If period is specified, the filter will return only
            those data items that fall within the bounds determined by the Period,
            inclusive of the period boundaries. If dateTime is specified, the filter will
            return only those data items that are equal to the specified dateTime. If a
            Duration is specified, the filter will return only those data items that fall
            within Duration before now.

        valueDuration: The value of the filter. If period is specified, the filter will return only
            those data items that fall within the bounds determined by the Period,
            inclusive of the period boundaries. If dateTime is specified, the filter will
            return only those data items that are equal to the specified dateTime. If a
            Duration is specified, the filter will return only those data items that fall
            within Duration before now.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        if (
            max_recursion_limit
            and nesting_list.count("DataRequirement_DateFilter") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "DataRequirement_DateFilter"
        ]
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
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The date-valued attribute of the filter. The specified path SHALL be a
                # FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
                # consist only of identifiers, constant indexers, and .resolve(). The path is
                # allowed to contain qualifiers (.) to traverse sub-elements, as well as
                # indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
                # FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
                # must be an integer constant. The path must resolve to an element of type date,
                # dateTime, Period, Schedule, or Timing.
                StructField("path", StringType(), True),
                # A date parameter that refers to a search parameter defined on the specified
                # type of the DataRequirement, and which searches on elements of type date,
                # dateTime, Period, Schedule, or Timing.
                StructField("searchParam", StringType(), True),
                # The value of the filter. If period is specified, the filter will return only
                # those data items that fall within the bounds determined by the Period,
                # inclusive of the period boundaries. If dateTime is specified, the filter will
                # return only those data items that are equal to the specified dateTime. If a
                # Duration is specified, the filter will return only those data items that fall
                # within Duration before now.
                StructField("valueDateTime", StringType(), True),
                # The value of the filter. If period is specified, the filter will return only
                # those data items that fall within the bounds determined by the Period,
                # inclusive of the period boundaries. If dateTime is specified, the filter will
                # return only those data items that are equal to the specified dateTime. If a
                # Duration is specified, the filter will return only those data items that fall
                # within Duration before now.
                StructField(
                    "valuePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The value of the filter. If period is specified, the filter will return only
                # those data items that fall within the bounds determined by the Period,
                # inclusive of the period boundaries. If dateTime is specified, the filter will
                # return only those data items that are equal to the specified dateTime. If a
                # Duration is specified, the filter will return only those data items that fall
                # within Duration before now.
                StructField(
                    "valueDuration",
                    DurationSchema.get_schema(
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
