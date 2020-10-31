from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ElementDefinition_Slicing:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Captures constraints on each element within the resource, profile, or
        extension.


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

        discriminator: Designates which child elements are used to discriminate between the slices
            when processing an instance. If one or more discriminators are provided, the
            value of the child elements in the instance data SHALL completely distinguish
            which slice the element in the resource matches based on the allowed values
            for those elements in each of the slices.

        description: A human-readable text description of how the slicing works. If there is no
            discriminator, this is required to be present to provide whatever information
            is possible about how the slices can be differentiated.

        ordered: If the matching elements have to occur in the same order as defined in the
            profile.

        rules: Whether additional slices are allowed or not. When the slices are ordered,
            profile authors can also say that additional slices are only allowed at the
            end.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.elementdefinition_discriminator import ElementDefinition_Discriminator
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
                # Designates which child elements are used to discriminate between the slices
                # when processing an instance. If one or more discriminators are provided, the
                # value of the child elements in the instance data SHALL completely distinguish
                # which slice the element in the resource matches based on the allowed values
                # for those elements in each of the slices.
                StructField(
                    "discriminator",
                    ArrayType(
                        ElementDefinition_Discriminator.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A human-readable text description of how the slicing works. If there is no
                # discriminator, this is required to be present to provide whatever information
                # is possible about how the slices can be differentiated.
                StructField("description", StringType(), True),
                # If the matching elements have to occur in the same order as defined in the
                # profile.
                StructField("ordered", BooleanType(), True),
                # Whether additional slices are allowed or not. When the slices are ordered,
                # profile authors can also say that additional slices are only allowed at the
                # end.
                StructField("rules", StringType(), True),
            ]
        )
        return schema
