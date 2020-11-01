from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductPharmaceutical_RouteOfAdministrationSchema:
    """
    A pharmaceutical product described in terms of its composition and dose form.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        A pharmaceutical product described in terms of its composition and dose form.


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

        code: Coded expression for the route.

        firstDose: The first dose (dose quantity) administered in humans can be specified, for a
            product under investigation, using a numerical value and its unit of
            measurement.

        maxSingleDose: The maximum single dose that can be administered as per the protocol of a
            clinical trial can be specified using a numerical value and its unit of
            measurement.

        maxDosePerDay: The maximum dose per day (maximum dose quantity to be administered in any one
            24-h period) that can be administered as per the protocol referenced in the
            clinical trial authorisation.

        maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered as per the
            protocol referenced in the clinical trial authorisation.

        maxTreatmentPeriod: The maximum treatment period during which an Investigational Medicinal Product
            can be administered as per the protocol referenced in the clinical trial
            authorisation.

        targetSpecies: A species for which this route applies.

        """
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.ratio import RatioSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        from spark_fhir_schemas.r4.complex_types.medicinalproductpharmaceutical_targetspecies import MedicinalProductPharmaceutical_TargetSpeciesSchema
        if recursion_list.count(
            "MedicinalProductPharmaceutical_RouteOfAdministration"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + [
            "MedicinalProductPharmaceutical_RouteOfAdministration"
        ]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.

                # >>> Hiding extension Extension

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

                # >>> Hiding modifierExtension Extension

                # Coded expression for the route.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The first dose (dose quantity) administered in humans can be specified, for a
                # product under investigation, using a numerical value and its unit of
                # measurement.
                StructField(
                    "firstDose",
                    QuantitySchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The maximum single dose that can be administered as per the protocol of a
                # clinical trial can be specified using a numerical value and its unit of
                # measurement.
                StructField(
                    "maxSingleDose",
                    QuantitySchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The maximum dose per day (maximum dose quantity to be administered in any one
                # 24-h period) that can be administered as per the protocol referenced in the
                # clinical trial authorisation.
                StructField(
                    "maxDosePerDay",
                    QuantitySchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The maximum dose per treatment period that can be administered as per the
                # protocol referenced in the clinical trial authorisation.
                StructField(
                    "maxDosePerTreatmentPeriod",
                    RatioSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The maximum treatment period during which an Investigational Medicinal Product
                # can be administered as per the protocol referenced in the clinical trial
                # authorisation.
                StructField(
                    "maxTreatmentPeriod",
                    DurationSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A species for which this route applies.
                StructField(
                    "targetSpecies",
                    ArrayType(
                        MedicinalProductPharmaceutical_TargetSpeciesSchema.
                        get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
            ]
        )
        return schema
