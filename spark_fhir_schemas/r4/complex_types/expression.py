from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Expression:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A expression that is evaluated in a specified context and returns a value. The
        context of use of the expression must specify the context in which the
        expression is evaluated, and how the result of the expression is used.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        description: A brief, natural language description of the condition that effectively
            communicates the intended semantics.

        name: A short name assigned to the expression to allow for multiple reuse of the
            expression in the context where it is defined.

        language: The media type of the language for the expression.

        expression: An expression in the specified language that returns a value.

        reference: A URI that defines where the expression is found.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.simple_types.uri import uri
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
                # A brief, natural language description of the condition that effectively
                # communicates the intended semantics.
                StructField("description", StringType(), True),
                # A short name assigned to the expression to allow for multiple reuse of the
                # expression in the context where it is defined.
                StructField("name", id.get_schema(recursion_depth + 1), True),
                # The media type of the language for the expression.
                StructField("language", StringType(), True),
                # An expression in the specified language that returns a value.
                StructField("expression", StringType(), True),
                # A URI that defines where the expression is found.
                StructField(
                    "reference", uri.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
