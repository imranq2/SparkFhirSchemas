from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TriggerDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A description of a triggering event. Triggering events can be named events,
        data events, or periodic, as determined by the type element.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: The type of triggering event.

        name: A formal name for the event. This may be an absolute URI that identifies the
            event formally (e.g. from a trigger registry), or a simple relative URI that
            identifies the event in a local context.

        timingTiming: The timing of the event (if this is a periodic trigger).

        timingReference: The timing of the event (if this is a periodic trigger).

        timingDate: The timing of the event (if this is a periodic trigger).

        timingDateTime: The timing of the event (if this is a periodic trigger).

        data: The triggering data of the event (if this is a data trigger). If more than one
            data is requirement is specified, then all the data requirements must be true.

        condition: A boolean-valued expression that is evaluated in the context of the container
            of the trigger definition and returns whether or not the trigger fires.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        from spark_fhir_schemas.r4.complex_types.expression import Expression
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
                # The type of triggering event.
                StructField("type", StringType(), True),
                # A formal name for the event. This may be an absolute URI that identifies the
                # event formally (e.g. from a trigger registry), or a simple relative URI that
                # identifies the event in a local context.
                StructField("name", StringType(), True),
                # The timing of the event (if this is a periodic trigger).
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # The timing of the event (if this is a periodic trigger).
                StructField(
                    "timingReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The timing of the event (if this is a periodic trigger).
                StructField("timingDate", StringType(), True),
                # The timing of the event (if this is a periodic trigger).
                StructField("timingDateTime", StringType(), True),
                # The triggering data of the event (if this is a data trigger). If more than one
                # data is requirement is specified, then all the data requirements must be true.
                StructField(
                    "data",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
                # A boolean-valued expression that is evaluated in the context of the container
                # of the trigger definition and returns whether or not the trigger fires.
                StructField(
                    "condition", Expression.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
