from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OperationDefinition_ParameterSchema:
    """
    A formal computable definition of an operation (on the RESTful interface) or a
    named query (using the search interaction).
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
        A formal computable definition of an operation (on the RESTful interface) or a
        named query (using the search interaction).


        name: The name of used to identify the parameter.

        use: Whether this is an input or an output parameter.

        min: The minimum number of times this parameter SHALL appear in the request or
            response.

        max: The maximum number of times this element is permitted to appear in the request
            or response.

        documentation: Describes the meaning or use of this parameter.

        type: The type for this parameter.

        searchType: How the parameter is understood as a search parameter. This is only used if
            the parameter type is 'string'.

        profile: A profile the specifies the rules that this parameter must conform to.

        binding: Binds to a value set if this parameter is coded (code, Coding,
            CodeableConcept).

        part: The parts of a nested Parameter.

        """
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.operationdefinition_binding import OperationDefinition_BindingSchema
        if (
            max_recursion_limit
            and nesting_list.count("OperationDefinition_Parameter") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "OperationDefinition_Parameter"
        ]
        schema = StructType(
            [
                # The name of used to identify the parameter.
                StructField("name", StringType(), True),
                # Whether this is an input or an output parameter.
                StructField("use", StringType(), True),
                # The minimum number of times this parameter SHALL appear in the request or
                # response.
                StructField("min", IntegerType(), True),
                # The maximum number of times this element is permitted to appear in the request
                # or response.
                StructField("max", StringType(), True),
                # Describes the meaning or use of this parameter.
                StructField("documentation", StringType(), True),
                # The type for this parameter.
                StructField("type", StringType(), True),
                # How the parameter is understood as a search parameter. This is only used if
                # the parameter type is 'string'.
                StructField("searchType", StringType(), True),
                # A profile the specifies the rules that this parameter must conform to.
                StructField(
                    "profile",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Binds to a value set if this parameter is coded (code, Coding,
                # CodeableConcept).
                StructField(
                    "binding",
                    OperationDefinition_BindingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The parts of a nested Parameter.
                StructField(
                    "part",
                    ArrayType(
                        OperationDefinition_ParameterSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
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
