from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_SecurityLabel:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


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

        number: Number used to link this term or term element to the applicable Security
            Label.

        classification: Security label privacy tag that species the level of confidentiality
            protection required for this term and/or term elements.

        category: Security label privacy tag that species the applicable privacy and security
            policies governing this term and/or term elements.

        control: Security label privacy tag that species the manner in which term and/or term
            elements are to be protected.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.coding import Coding
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
                # Number used to link this term or term element to the applicable Security
                # Label.
                StructField(
                    "number",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
                # Security label privacy tag that species the level of confidentiality
                # protection required for this term and/or term elements.
                StructField(
                    "classification", Coding.get_schema(recursion_depth + 1),
                    True
                ),
                # Security label privacy tag that species the applicable privacy and security
                # policies governing this term and/or term elements.
                StructField(
                    "category",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                # Security label privacy tag that species the manner in which term and/or term
                # elements are to be protected.
                StructField(
                    "control",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
