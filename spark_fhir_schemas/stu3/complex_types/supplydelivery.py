from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class SupplyDeliverySchema:
    """
    Record of delivery of what is supplied.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        Record of delivery of what is supplied.


        resourceType: This is a SupplyDelivery resource

        identifier: Identifier assigned by the dispensing facility when the item(s) is dispensed.

        basedOn: A plan, proposal or order that is fulfilled in whole or in part by this event.

        partOf: A larger event of which this particular event is a component or step.

        status: A code specifying the state of the dispense event.

        patient: A link to a resource representing the person whom the delivered item is for.

        type: Indicates the type of dispensing event that is performed. Examples include:
            Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.

        suppliedItem: The item that is being delivered or has been supplied.

        occurrenceDateTime: The date or time(s) the activity occurred.

        occurrencePeriod: The date or time(s) the activity occurred.

        occurrenceTiming: The date or time(s) the activity occurred.

        supplier: The individual responsible for dispensing the medication, supplier or device.

        destination: Identification of the facility/location where the Supply was shipped to, as
            part of the dispense event.

        receiver: Identifies the person who picked up the Supply.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.supplydelivery_supplieditem import SupplyDelivery_SuppliedItemSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.timing import TimingSchema
        if (
            max_recursion_limit
            and nesting_list.count("SupplyDelivery") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SupplyDelivery"]
        schema = StructType(
            [
                # This is a SupplyDelivery resource
                StructField("resourceType", StringType(), True),
                # Identifier assigned by the dispensing facility when the item(s) is dispensed.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A plan, proposal or order that is fulfilled in whole or in part by this event.
                StructField(
                    "basedOn",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A larger event of which this particular event is a component or step.
                StructField(
                    "partOf",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A code specifying the state of the dispense event.
                StructField("status", StringType(), True),
                # A link to a resource representing the person whom the delivered item is for.
                StructField(
                    "patient",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates the type of dispensing event that is performed. Examples include:
                # Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The item that is being delivered or has been supplied.
                StructField(
                    "suppliedItem",
                    SupplyDelivery_SuppliedItemSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The date or time(s) the activity occurred.
                StructField("occurrenceDateTime", StringType(), True),
                # The date or time(s) the activity occurred.
                StructField(
                    "occurrencePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The date or time(s) the activity occurred.
                StructField(
                    "occurrenceTiming",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The individual responsible for dispensing the medication, supplier or device.
                StructField(
                    "supplier",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Identification of the facility/location where the Supply was shipped to, as
                # part of the dispense event.
                StructField(
                    "destination",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Identifies the person who picked up the Supply.
                StructField(
                    "receiver",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
