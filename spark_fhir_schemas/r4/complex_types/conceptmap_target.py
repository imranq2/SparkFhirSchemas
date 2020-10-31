from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ConceptMap_Target:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A statement of relationships from one set of concepts to one or more other
        concepts - either concepts in code systems, or data element/data element
        concepts, or classes in class models.


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

        code: Identity (code or path) or the element/item that the map refers to.

        display: The display for the code. The display is only provided to help editors when
            editing the concept map.

        equivalence: The equivalence between the source and target concepts (counting for the
            dependencies and products). The equivalence is read from target to source
            (e.g. the target is 'wider' than the source).

        comment: A description of status/issues in mapping that conveys additional information
            not represented in  the structured data.

        dependsOn: A set of additional dependencies for this mapping to hold. This mapping is
            only applicable if the specified element can be resolved, and it has the
            specified value.

        product: A set of additional outcomes from this mapping to other elements. To properly
            execute this mapping, the specified element must be mapped to some data
            element or source that is in context. The mapping may still be useful without
            a place for the additional data elements, but the equivalence cannot be relied
            on.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.conceptmap_dependson import ConceptMap_DependsOn
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
                # Identity (code or path) or the element/item that the map refers to.
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                # The display for the code. The display is only provided to help editors when
                # editing the concept map.
                StructField("display", StringType(), True),
                # The equivalence between the source and target concepts (counting for the
                # dependencies and products). The equivalence is read from target to source
                # (e.g. the target is 'wider' than the source).
                StructField("equivalence", StringType(), True),
                # A description of status/issues in mapping that conveys additional information
                # not represented in  the structured data.
                StructField("comment", StringType(), True),
                # A set of additional dependencies for this mapping to hold. This mapping is
                # only applicable if the specified element can be resolved, and it has the
                # specified value.
                StructField(
                    "dependsOn",
                    ArrayType(
                        ConceptMap_DependsOn.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A set of additional outcomes from this mapping to other elements. To properly
                # execute this mapping, the specified element must be mapped to some data
                # element or source that is in context. The mapping may still be useful without
                # a place for the additional data elements, but the equivalence cannot be relied
                # on.
                StructField(
                    "product",
                    ArrayType(
                        ConceptMap_DependsOn.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
