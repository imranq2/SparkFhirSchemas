from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ElementDefinition_SlicingSchema:
    """
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.complex_types.elementdefinition_discriminator import ElementDefinition_DiscriminatorSchema
        if recursion_list.count(
            "ElementDefinition_Slicing"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + [
            "ElementDefinition_Slicing"
        ]
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

                # >>> Hiding extension Extension

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

                # >>> Hiding modifierExtension Extension

                # Designates which child elements are used to discriminate between the slices
                # when processing an instance. If one or more discriminators are provided, the
                # value of the child elements in the instance data SHALL completely distinguish
                # which slice the element in the resource matches based on the allowed values
                # for those elements in each of the slices.
                StructField(
                    "discriminator",
                    ArrayType(
                        ElementDefinition_DiscriminatorSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
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
