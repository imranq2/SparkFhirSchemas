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
class Timing_RepeatSchema:
    """
    Specifies an event that may occur multiple times. Timing schedules are used to
    record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
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
        Specifies an event that may occur multiple times. Timing schedules are used to
        record when things are planned, expected or requested to occur. The most
        common usage is in dosage instructions for medications. They are also used
        when planning care of various kinds, and may be used for reporting the
        schedule to which past regular activities were carried out.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        boundsDuration: Either a duration for the length of the timing schedule, a range of possible
            length, or outer bounds for start and/or end limits of the timing schedule.

        boundsRange: Either a duration for the length of the timing schedule, a range of possible
            length, or outer bounds for start and/or end limits of the timing schedule.

        boundsPeriod: Either a duration for the length of the timing schedule, a range of possible
            length, or outer bounds for start and/or end limits of the timing schedule.

        count: A total count of the desired number of repetitions across the duration of the
            entire timing specification. If countMax is present, this element indicates
            the lower bound of the allowed range of count values.

        countMax: If present, indicates that the count is a range - so to perform the action
            between [count] and [countMax] times.

        duration: How long this thing happens for when it happens. If durationMax is present,
            this element indicates the lower bound of the allowed range of the duration.

        durationMax: If present, indicates that the duration is a range - so to perform the action
            between [duration] and [durationMax] time length.

        durationUnit: The units of time for the duration, in UCUM units.

        frequency: The number of times to repeat the action within the specified period. If
            frequencyMax is present, this element indicates the lower bound of the allowed
            range of the frequency.

        frequencyMax: If present, indicates that the frequency is a range - so to repeat between
            [frequency] and [frequencyMax] times within the period or period range.

        period: Indicates the duration of time over which repetitions are to occur; e.g. to
            express "3 times per day", 3 would be the frequency and "1 day" would be the
            period. If periodMax is present, this element indicates the lower bound of the
            allowed range of the period length.

        periodMax: If present, indicates that the period is a range from [period] to [periodMax],
            allowing expressing concepts such as "do this once every 3-5 days.

        periodUnit: The units of time for the period in UCUM units.

        dayOfWeek: If one or more days of week is provided, then the action happens only on the
            specified day(s).

        timeOfDay: Specified time of day for action to take place.

        when: An approximate time period during the day, potentially linked to an event of
            daily living that indicates when the action should occur.

        offset: The number of minutes from the event. If the event code does not indicate
            whether the minutes is before or after the event, then the offset is assumed
            to be after the event.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveIntSchema
        from spark_fhir_schemas.r4.simple_types.decimal import decimalSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.simple_types.time import timeSchema
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedIntSchema
        if (
            max_recursion_limit
            and nesting_list.count("Timing_Repeat") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Timing_Repeat"]
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
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Either a duration for the length of the timing schedule, a range of possible
                # length, or outer bounds for start and/or end limits of the timing schedule.
                StructField(
                    "boundsDuration",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Either a duration for the length of the timing schedule, a range of possible
                # length, or outer bounds for start and/or end limits of the timing schedule.
                StructField(
                    "boundsRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Either a duration for the length of the timing schedule, a range of possible
                # length, or outer bounds for start and/or end limits of the timing schedule.
                StructField(
                    "boundsPeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A total count of the desired number of repetitions across the duration of the
                # entire timing specification. If countMax is present, this element indicates
                # the lower bound of the allowed range of count values.
                StructField(
                    "count",
                    positiveIntSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # If present, indicates that the count is a range - so to perform the action
                # between [count] and [countMax] times.
                StructField(
                    "countMax",
                    positiveIntSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # How long this thing happens for when it happens. If durationMax is present,
                # this element indicates the lower bound of the allowed range of the duration.
                StructField(
                    "duration",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # If present, indicates that the duration is a range - so to perform the action
                # between [duration] and [durationMax] time length.
                StructField(
                    "durationMax",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The units of time for the duration, in UCUM units.
                StructField("durationUnit", StringType(), True),
                # The number of times to repeat the action within the specified period. If
                # frequencyMax is present, this element indicates the lower bound of the allowed
                # range of the frequency.
                StructField(
                    "frequency",
                    positiveIntSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # If present, indicates that the frequency is a range - so to repeat between
                # [frequency] and [frequencyMax] times within the period or period range.
                StructField(
                    "frequencyMax",
                    positiveIntSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Indicates the duration of time over which repetitions are to occur; e.g. to
                # express "3 times per day", 3 would be the frequency and "1 day" would be the
                # period. If periodMax is present, this element indicates the lower bound of the
                # allowed range of the period length.
                StructField(
                    "period",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # If present, indicates that the period is a range from [period] to [periodMax],
                # allowing expressing concepts such as "do this once every 3-5 days.
                StructField(
                    "periodMax",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The units of time for the period in UCUM units.
                StructField("periodUnit", StringType(), True),
                # If one or more days of week is provided, then the action happens only on the
                # specified day(s).
                StructField(
                    "dayOfWeek",
                    ArrayType(
                        codeSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Specified time of day for action to take place.
                StructField(
                    "timeOfDay",
                    ArrayType(
                        timeSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # An approximate time period during the day, potentially linked to an event of
                # daily living that indicates when the action should occur.
                # The number of minutes from the event. If the event code does not indicate
                # whether the minutes is before or after the event, then the offset is assumed
                # to be after the event.
                StructField(
                    "offset",
                    unsignedIntSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
            ]
        )
        return schema
