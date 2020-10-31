from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicinalProductPackaged_PackageItem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A medicinal product in a container or package.


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

        identifier: Including possibly Data Carrier Identifier.

        type: The physical type of the container of the medicine.

        quantity: The quantity of this package in the medicinal product, at the current level of
            packaging. The outermost is always 1.

        material: Material type of the package item.

        alternateMaterial: A possible alternate material for the packaging.

        device: A device accompanying a medicinal product.

        manufacturedItem: The manufactured item as contained in the packaged medicinal product.

        packageItem: Allows containers within containers.

        physicalCharacteristics: Dimensions, color etc.

        otherCharacteristics: Other codeable characteristics.

        shelfLifeStorage: Shelf Life and storage information.

        manufacturer: Manufacturer of this Package Item.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.prodcharacteristic import ProdCharacteristic
        from spark_fhir_schemas.r4.complex_types.productshelflife import ProductShelfLife
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
                # Including possibly Data Carrier Identifier.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The physical type of the container of the medicine.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The quantity of this package in the medicinal product, at the current level of
                # packaging. The outermost is always 1.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Material type of the package item.
                StructField(
                    "material",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A possible alternate material for the packaging.
                StructField(
                    "alternateMaterial",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A device accompanying a medicinal product.
                StructField(
                    "device",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The manufactured item as contained in the packaged medicinal product.
                StructField(
                    "manufacturedItem",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Allows containers within containers.
                StructField(
                    "packageItem",
                    ArrayType(
                        MedicinalProductPackaged_PackageItem.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Dimensions, color etc.
                StructField(
                    "physicalCharacteristics",
                    ProdCharacteristic.get_schema(recursion_depth + 1), True
                ),
                # Other codeable characteristics.
                StructField(
                    "otherCharacteristics",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Shelf Life and storage information.
                StructField(
                    "shelfLifeStorage",
                    ArrayType(
                        ProductShelfLife.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Manufacturer of this Package Item.
                StructField(
                    "manufacturer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
