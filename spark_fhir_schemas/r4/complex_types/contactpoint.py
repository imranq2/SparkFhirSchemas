from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ContactPoint:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Details for all kinds of technology mediated contact points for a person or
        organization, including telephone, email, etc.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        system: Telecommunications form for contact point - what communications system is
            required to make use of the contact.

        value: The actual contact point details, in a form that is meaningful to the
            designated communication system (i.e. phone number or email address).

        use: Identifies the purpose for the contact point.

        rank: Specifies a preferred order in which to use a set of contacts. ContactPoints
            with lower rank values are more preferred than those with higher rank values.

        period: Time period when the contact point was/is in use.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.period import Period
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
                # Telecommunications form for contact point - what communications system is
                # required to make use of the contact.
                StructField("system", StringType(), True),
                # The actual contact point details, in a form that is meaningful to the
                # designated communication system (i.e. phone number or email address).
                StructField("value", StringType(), True),
                # Identifies the purpose for the contact point.
                StructField("use", StringType(), True),
                # Specifies a preferred order in which to use a set of contacts. ContactPoints
                # with lower rank values are more preferred than those with higher rank values.
                StructField(
                    "rank", positiveInt.get_schema(recursion_depth + 1), True
                ),
                # Time period when the contact point was/is in use.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
