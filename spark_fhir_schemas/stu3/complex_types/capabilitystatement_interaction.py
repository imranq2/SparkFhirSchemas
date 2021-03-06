from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatement_InteractionSchema:
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR
    Server that may be used as a statement of actual server functionality or a
    statement of required or desired server implementation.
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
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server that may be used as a statement of actual server functionality or a
        statement of required or desired server implementation.


        code: Coded identifier of the operation, supported by the system resource.

        documentation: Guidance specific to the implementation of this operation, such as 'delete is
            a logical delete' or 'updates are only allowed with version id' or 'creates
            permitted from pre-authorized certificates only'.

        """
        if (
            max_recursion_limit
            and nesting_list.count("CapabilityStatement_Interaction") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "CapabilityStatement_Interaction"
        ]
        schema = StructType(
            [
                # Coded identifier of the operation, supported by the system resource.
                StructField("code", StringType(), True),
                # Guidance specific to the implementation of this operation, such as 'delete is
                # a logical delete' or 'updates are only allowed with version id' or 'creates
                # permitted from pre-authorized certificates only'.
                StructField("documentation", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
