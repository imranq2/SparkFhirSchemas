from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class GroupSchema:
    """
    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively and are not
    formally or legally recognized; i.e. a collection of entities that isn't an
    Organization.
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
        Represents a defined collection of entities that may be discussed or acted
        upon collectively but which are not expected to act collectively and are not
        formally or legally recognized; i.e. a collection of entities that isn't an
        Organization.


        resourceType: This is a Group resource

        identifier: A unique business identifier for this group.

        active: Indicates whether the record for the group is available for use or is merely
            being retained for historical purposes.

        type: Identifies the broad classification of the kind of resources the group
            includes.

        actual: If true, indicates that the resource refers to a specific group of real
            individuals.  If false, the group defines a set of intended individuals.

        code: Provides a specific type of resource the group includes; e.g. "cow",
            "syringe", etc.

        name: A label assigned to the group for human identification and communication.

        quantity: A count of the number of resource instances that are part of the group.

        characteristic: Identifies the traits shared by members of the group.

        member: Identifies the resource instances that are members of the group.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.group_characteristic import Group_CharacteristicSchema
        from spark_fhir_schemas.stu3.complex_types.group_member import Group_MemberSchema
        if (
            max_recursion_limit
            and nesting_list.count("Group") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Group"]
        schema = StructType(
            [
                # This is a Group resource
                StructField("resourceType", StringType(), True),
                # A unique business identifier for this group.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Indicates whether the record for the group is available for use or is merely
                # being retained for historical purposes.
                StructField("active", BooleanType(), True),
                # Identifies the broad classification of the kind of resources the group
                # includes.
                StructField("type", StringType(), True),
                # If true, indicates that the resource refers to a specific group of real
                # individuals.  If false, the group defines a set of intended individuals.
                StructField("actual", BooleanType(), True),
                # Provides a specific type of resource the group includes; e.g. "cow",
                # "syringe", etc.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A label assigned to the group for human identification and communication.
                StructField("name", StringType(), True),
                # A count of the number of resource instances that are part of the group.
                StructField("quantity", IntegerType(), True),
                # Identifies the traits shared by members of the group.
                StructField(
                    "characteristic",
                    ArrayType(
                        Group_CharacteristicSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Identifies the resource instances that are members of the group.
                StructField(
                    "member",
                    ArrayType(
                        Group_MemberSchema.get_schema(
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
