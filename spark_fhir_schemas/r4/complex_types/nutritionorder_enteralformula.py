from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class NutritionOrder_EnteralFormula:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


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

        baseFormulaType: The type of enteral or infant formula such as an adult standard formula with
            fiber or a soy-based infant formula.

        baseFormulaProductName: The product or brand name of the enteral or infant formula product such as
            "ACME Adult Standard Formula".

        additiveType: Indicates the type of modular component such as protein, carbohydrate, fat or
            fiber to be provided in addition to or mixed with the base formula.

        additiveProductName: The product or brand name of the type of modular component to be added to the
            formula.

        caloricDensity: The amount of energy (calories) that the formula should provide per specified
            volume, typically per mL or fluid oz.  For example, an infant may require a
            formula that provides 24 calories per fluid ounce or an adult may require an
            enteral formula that provides 1.5 calorie/mL.

        routeofAdministration: The route or physiological path of administration into the patient's
            gastrointestinal  tract for purposes of providing the formula feeding, e.g.
            nasogastric tube.

        administration: Formula administration instructions as structured data.  This repeating
            structure allows for changing the administration rate or volume over time for
            both bolus and continuous feeding.  An example of this would be an instruction
            to increase the rate of continuous feeding every 2 hours.

        maxVolumeToDeliver: The maximum total quantity of formula that may be administered to a subject
            over the period of time, e.g. 1440 mL over 24 hours.

        administrationInstruction: Free text formula administration, feeding instructions or additional
            instructions or information.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.nutritionorder_administration import NutritionOrder_Administration
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
                # The type of enteral or infant formula such as an adult standard formula with
                # fiber or a soy-based infant formula.
                StructField(
                    "baseFormulaType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The product or brand name of the enteral or infant formula product such as
                # "ACME Adult Standard Formula".
                StructField("baseFormulaProductName", StringType(), True),
                # Indicates the type of modular component such as protein, carbohydrate, fat or
                # fiber to be provided in addition to or mixed with the base formula.
                StructField(
                    "additiveType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The product or brand name of the type of modular component to be added to the
                # formula.
                StructField("additiveProductName", StringType(), True),
                # The amount of energy (calories) that the formula should provide per specified
                # volume, typically per mL or fluid oz.  For example, an infant may require a
                # formula that provides 24 calories per fluid ounce or an adult may require an
                # enteral formula that provides 1.5 calorie/mL.
                StructField(
                    "caloricDensity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The route or physiological path of administration into the patient's
                # gastrointestinal  tract for purposes of providing the formula feeding, e.g.
                # nasogastric tube.
                StructField(
                    "routeofAdministration",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Formula administration instructions as structured data.  This repeating
                # structure allows for changing the administration rate or volume over time for
                # both bolus and continuous feeding.  An example of this would be an instruction
                # to increase the rate of continuous feeding every 2 hours.
                StructField(
                    "administration",
                    ArrayType(
                        NutritionOrder_Administration.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The maximum total quantity of formula that may be administered to a subject
                # over the period of time, e.g. 1440 mL over 24 hours.
                StructField(
                    "maxVolumeToDeliver",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                # Free text formula administration, feeding instructions or additional
                # instructions or information.
                StructField("administrationInstruction", StringType(), True),
            ]
        )
        return schema
