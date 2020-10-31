from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ElementDefinition_Type:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        code: URL of Data type or Resource that is a(or the) type used for this element.
            References are URLs that are relative to
            http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to
            http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed
            in logical models.

        profile: Identifies a profile structure or implementation Guide that applies to the
            datatype this element refers to. If any profiles are specified, then the
            content must conform to at least one of them. The URL can be a local reference
            - to a contained StructureDefinition, or a reference to another
            StructureDefinition or Implementation Guide by a canonical URL. When an
            implementation guide is specified, the type SHALL conform to at least one
            profile defined in the implementation guide.

        targetProfile: Used when the type is "Reference" or "canonical", and identifies a profile
            structure or implementation Guide that applies to the target of the reference
            this element refers to. If any profiles are specified, then the content must
            conform to at least one of them. The URL can be a local reference - to a
            contained StructureDefinition, or a reference to another StructureDefinition
            or Implementation Guide by a canonical URL. When an implementation guide is
            specified, the target resource SHALL conform to at least one profile defined
            in the implementation guide.

        aggregation: If the type is a reference to another resource, how the resource is or can be
            aggregated - is it a contained resource, or a reference, and if the context is
            a bundle, is it included in the bundle.

        versioning: Whether this reference needs to be version specific or version independent, or
            whether either can be used.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
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
                # URL of Data type or Resource that is a(or the) type used for this element.
                # References are URLs that are relative to
                # http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to
                # http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed
                # in logical models.
                StructField("code", uri.get_schema(recursion_depth + 1), True),
                # Identifies a profile structure or implementation Guide that applies to the
                # datatype this element refers to. If any profiles are specified, then the
                # content must conform to at least one of them. The URL can be a local reference
                # - to a contained StructureDefinition, or a reference to another
                # StructureDefinition or Implementation Guide by a canonical URL. When an
                # implementation guide is specified, the type SHALL conform to at least one
                # profile defined in the implementation guide.
                StructField(
                    "profile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # Used when the type is "Reference" or "canonical", and identifies a profile
                # structure or implementation Guide that applies to the target of the reference
                # this element refers to. If any profiles are specified, then the content must
                # conform to at least one of them. The URL can be a local reference - to a
                # contained StructureDefinition, or a reference to another StructureDefinition
                # or Implementation Guide by a canonical URL. When an implementation guide is
                # specified, the target resource SHALL conform to at least one profile defined
                # in the implementation guide.
                StructField(
                    "targetProfile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # If the type is a reference to another resource, how the resource is or can be
                # aggregated - is it a contained resource, or a reference, and if the context is
                # a bundle, is it included in the bundle.
                # Whether this reference needs to be version specific or version independent, or
                # whether either can be used.
                StructField("versioning", StringType(), True),
            ]
        )
        return schema
