from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CodeSystem_ConceptSchema:
    """
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and optionally
    define a part or all of its content.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
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

        code: A code - a text symbol - that uniquely identifies the concept within the code
            system.

        display: A human readable string that is the recommended default way to present this
            concept to a user.

        definition: The formal definition of the concept. The code system resource does not make
            formal definitions required, because of the prevalence of legacy systems.
            However, they are highly recommended, as without them there is no formal
            meaning associated with the concept.

        designation: Additional representations for the concept - other languages, aliases,
            specialized purposes, used for particular purposes, etc.

        property: A property value for this concept.

        concept: Defines children of a concept to produce a hierarchy of concepts. The nature
            of the relationships is variable (is-a/contains/categorizes) - see
            hierarchyMeaning.

        """
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.codesystem_designation import CodeSystem_DesignationSchema
        from spark_fhir_schemas.r4.complex_types.codesystem_property1 import CodeSystem_Property1Schema
        if (
            max_recursion_limit
            and nesting_list.count("CodeSystem_Concept") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CodeSystem_Concept"]
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

                # A code - a text symbol - that uniquely identifies the concept within the code
                # system.
                StructField(
                    "code",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A human readable string that is the recommended default way to present this
                # concept to a user.
                StructField("display", StringType(), True),
                # The formal definition of the concept. The code system resource does not make
                # formal definitions required, because of the prevalence of legacy systems.
                # However, they are highly recommended, as without them there is no formal
                # meaning associated with the concept.
                StructField("definition", StringType(), True),
                # Additional representations for the concept - other languages, aliases,
                # specialized purposes, used for particular purposes, etc.
                StructField(
                    "designation",
                    ArrayType(
                        CodeSystem_DesignationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # A property value for this concept.
                StructField(
                    "property",
                    ArrayType(
                        CodeSystem_Property1Schema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Defines children of a concept to produce a hierarchy of concepts. The nature
                # of the relationships is variable (is-a/contains/categorizes) - see
                # hierarchyMeaning.
                StructField(
                    "concept",
                    ArrayType(
                        CodeSystem_ConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
