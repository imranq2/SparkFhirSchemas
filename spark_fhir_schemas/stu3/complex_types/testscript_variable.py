from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class TestScript_VariableSchema:
    """
    A structured set of tests against a FHIR server implementation to determine
    compliance against the FHIR specification.
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
        A structured set of tests against a FHIR server implementation to determine
        compliance against the FHIR specification.


        name: Descriptive name for this variable.

        defaultValue: A default, hard-coded, or user-defined value for this variable.

        description: A free text natural language description of the variable and its purpose.

        expression: The fluentpath expression to evaluate against the fixture body. When variables
            are defined, only one of either expression, headerField or path must be
            specified.

        headerField: Will be used to grab the HTTP header field value from the headers that
            sourceId is pointing to.

        hint: Displayable text string with hint help information to the user when entering a
            default value.

        path: XPath or JSONPath to evaluate against the fixture body.  When variables are
            defined, only one of either expression, headerField or path must be specified.

        sourceId: Fixture to evaluate the XPath/JSONPath expression or the headerField  against
            within this variable.

        """
        if (
            max_recursion_limit and
            nesting_list.count("TestScript_Variable") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript_Variable"]
        schema = StructType(
            [
                # Descriptive name for this variable.
                StructField("name", StringType(), True),
                # A default, hard-coded, or user-defined value for this variable.
                StructField("defaultValue", StringType(), True),
                # A free text natural language description of the variable and its purpose.
                StructField("description", StringType(), True),
                # The fluentpath expression to evaluate against the fixture body. When variables
                # are defined, only one of either expression, headerField or path must be
                # specified.
                StructField("expression", StringType(), True),
                # Will be used to grab the HTTP header field value from the headers that
                # sourceId is pointing to.
                StructField("headerField", StringType(), True),
                # Displayable text string with hint help information to the user when entering a
                # default value.
                StructField("hint", StringType(), True),
                # XPath or JSONPath to evaluate against the fixture body.  When variables are
                # defined, only one of either expression, headerField or path must be specified.
                StructField("path", StringType(), True),
                # Fixture to evaluate the XPath/JSONPath expression or the headerField  against
                # within this variable.
                StructField("sourceId", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
