from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ElementDefinition_ConstraintSchema:
    """
    Captures constraints on each element within the resource, profile, or
    extension.
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
        Captures constraints on each element within the resource, profile, or
        extension.


        key: Allows identification of which elements have their cardinalities impacted by
            the constraint.  Will not be referenced for constraints that do not affect
            cardinality.

        requirements: Description of why this constraint is necessary or appropriate.

        severity: Identifies the impact constraint violation has on the conformance of the
            instance.

        human: Text that can be used to describe the constraint in messages identifying that
            the constraint has been violated.

        expression: A [FHIRPath](http://hl7.org/fluentpath) expression of constraint that can be
            executed to see if this constraint is met.

        xpath: An XPath expression of constraint that can be executed to see if this
            constraint is met.

        source: A reference to the original source of the constraint, for traceability
            purposes.

        """
        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition_Constraint") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ElementDefinition_Constraint"
        ]
        schema = StructType(
            [
                # Allows identification of which elements have their cardinalities impacted by
                # the constraint.  Will not be referenced for constraints that do not affect
                # cardinality.
                StructField("key", StringType(), True),
                # Description of why this constraint is necessary or appropriate.
                StructField("requirements", StringType(), True),
                # Identifies the impact constraint violation has on the conformance of the
                # instance.
                StructField("severity", StringType(), True),
                # Text that can be used to describe the constraint in messages identifying that
                # the constraint has been violated.
                StructField("human", StringType(), True),
                # A [FHIRPath](http://hl7.org/fluentpath) expression of constraint that can be
                # executed to see if this constraint is met.
                StructField("expression", StringType(), True),
                # An XPath expression of constraint that can be executed to see if this
                # constraint is met.
                StructField("xpath", StringType(), True),
                # A reference to the original source of the constraint, for traceability
                # purposes.
                StructField("source", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
