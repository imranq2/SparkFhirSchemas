from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ObservationDefinition_QuantitativeDetailsSchema:
    """
    Set of definitional characteristics for a kind of observation or measurement
    produced or consumed by an orderable health care service.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Set of definitional characteristics for a kind of observation or measurement
        produced or consumed by an orderable health care service.


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

        customaryUnit: Customary unit used to report quantitative results of observations conforming
            to this ObservationDefinition.

        unit: SI unit used to report quantitative results of observations conforming to this
            ObservationDefinition.

        conversionFactor: Factor for converting value expressed with SI unit to value expressed with
            customary unit.

        decimalPrecision: Number of digits after decimal separator when the results of such observations
            are of type Quantity.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.simple_types.decimal import decimalSchema
        from spark_fhir_schemas.r4.simple_types.integer import integerSchema
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Customary unit used to report quantitative results of observations conforming
                # to this ObservationDefinition.
                StructField(
                    "customaryUnit",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # SI unit used to report quantitative results of observations conforming to this
                # ObservationDefinition.
                StructField(
                    "unit",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Factor for converting value expressed with SI unit to value expressed with
                # customary unit.
                StructField(
                    "conversionFactor",
                    decimalSchema.get_schema(recursion_depth + 1), True
                ),
                # Number of digits after decimal separator when the results of such observations
                # are of type Quantity.
                StructField(
                    "decimalPrecision",
                    integerSchema.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
