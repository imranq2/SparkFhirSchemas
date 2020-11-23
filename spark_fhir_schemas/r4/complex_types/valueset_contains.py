from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ValueSet_ContainsSchema:
    """
    A ValueSet resource instance specifies a set of codes drawn from one or more
    code systems, intended for use in a particular context. Value sets link
    between [[[CodeSystem]]] definitions and their use in [coded
    elements](terminologies.html).
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
        """
        A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        system: An absolute URI which is the code system in which the code for this item in
            the expansion is defined.

        abstract: If true, this entry is included in the expansion for navigational purposes,
            and the user cannot select the code directly as a proper value.

        inactive: If the concept is inactive in the code system that defines it. Inactive codes
            are those that are no longer to be used, but are maintained by the code system
            for understanding legacy data. It might not be known or specified whether an
            concept is inactive (and it may depend on the context of use).

        version: The version of the code system from this code was taken. Note that a well-
            maintained code system does not need the version reported, because the meaning
            of codes is consistent across versions. However this cannot consistently be
            assured, and when the meaning is not guaranteed to be consistent, the version
            SHOULD be exchanged.

        code: The code for this item in the expansion hierarchy. If this code is missing the
            entry in the hierarchy is a place holder (abstract) and does not represent a
            valid code in the value set.

        display: The recommended display for this item in the expansion.

        designation: Additional representations for this item - other languages, aliases,
            specialized purposes, used for particular purposes, etc. These are relevant
            when the conditions of the expansion do not fix to a single correct
            representation.

        contains: Other codes and entries contained under this entry in the hierarchy.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.valueset_designation import ValueSet_DesignationSchema
        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Contains") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Contains"]
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
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # An absolute URI which is the code system in which the code for this item in
                # the expansion is defined.
                StructField(
                    "system",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # If true, this entry is included in the expansion for navigational purposes,
                # and the user cannot select the code directly as a proper value.
                StructField("abstract", BooleanType(), True),
                # If the concept is inactive in the code system that defines it. Inactive codes
                # are those that are no longer to be used, but are maintained by the code system
                # for understanding legacy data. It might not be known or specified whether an
                # concept is inactive (and it may depend on the context of use).
                StructField("inactive", BooleanType(), True),
                # The version of the code system from this code was taken. Note that a well-
                # maintained code system does not need the version reported, because the meaning
                # of codes is consistent across versions. However this cannot consistently be
                # assured, and when the meaning is not guaranteed to be consistent, the version
                # SHOULD be exchanged.
                StructField("version", StringType(), True),
                # The code for this item in the expansion hierarchy. If this code is missing the
                # entry in the hierarchy is a place holder (abstract) and does not represent a
                # valid code in the value set.
                StructField(
                    "code",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The recommended display for this item in the expansion.
                StructField("display", StringType(), True),
                # Additional representations for this item - other languages, aliases,
                # specialized purposes, used for particular purposes, etc. These are relevant
                # when the conditions of the expansion do not fix to a single correct
                # representation.
                StructField(
                    "designation",
                    ArrayType(
                        ValueSet_DesignationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Other codes and entries contained under this entry in the hierarchy.
                StructField(
                    "contains",
                    ArrayType(
                        ValueSet_ContainsSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
