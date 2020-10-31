from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class StructureMap_Rule:
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

        name: Name of the rule for internal references.

        source: Source inputs to the mapping.

        target: Content to create because of this mapping rule.

        rule: Rules contained in this rule.

        dependent: Which other rules to apply in the context of this rule.

        documentation: Documentation for this instance of data.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.structuremap_source import StructureMap_Source
        from spark_fhir_schemas.r4.complex_types.structuremap_target import StructureMap_Target
        from spark_fhir_schemas.r4.complex_types.structuremap_dependent import StructureMap_Dependent
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
                # Name of the rule for internal references.
                StructField("name", id.get_schema(recursion_depth + 1), True),
                # Source inputs to the mapping.
                StructField(
                    "source",
                    ArrayType(
                        StructureMap_Source.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Content to create because of this mapping rule.
                StructField(
                    "target",
                    ArrayType(
                        StructureMap_Target.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Rules contained in this rule.
                StructField(
                    "rule",
                    ArrayType(
                        StructureMap_Rule.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Which other rules to apply in the context of this rule.
                StructField(
                    "dependent",
                    ArrayType(
                        StructureMap_Dependent.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Documentation for this instance of data.
                StructField("documentation", StringType(), True),
            ]
        )
        return schema
