from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OperationOutcome_IssueSchema:
    """
    A collection of error, warning, or information messages that result from a
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
        A collection of error, warning, or information messages that result from a
        system action.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        severity: Indicates whether the issue indicates a variation from successful processing.

        code: Describes the type of the issue. The system that creates an OperationOutcome
            SHALL choose the most applicable code from the IssueType value set, and may
            additional provide its own code for the error in the details element.

        details: Additional details about the error. This may be a text description of the
            error or a system code that identifies the error.

        diagnostics: Additional diagnostic information about the issue.

        location: This element is deprecated because it is XML specific. It is replaced by
            issue.expression, which is format independent, and simpler to parse.

            For resource issues, this will be a simple XPath limited to element names,
            repetition indicators and the default child accessor that identifies one of
            the elements in the resource that caused this issue to be raised.  For HTTP
            errors, will be "http." + the parameter name.

        expression: A [simple subset of FHIRPath](fhirpath.html#simple) limited to element names,
            repetition indicators and the default child accessor that identifies one of
            the elements in the resource that caused this issue to be raised.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit and
            nesting_list.count("OperationOutcome_Issue") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["OperationOutcome_Issue"]
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
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Indicates whether the issue indicates a variation from successful processing.
                StructField("severity", StringType(), True),
                # Describes the type of the issue. The system that creates an OperationOutcome
                # SHALL choose the most applicable code from the IssueType value set, and may
                # additional provide its own code for the error in the details element.
                StructField("code", StringType(), True),
                # Additional details about the error. This may be a text description of the
                # error or a system code that identifies the error.
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
                # Additional diagnostic information about the issue.
                StructField("diagnostics", StringType(), True),
                # This element is deprecated because it is XML specific. It is replaced by
                # issue.expression, which is format independent, and simpler to parse.
                #
                # For resource issues, this will be a simple XPath limited to element names,
                # repetition indicators and the default child accessor that identifies one of
                # the elements in the resource that caused this issue to be raised.  For HTTP
                # errors, will be "http." + the parameter name.
                StructField("location", ArrayType(StringType()), True),
                # A [simple subset of FHIRPath](fhirpath.html#simple) limited to element names,
                # repetition indicators and the default child accessor that identifies one of
                # the elements in the resource that caused this issue to be raised.
                StructField("expression", ArrayType(StringType()), True),
            ]
        )
        if not include_extension:
            schema.fields = [c for c in schema.fields if c.name != "extension"]
        return schema
