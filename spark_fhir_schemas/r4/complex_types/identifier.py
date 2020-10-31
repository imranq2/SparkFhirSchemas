from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Identifier:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An identifier - identifies some entity uniquely and unambiguously. Typically
        this is used for business identifiers.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        use: The purpose of this identifier.

        type: A coded type for the identifier that can be used to determine which identifier
            to use for a specific purpose.

        system: Establishes the namespace for the value - that is, a URL that describes a set
            values that are unique.

        value: The portion of the identifier typically relevant to the user and which is
            unique within the context of the system.

        period: Time period during which identifier is/was valid for use.

        assigner: Organization that issued/manages the identifier.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # The purpose of this identifier.
                StructField("use", StringType(), True),
                # A coded type for the identifier that can be used to determine which identifier
                # to use for a specific purpose.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Establishes the namespace for the value - that is, a URL that describes a set
                # values that are unique.
                StructField(
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                # The portion of the identifier typically relevant to the user and which is
                # unique within the context of the system.
                StructField("value", StringType(), True),
                # Time period during which identifier is/was valid for use.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # Organization that issued/manages the identifier.
                StructField(
                    "assigner", Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
