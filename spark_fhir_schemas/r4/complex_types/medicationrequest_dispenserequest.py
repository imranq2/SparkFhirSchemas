from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationRequest_DispenseRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An order or request for both supply of the medication and the instructions for
        administration of the medication to a patient. The resource is called
        "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
        to generalize the use across inpatient and outpatient settings, including care
        plans, etc., and to harmonize with workflow patterns.


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

        initialFill: Indicates the quantity or duration for the first dispense of the medication.

        dispenseInterval: The minimum period of time that must occur between dispenses of the
            medication.

        validityPeriod: This indicates the validity period of a prescription (stale dating the
            Prescription).

        numberOfRepeatsAllowed: An integer indicating the number of times, in addition to the original
            dispense, (aka refills or repeats) that the patient can receive the prescribed
            medication. Usage Notes: This integer does not include the original order
            dispense. This means that if an order indicates dispense 30 tablets plus "3
            repeats", then the order can be dispensed a total of 4 times and the patient
            can receive a total of 120 tablets.  A prescriber may explicitly say that zero
            refills are permitted after the initial dispense.

        quantity: The amount that is to be dispensed for one fill.

        expectedSupplyDuration: Identifies the period time over which the supplied product is expected to be
            used, or the length of time the dispense is expected to last.

        performer: Indicates the intended dispensing Organization specified by the prescriber.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.medicationrequest_initialfill import MedicationRequest_InitialFill
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # Indicates the quantity or duration for the first dispense of the medication.
                StructField(
                    "initialFill",
                    MedicationRequest_InitialFill.
                    get_schema(recursion_depth + 1), True
                ),
                # The minimum period of time that must occur between dispenses of the
                # medication.
                StructField(
                    "dispenseInterval",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # This indicates the validity period of a prescription (stale dating the
                # Prescription).
                StructField(
                    "validityPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # An integer indicating the number of times, in addition to the original
                # dispense, (aka refills or repeats) that the patient can receive the prescribed
                # medication. Usage Notes: This integer does not include the original order
                # dispense. This means that if an order indicates dispense 30 tablets plus "3
                # repeats", then the order can be dispensed a total of 4 times and the patient
                # can receive a total of 120 tablets.  A prescriber may explicitly say that zero
                # refills are permitted after the initial dispense.
                StructField(
                    "numberOfRepeatsAllowed",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # The amount that is to be dispensed for one fill.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Identifies the period time over which the supplied product is expected to be
                # used, or the length of time the dispense is expected to last.
                StructField(
                    "expectedSupplyDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # Indicates the intended dispensing Organization specified by the prescriber.
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
