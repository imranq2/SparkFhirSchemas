from typing import List
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CodeSystem_PropertySchema:
    """
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and optionally
    define a part or all of its content.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        The CodeSystem resource is used to declare the existence of and describe a
        code system or code system supplement and its key properties, and optionally
        define a part or all of its content.


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

        code: A code that is used to identify the property. The code is used internally (in
            CodeSystem.concept.property.code) and also externally, such as in property
            filters.

        uri: Reference to the formal meaning of the property. One possible source of
            meaning is the [Concept Properties](codesystem-concept-properties.html) code
            system.

        description: A description of the property- why it is defined, and how its value might be
            used.

        type: The type of the property value. Properties of type "code" contain a code
            defined by the code system (e.g. a reference to another defined concept).

        """
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        if recursion_list.count(
            "CodeSystem_Property"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["CodeSystem_Property"]
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

                # A code that is used to identify the property. The code is used internally (in
                # CodeSystem.concept.property.code) and also externally, such as in property
                # filters.
                StructField(
                    "code",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Reference to the formal meaning of the property. One possible source of
                # meaning is the [Concept Properties](codesystem-concept-properties.html) code
                # system.
                StructField(
                    "uri",
                    uriSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A description of the property- why it is defined, and how its value might be
                # used.
                StructField("description", StringType(), True),
                # The type of the property value. Properties of type "code" contain a code
                # defined by the code system (e.g. a reference to another defined concept).
                StructField("type", StringType(), True),
            ]
        )
        return schema
