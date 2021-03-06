from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OperationOutcome_IssueSchema:
    """
    A collection of error, warning or information messages that result from a
    system action.
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
        A collection of error, warning or information messages that result from a
        system action.


        severity: Indicates whether the issue indicates a variation from successful processing.

        code: Describes the type of the issue. The system that creates an OperationOutcome
            SHALL choose the most applicable code from the IssueType value set, and may
            additional provide its own code for the error in the details element.

        details: Additional details about the error. This may be a text description of the
            error, or a system code that identifies the error.

        diagnostics: Additional diagnostic information about the issue.  Typically, this may be a
            description of how a value is erroneous, or a stack dump to help trace the
            issue.

        location: For resource issues, this will be a simple XPath limited to element names,
            repetition indicators and the default child access that identifies one of the
            elements in the resource that caused this issue to be raised.  For HTTP
            errors, will be "http." + the parameter name.

        expression: A simple FHIRPath limited to element names, repetition indicators and the
            default child access that identifies one of the elements in the resource that
            caused this issue to be raised.

        """
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit and
            nesting_list.count("OperationOutcome_Issue") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["OperationOutcome_Issue"]
        schema = StructType(
            [
                # Indicates whether the issue indicates a variation from successful processing.
                StructField("severity", StringType(), True),
                # Describes the type of the issue. The system that creates an OperationOutcome
                # SHALL choose the most applicable code from the IssueType value set, and may
                # additional provide its own code for the error in the details element.
                StructField("code", StringType(), True),
                # Additional details about the error. This may be a text description of the
                # error, or a system code that identifies the error.
                StructField(
                    "details",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Additional diagnostic information about the issue.  Typically, this may be a
                # description of how a value is erroneous, or a stack dump to help trace the
                # issue.
                StructField("diagnostics", StringType(), True),
                # For resource issues, this will be a simple XPath limited to element names,
                # repetition indicators and the default child access that identifies one of the
                # elements in the resource that caused this issue to be raised.  For HTTP
                # errors, will be "http." + the parameter name.
                # A simple FHIRPath limited to element names, repetition indicators and the
                # default child access that identifies one of the elements in the resource that
                # caused this issue to be raised.
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
