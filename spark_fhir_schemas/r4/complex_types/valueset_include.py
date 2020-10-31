from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet_Include:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.valueset_concept import ValueSet_Concept
        from spark_fhir_schemas.r4.complex_types.valueset_filter import ValueSet_Filter
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # An absolute URI which is the code system from which the selected codes come
                # from.
                StructField(
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                # The version of the code system that the codes are selected from, or the
                # special version '*' for all versions.
                StructField("version", StringType(), True),
                # Specifies a concept to be included or excluded.
                StructField(
                    "concept",
                    ArrayType(
                        ValueSet_Concept.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Select concepts by specify a matching criterion based on the properties
                # (including relationships) defined by the system, or on filters defined by the
                # system. If multiple filters are specified, they SHALL all be true.
                StructField(
                    "filter",
                    ArrayType(ValueSet_Filter.get_schema(recursion_depth + 1)),
                    True
                ),
                # Selects the concepts found in this value set (based on its value set
                # definition). This is an absolute URI that is a reference to ValueSet.url.  If
                # multiple value sets are specified this includes the union of the contents of
                # all of the referenced value sets.
                StructField(
                    "valueSet",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
