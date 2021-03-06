from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class SlotSchema:
    """
    A slot of time on a schedule that may be available for booking appointments.
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
        A slot of time on a schedule that may be available for booking appointments.


        resourceType: This is a Slot resource

        identifier: External Ids for this item.

        serviceCategory: A broad categorisation of the service that is to be performed during this
            appointment.

        serviceType: The type of appointments that can be booked into this slot (ideally this would
            be an identifiable service - which is at a location, rather than the location
            itself). If provided then this overrides the value provided on the
            availability resource.

        specialty: The specialty of a practitioner that would be required to perform the service
            requested in this appointment.

        appointmentType: The style of appointment or patient that may be booked in the slot (not
            service type).

        schedule: The schedule resource that this slot defines an interval of status
            information.

        status: busy | free | busy-unavailable | busy-tentative | entered-in-error.

        start: Date/Time that the slot is to begin.

        end: Date/Time that the slot is to conclude.

        overbooked: This slot has already been overbooked, appointments are unlikely to be
            accepted for this time.

        comment: Comments on the slot to describe any extended information. Such as custom
            constraints on the slot.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        if (
            max_recursion_limit
            and nesting_list.count("Slot") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Slot"]
        schema = StructType(
            [
                # This is a Slot resource
                StructField("resourceType", StringType(), True),
                # External Ids for this item.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A broad categorisation of the service that is to be performed during this
                # appointment.
                StructField(
                    "serviceCategory",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The type of appointments that can be booked into this slot (ideally this would
                # be an identifiable service - which is at a location, rather than the location
                # itself). If provided then this overrides the value provided on the
                # availability resource.
                StructField(
                    "serviceType",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The specialty of a practitioner that would be required to perform the service
                # requested in this appointment.
                StructField(
                    "specialty",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The style of appointment or patient that may be booked in the slot (not
                # service type).
                StructField(
                    "appointmentType",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The schedule resource that this slot defines an interval of status
                # information.
                StructField(
                    "schedule",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # busy | free | busy-unavailable | busy-tentative | entered-in-error.
                StructField("status", StringType(), True),
                # Date/Time that the slot is to begin.
                StructField("start", StringType(), True),
                # Date/Time that the slot is to conclude.
                StructField("end", StringType(), True),
                # This slot has already been overbooked, appointments are unlikely to be
                # accepted for this time.
                StructField("overbooked", BooleanType(), True),
                # Comments on the slot to describe any extended information. Such as custom
                # constraints on the slot.
                StructField("comment", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
