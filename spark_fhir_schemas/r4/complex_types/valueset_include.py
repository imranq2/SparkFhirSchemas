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
class ValueSet_IncludeSchema:
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
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
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

        system: An absolute URI which is the code system from which the selected codes come
            from.

        version: The version of the code system that the codes are selected from, or the
            special version '*' for all versions.

        concept: Specifies a concept to be included or excluded.

        filter: Select concepts by specify a matching criterion based on the properties
            (including relationships) defined by the system, or on filters defined by the
            system. If multiple filters are specified, they SHALL all be true.

        valueSet: Selects the concepts found in this value set (based on its value set
            definition). This is an absolute URI that is a reference to ValueSet.url.  If
            multiple value sets are specified this includes the union of the contents of
            all of the referenced value sets.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.complex_types.valueset_concept import ValueSet_ConceptSchema
        from spark_fhir_schemas.r4.complex_types.valueset_filter import ValueSet_FilterSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Include") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Include"]
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
                # An absolute URI which is the code system from which the selected codes come
                # from.
                StructField(
                    "system",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The version of the code system that the codes are selected from, or the
                # special version '*' for all versions.
                StructField("version", StringType(), True),
                # Specifies a concept to be included or excluded.
                StructField(
                    "concept",
                    ArrayType(
                        ValueSet_ConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Select concepts by specify a matching criterion based on the properties
                # (including relationships) defined by the system, or on filters defined by the
                # system. If multiple filters are specified, they SHALL all be true.
                StructField(
                    "filter",
                    ArrayType(
                        ValueSet_FilterSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Selects the concepts found in this value set (based on its value set
                # definition). This is an absolute URI that is a reference to ValueSet.url.  If
                # multiple value sets are specified this includes the union of the contents of
                # all of the referenced value sets.
                StructField(
                    "valueSet",
                    ArrayType(
                        canonicalSchema.get_schema(
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
