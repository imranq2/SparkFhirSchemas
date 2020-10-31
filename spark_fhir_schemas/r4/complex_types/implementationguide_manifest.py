from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImplementationGuide_Manifest:
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

        rendering: A pointer to official web page, PDF or other rendering of the implementation
            guide.

        resource: A resource that is part of the implementation guide. Conformance resources
            (value set, structure definition, capability statements etc.) are obvious
            candidates for inclusion, but any kind of resource can be included as an
            example resource.

        page: Information about a page within the IG.

        image: Indicates a relative path to an image that exists within the IG.

        other: Indicates the relative path of an additional non-page, non-image file that is
            part of the IG - e.g. zip, jar and similar files that could be the target of a
            hyperlink in a derived IG.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.url import url
        from spark_fhir_schemas.r4.complex_types.implementationguide_resource1 import ImplementationGuide_Resource1
        from spark_fhir_schemas.r4.complex_types.implementationguide_page1 import ImplementationGuide_Page1
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
                # A pointer to official web page, PDF or other rendering of the implementation
                # guide.
                StructField(
                    "rendering", url.get_schema(recursion_depth + 1), True
                ),
                # A resource that is part of the implementation guide. Conformance resources
                # (value set, structure definition, capability statements etc.) are obvious
                # candidates for inclusion, but any kind of resource can be included as an
                # example resource.
                StructField(
                    "resource",
                    ArrayType(
                        ImplementationGuide_Resource1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Information about a page within the IG.
                StructField(
                    "page",
                    ArrayType(
                        ImplementationGuide_Page1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Indicates a relative path to an image that exists within the IG.
                StructField("image", ArrayType(StringType()), True),
                # Indicates the relative path of an additional non-page, non-image file that is
                # part of the IG - e.g. zip, jar and similar files that could be the target of a
                # hyperlink in a derived IG.
                StructField("other", ArrayType(StringType()), True),
            ]
        )
        return schema
