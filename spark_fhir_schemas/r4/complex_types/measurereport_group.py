from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class MeasureReport_GroupSchema:
    """
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The MeasureReport resource contains the results of the calculation of a
        measure; and optionally a reference to the resources involved in that
        calculation.


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

        code: The meaning of the population group as defined in the measure definition.

        population: The populations that make up the population group, one for each type of
            population appropriate for the measure.

        measureScore: The measure score for this population group, calculated as appropriate for the
            measure type and scoring method, and based on the contents of the populations
            defined in the group.

        stratifier: When a measure includes multiple stratifiers, there will be a stratifier group
            for each stratifier defined by the measure.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.measurereport_population import MeasureReport_PopulationSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.measurereport_stratifier import MeasureReport_StratifierSchema
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
                # The meaning of the population group as defined in the measure definition.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The populations that make up the population group, one for each type of
                # population appropriate for the measure.
                StructField(
                    "population",
                    ArrayType(
                        MeasureReport_PopulationSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The measure score for this population group, calculated as appropriate for the
                # measure type and scoring method, and based on the contents of the populations
                # defined in the group.
                StructField(
                    "measureScore",
                    QuantitySchema.get_schema(recursion_depth + 1), True
                ),
                # When a measure includes multiple stratifiers, there will be a stratifier group
                # for each stratifier defined by the measure.
                StructField(
                    "stratifier",
                    ArrayType(
                        MeasureReport_StratifierSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
