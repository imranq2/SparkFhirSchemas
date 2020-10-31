from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet_Expansion:
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

        identifier: An identifier that uniquely identifies this expansion of the valueset, based
            on a unique combination of the provided parameters, the system default
            parameters, and the underlying system code system versions etc. Systems may
            re-use the same identifier as long as those factors remain the same, and the
            expansion is the same, but are not required to do so. This is a business
            identifier.

        timestamp: The time at which the expansion was produced by the expanding system.

        total: The total number of concepts in the expansion. If the number of concept nodes
            in this resource is less than the stated number, then the server can return
            more using the offset parameter.

        offset: If paging is being used, the offset at which this resource starts.  I.e. this
            resource is a partial view into the expansion. If paging is not being used,
            this element SHALL NOT be present.

        parameter: A parameter that controlled the expansion process. These parameters may be
            used by users of expanded value sets to check whether the expansion is
            suitable for a particular purpose, or to pick the correct expansion.

        contains: The codes that are contained in the value set expansion.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.valueset_parameter import ValueSet_Parameter
        from spark_fhir_schemas.r4.complex_types.valueset_contains import ValueSet_Contains
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
                # An identifier that uniquely identifies this expansion of the valueset, based
                # on a unique combination of the provided parameters, the system default
                # parameters, and the underlying system code system versions etc. Systems may
                # re-use the same identifier as long as those factors remain the same, and the
                # expansion is the same, but are not required to do so. This is a business
                # identifier.
                StructField(
                    "identifier", uri.get_schema(recursion_depth + 1), True
                ),
                # The time at which the expansion was produced by the expanding system.
                StructField(
                    "timestamp", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The total number of concepts in the expansion. If the number of concept nodes
                # in this resource is less than the stated number, then the server can return
                # more using the offset parameter.
                StructField(
                    "total", integer.get_schema(recursion_depth + 1), True
                ),
                # If paging is being used, the offset at which this resource starts.  I.e. this
                # resource is a partial view into the expansion. If paging is not being used,
                # this element SHALL NOT be present.
                StructField(
                    "offset", integer.get_schema(recursion_depth + 1), True
                ),
                # A parameter that controlled the expansion process. These parameters may be
                # used by users of expanded value sets to check whether the expansion is
                # suitable for a particular purpose, or to pick the correct expansion.
                StructField(
                    "parameter",
                    ArrayType(
                        ValueSet_Parameter.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The codes that are contained in the value set expansion.
                StructField(
                    "contains",
                    ArrayType(
                        ValueSet_Contains.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
