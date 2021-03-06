from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Communication_PayloadSchema:
    """
    An occurrence of information being transmitted; e.g. an alert that was sent to
    a responsible provider, a public health agency was notified about a reportable
    condition.
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
        An occurrence of information being transmitted; e.g. an alert that was sent to
        a responsible provider, a public health agency was notified about a reportable
        condition.


        contentString: A communicated content (or for multi-part communications, one portion of the
            communication).

        contentAttachment: A communicated content (or for multi-part communications, one portion of the
            communication).

        contentReference: A communicated content (or for multi-part communications, one portion of the
            communication).

        """
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        if (
            max_recursion_limit and
            nesting_list.count("Communication_Payload") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Communication_Payload"]
        schema = StructType(
            [
                # A communicated content (or for multi-part communications, one portion of the
                # communication).
                StructField("contentString", StringType(), True),
                # A communicated content (or for multi-part communications, one portion of the
                # communication).
                StructField(
                    "contentAttachment",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A communicated content (or for multi-part communications, one portion of the
                # communication).
                StructField(
                    "contentReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
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
