from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PractitionerRole_AvailableTime:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A specific set of Roles/Locations/specialties/services that a practitioner may
        perform at an organization for a period of time.


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

        daysOfWeek: Indicates which days of the week are available between the start and end
            Times.

        allDay: Is this always available? (hence times are irrelevant) e.g. 24 hour service.

        availableStartTime: The opening time of day. Note: If the AllDay flag is set, then this time is
            ignored.

        availableEndTime: The closing time of day. Note: If the AllDay flag is set, then this time is
            ignored.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.time import time
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Indicates which days of the week are available between the start and end
                # Times.
                StructField(
                    "daysOfWeek",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                # Is this always available? (hence times are irrelevant) e.g. 24 hour service.
                StructField("allDay", BooleanType(), True),
                # The opening time of day. Note: If the AllDay flag is set, then this time is
                # ignored.
                StructField(
                    "availableStartTime", time.get_schema(recursion_depth + 1),
                    True
                ),
                # The closing time of day. Note: If the AllDay flag is set, then this time is
                # ignored.
                StructField(
                    "availableEndTime", time.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
