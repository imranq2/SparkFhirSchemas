from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ConceptMap_Group:
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

        source: An absolute URI that identifies the source system where the concepts to be
            mapped are defined.

        sourceVersion: The specific version of the code system, as determined by the code system
            authority.

        target: An absolute URI that identifies the target system that the concepts will be
            mapped to.

        targetVersion: The specific version of the code system, as determined by the code system
            authority.

        element: Mappings for an individual concept in the source to one or more concepts in
            the target.

        unmapped: What to do when there is no mapping for the source concept. "Unmapped" does
            not include codes that are unmatched, and the unmapped element is ignored in a
            code is specified to have equivalence = unmatched.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.conceptmap_element import ConceptMap_Element
        from spark_fhir_schemas.r4.complex_types.conceptmap_unmapped import ConceptMap_Unmapped
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
                # An absolute URI that identifies the source system where the concepts to be
                # mapped are defined.
                StructField(
                    "source", uri.get_schema(recursion_depth + 1), True
                ),
                # The specific version of the code system, as determined by the code system
                # authority.
                StructField("sourceVersion", StringType(), True),
                # An absolute URI that identifies the target system that the concepts will be
                # mapped to.
                StructField(
                    "target", uri.get_schema(recursion_depth + 1), True
                ),
                # The specific version of the code system, as determined by the code system
                # authority.
                StructField("targetVersion", StringType(), True),
                # Mappings for an individual concept in the source to one or more concepts in
                # the target.
                StructField(
                    "element",
                    ArrayType(
                        ConceptMap_Element.get_schema(recursion_depth + 1)
                    ), True
                ),
                # What to do when there is no mapping for the source concept. "Unmapped" does
                # not include codes that are unmatched, and the unmapped element is ignored in a
                # code is specified to have equivalence = unmatched.
                StructField(
                    "unmapped",
                    ConceptMap_Unmapped.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
