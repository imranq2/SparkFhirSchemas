from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ConceptMap_Unmapped:
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

        mode: Defines which action to take if there is no match for the source concept in
            the target system designated for the group. One of 3 actions are possible: use
            the unmapped code (this is useful when doing a mapping between versions, and
            only a few codes have changed), use a fixed code (a default code), or
            alternatively, a reference to a different concept map can be provided (by
            canonical URL).

        code: The fixed code to use when the mode = 'fixed'  - all unmapped codes are mapped
            to a single fixed code.

        display: The display for the code. The display is only provided to help editors when
            editing the concept map.

        url: The canonical reference to an additional ConceptMap resource instance to use
            for mapping if this ConceptMap resource contains no matching mapping for the
            source concept.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
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
                # Defines which action to take if there is no match for the source concept in
                # the target system designated for the group. One of 3 actions are possible: use
                # the unmapped code (this is useful when doing a mapping between versions, and
                # only a few codes have changed), use a fixed code (a default code), or
                # alternatively, a reference to a different concept map can be provided (by
                # canonical URL).
                StructField("mode", StringType(), True),
                # The fixed code to use when the mode = 'fixed'  - all unmapped codes are mapped
                # to a single fixed code.
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                # The display for the code. The display is only provided to help editors when
                # editing the concept map.
                StructField("display", StringType(), True),
                # The canonical reference to an additional ConceptMap resource instance to use
                # for mapping if this ConceptMap resource contains no matching mapping for the
                # source concept.
                StructField(
                    "url", canonical.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
