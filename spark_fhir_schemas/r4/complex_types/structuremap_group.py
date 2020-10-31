from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class StructureMap_Group:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A Map of relationships between 2 structures that can be used to transform
        data.


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

        name: A unique name for the group for the convenience of human readers.

        extends: Another group that this group adds rules to.

        typeMode: If this is the default rule set to apply for the source type or this
            combination of types.

        documentation: Additional supporting documentation that explains the purpose of the group and
            the types of mappings within it.

        input: A name assigned to an instance of data. The instance must be provided when the
            mapping is invoked.

        rule: Transform Rule from source to target.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.structuremap_input import StructureMap_Input
        from spark_fhir_schemas.r4.complex_types.structuremap_rule import StructureMap_Rule
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
                # A unique name for the group for the convenience of human readers.
                StructField("name", id.get_schema(recursion_depth + 1), True),
                # Another group that this group adds rules to.
                StructField(
                    "extends", id.get_schema(recursion_depth + 1), True
                ),
                # If this is the default rule set to apply for the source type or this
                # combination of types.
                StructField("typeMode", StringType(), True),
                # Additional supporting documentation that explains the purpose of the group and
                # the types of mappings within it.
                StructField("documentation", StringType(), True),
                # A name assigned to an instance of data. The instance must be provided when the
                # mapping is invoked.
                StructField(
                    "input",
                    ArrayType(
                        StructureMap_Input.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Transform Rule from source to target.
                StructField(
                    "rule",
                    ArrayType(
                        StructureMap_Rule.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
