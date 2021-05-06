from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class StructureDefinition_MappingSchema:
    """
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
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
        A definition of a FHIR structure. This resource is used to describe the
        underlying resources, data types defined in FHIR, and also for describing
        extensions and constraints on resources and data types.


        identity: An Internal id that is used to identify this mapping set when specific
            mappings are made.

        uri: An absolute URI that identifies the specification that this mapping is
            expressed to.

        name: A name for the specification that is being mapped to.

        comment: Comments about this mapping, including version notes, issues, scope
            limitations, and other important notes for usage.

        """
        if (
            max_recursion_limit
            and nesting_list.count("StructureDefinition_Mapping") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "StructureDefinition_Mapping"
        ]
        schema = StructType(
            [
                # An Internal id that is used to identify this mapping set when specific
                # mappings are made.
                StructField("identity", StringType(), True),
                # An absolute URI that identifies the specification that this mapping is
                # expressed to.
                StructField("uri", StringType(), True),
                # A name for the specification that is being mapped to.
                StructField("name", StringType(), True),
                # Comments about this mapping, including version notes, issues, scope
                # limitations, and other important notes for usage.
                StructField("comment", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
