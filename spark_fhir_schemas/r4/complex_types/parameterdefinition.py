from typing import List
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ParameterDefinitionSchema:
    """
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of the
    $evaluate operation. Output parameters are included in the GuidanceResponse.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.simple_types.integer import integerSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        if recursion_list.count(
            "ParameterDefinition"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["ParameterDefinition"]
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

                # >>> Hiding extension Extension

                # The name of the parameter used to allow access to the value of the parameter
                # in evaluation contexts.
                StructField(
                    "name",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Whether the parameter is input or output for the module.
                StructField(
                    "use",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The minimum number of times this parameter SHALL appear in the request or
                # response.
                StructField(
                    "min",
                    integerSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The maximum number of times this element is permitted to appear in the request
                # or response.
                StructField("max", StringType(), True),
                # A brief discussion of what the parameter is for and how it is used by the
                # module.
                StructField("documentation", StringType(), True),
                # The type of the parameter.
                StructField(
                    "type",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # If specified, this indicates a profile that the input data must conform to, or
                # that the output data will conform to.
                StructField(
                    "profile",
                    canonicalSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
            ]
        )
        return schema
