from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ParameterDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The parameters to the module. This collection specifies both the input and
        output parameters. Input parameters are provided by the caller as part of the
        $evaluate operation. Output parameters are included in the GuidanceResponse.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        name: The name of the parameter used to allow access to the value of the parameter
            in evaluation contexts.

        use: Whether the parameter is input or output for the module.

        min: The minimum number of times this parameter SHALL appear in the request or
            response.

        max: The maximum number of times this element is permitted to appear in the request
            or response.

        documentation: A brief discussion of what the parameter is for and how it is used by the
            module.

        type: The type of the parameter.

        profile: If specified, this indicates a profile that the input data must conform to, or
            that the output data will conform to.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
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
                # The name of the parameter used to allow access to the value of the parameter
                # in evaluation contexts.
                StructField(
                    "name", code.get_schema(recursion_depth + 1), True
                ),
                # Whether the parameter is input or output for the module.
                StructField("use", code.get_schema(recursion_depth + 1), True),
                # The minimum number of times this parameter SHALL appear in the request or
                # response.
                StructField(
                    "min", integer.get_schema(recursion_depth + 1), True
                ),
                # The maximum number of times this element is permitted to appear in the request
                # or response.
                StructField("max", StringType(), True),
                # A brief discussion of what the parameter is for and how it is used by the
                # module.
                StructField("documentation", StringType(), True),
                # The type of the parameter.
                StructField(
                    "type", code.get_schema(recursion_depth + 1), True
                ),
                # If specified, this indicates a profile that the input data must conform to, or
                # that the output data will conform to.
                StructField(
                    "profile", canonical.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
