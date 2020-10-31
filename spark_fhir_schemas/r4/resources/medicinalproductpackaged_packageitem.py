from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.medicinalproductpackaged_packageitem import MedicinalProductPackaged_PackageItem
from spark_fhir_schemas.r4.resources.prodcharacteristic import ProdCharacteristic
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.productshelflife import ProductShelfLife
from spark_fhir_schemas.r4.resources.reference import Reference


class MedicinalProductPackaged_PackageItem:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("material",ArrayType(CodeableConcept.get_schema()), True),
                StructField("alternateMaterial",ArrayType(CodeableConcept.get_schema()), True),
                StructField("device",ArrayType(Reference.get_schema()), True),
                StructField("manufacturedItem",ArrayType(Reference.get_schema()), True),
                StructField("packageItem",ArrayType(MedicinalProductPackaged_PackageItem.get_schema()), True),
                StructField("physicalCharacteristics", ProdCharacteristic.get_schema(), True),
                StructField("otherCharacteristics",ArrayType(CodeableConcept.get_schema()), True),
                StructField("shelfLifeStorage",ArrayType(ProductShelfLife.get_schema()), True),
                StructField("manufacturer",ArrayType(Reference.get_schema()), True),]
        )

        return schema
