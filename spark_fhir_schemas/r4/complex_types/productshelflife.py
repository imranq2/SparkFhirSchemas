from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ProductShelfLife:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The shelf-life and storage information for a medicinal product item or
        container can be described using this class.


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

        identifier: Unique identifier for the packaged Medicinal Product.

        type: This describes the shelf life, taking into account various scenarios such as
            shelf life of the packaged Medicinal Product itself, shelf life after
            transformation where necessary and shelf life after the first opening of a
            bottle, etc. The shelf life type shall be specified using an appropriate
            controlled vocabulary The controlled term and the controlled term identifier
            shall be specified.

        period: The shelf life time period can be specified using a numerical value for the
            period of time and its unit of time measurement The unit of measurement shall
            be specified in accordance with ISO 11240 and the resulting terminology The
            symbol and the symbol identifier shall be used.

        specialPrecautionsForStorage: Special precautions for storage, if any, can be specified using an appropriate
            controlled vocabulary The controlled term and the controlled term identifier
            shall be specified.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                # Unique identifier for the packaged Medicinal Product.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # This describes the shelf life, taking into account various scenarios such as
                # shelf life of the packaged Medicinal Product itself, shelf life after
                # transformation where necessary and shelf life after the first opening of a
                # bottle, etc. The shelf life type shall be specified using an appropriate
                # controlled vocabulary The controlled term and the controlled term identifier
                # shall be specified.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The shelf life time period can be specified using a numerical value for the
                # period of time and its unit of time measurement The unit of measurement shall
                # be specified in accordance with ISO 11240 and the resulting terminology The
                # symbol and the symbol identifier shall be used.
                StructField(
                    "period", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Special precautions for storage, if any, can be specified using an appropriate
                # controlled vocabulary The controlled term and the controlled term identifier
                # shall be specified.
                StructField(
                    "specialPrecautionsForStorage",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
