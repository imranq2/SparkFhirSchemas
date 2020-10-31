from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImplementationGuide_Definition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.


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

        grouping: A logical group of resources. Logical groups can be used when building pages.

        resource: A resource that is part of the implementation guide. Conformance resources
            (value set, structure definition, capability statements etc.) are obvious
            candidates for inclusion, but any kind of resource can be included as an
            example resource.

        page: A page / section in the implementation guide. The root page is the
            implementation guide home page.

        parameter: Defines how IG is built by tools.

        template: A template for building resources.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.implementationguide_grouping import ImplementationGuide_Grouping
        from spark_fhir_schemas.r4.complex_types.implementationguide_resource import ImplementationGuide_Resource
        from spark_fhir_schemas.r4.complex_types.implementationguide_page import ImplementationGuide_Page
        from spark_fhir_schemas.r4.complex_types.implementationguide_parameter import ImplementationGuide_Parameter
        from spark_fhir_schemas.r4.complex_types.implementationguide_template import ImplementationGuide_Template
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
                # A logical group of resources. Logical groups can be used when building pages.
                StructField(
                    "grouping",
                    ArrayType(
                        ImplementationGuide_Grouping.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A resource that is part of the implementation guide. Conformance resources
                # (value set, structure definition, capability statements etc.) are obvious
                # candidates for inclusion, but any kind of resource can be included as an
                # example resource.
                StructField(
                    "resource",
                    ArrayType(
                        ImplementationGuide_Resource.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A page / section in the implementation guide. The root page is the
                # implementation guide home page.
                StructField(
                    "page",
                    ImplementationGuide_Page.get_schema(recursion_depth + 1),
                    True
                ),
                # Defines how IG is built by tools.
                StructField(
                    "parameter",
                    ArrayType(
                        ImplementationGuide_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A template for building resources.
                StructField(
                    "template",
                    ArrayType(
                        ImplementationGuide_Template.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
