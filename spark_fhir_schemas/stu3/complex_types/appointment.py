from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class AppointmentSchema:
    """
    A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one or
    more Encounter(s).
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
        A booking of a healthcare event among patient(s), practitioner(s), related
        person(s) and/or device(s) for a specific date/time. This may result in one or
        more Encounter(s).


        resourceType: This is a Appointment resource

        identifier: This records identifiers associated with this appointment concern that are
            defined by business processes and/or used to refer to it when a direct URL
            reference to the resource itself is not appropriate (e.g. in CDA documents, or
            in written / printed documentation).

        status: The overall status of the Appointment. Each of the participants has their own
            participation status which indicates their involvement in the process, however
            this status indicates the shared status.

        serviceCategory: A broad categorisation of the service that is to be performed during this
            appointment.

        serviceType: The specific service that is to be performed during this appointment.

        specialty: The specialty of a practitioner that would be required to perform the service
            requested in this appointment.

        appointmentType: The style of appointment or patient that has been booked in the slot (not
            service type).

        reason: The reason that this appointment is being scheduled. This is more clinical
            than administrative.

        indication: Reason the appointment has been scheduled to take place, as specified using
            information from another resource. When the patient arrives and the encounter
            begins it may be used as the admission diagnosis. The indication will
            typically be a Condition (with other resources referenced in the
            evidence.detail), or a Procedure.

        priority: The priority of the appointment. Can be used to make informed decisions if
            needing to re-prioritize appointments. (The iCal Standard specifies 0 as
            undefined, 1 as highest, 9 as lowest priority).

        description: The brief description of the appointment as would be shown on a subject line
            in a meeting request, or appointment list. Detailed or expanded information
            should be put in the comment field.

        supportingInformation: Additional information to support the appointment provided when making the
            appointment.

        start: Date/Time that the appointment is to take place.

        end: Date/Time that the appointment is to conclude.

        minutesDuration: Number of minutes that the appointment is to take. This can be less than the
            duration between the start and end times (where actual time of appointment is
            only an estimate or is a planned appointment request).

        slot: The slots from the participants' schedules that will be filled by the
            appointment.

        created: The date that this appointment was initially created. This could be different
            to the meta.lastModified value on the initial entry, as this could have been
            before the resource was created on the FHIR server, and should remain
            unchanged over the lifespan of the appointment.

        comment: Additional comments about the appointment.

        incomingReferral: The referral request this appointment is allocated to assess (incoming
            referral).

        participant: List of participants involved in the appointment.

        requestedPeriod: A set of date ranges (potentially including times) that the appointment is
            preferred to be scheduled within. When using these values, the minutes
            duration should be provided to indicate the length of the appointment to fill
            and populate the start/end times for the actual allocated time.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.appointment_participant import Appointment_ParticipantSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        if (
            max_recursion_limit
            and nesting_list.count("Appointment") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Appointment"]
        schema = StructType(
            [
                # This is a Appointment resource
                StructField("resourceType", StringType(), True),
                # This records identifiers associated with this appointment concern that are
                # defined by business processes and/or used to refer to it when a direct URL
                # reference to the resource itself is not appropriate (e.g. in CDA documents, or
                # in written / printed documentation).
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
                # The overall status of the Appointment. Each of the participants has their own
                # participation status which indicates their involvement in the process, however
                # this status indicates the shared status.
                StructField("status", StringType(), True),
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
                # The specific service that is to be performed during this appointment.
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
                # The style of appointment or patient that has been booked in the slot (not
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
                # The reason that this appointment is being scheduled. This is more clinical
                # than administrative.
                StructField(
                    "reason",
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
                # Reason the appointment has been scheduled to take place, as specified using
                # information from another resource. When the patient arrives and the encounter
                # begins it may be used as the admission diagnosis. The indication will
                # typically be a Condition (with other resources referenced in the
                # evidence.detail), or a Procedure.
                StructField(
                    "indication",
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
                # The priority of the appointment. Can be used to make informed decisions if
                # needing to re-prioritize appointments. (The iCal Standard specifies 0 as
                # undefined, 1 as highest, 9 as lowest priority).
                StructField("priority", IntegerType(), True),
                # The brief description of the appointment as would be shown on a subject line
                # in a meeting request, or appointment list. Detailed or expanded information
                # should be put in the comment field.
                StructField("description", StringType(), True),
                # Additional information to support the appointment provided when making the
                # appointment.
                StructField(
                    "supportingInformation",
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
                # Date/Time that the appointment is to take place.
                StructField("start", StringType(), True),
                # Date/Time that the appointment is to conclude.
                StructField("end", StringType(), True),
                # Number of minutes that the appointment is to take. This can be less than the
                # duration between the start and end times (where actual time of appointment is
                # only an estimate or is a planned appointment request).
                StructField("minutesDuration", IntegerType(), True),
                # The slots from the participants' schedules that will be filled by the
                # appointment.
                StructField(
                    "slot",
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
                # The date that this appointment was initially created. This could be different
                # to the meta.lastModified value on the initial entry, as this could have been
                # before the resource was created on the FHIR server, and should remain
                # unchanged over the lifespan of the appointment.
                StructField("created", StringType(), True),
                # Additional comments about the appointment.
                StructField("comment", StringType(), True),
                # The referral request this appointment is allocated to assess (incoming
                # referral).
                StructField(
                    "incomingReferral",
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
                # List of participants involved in the appointment.
                StructField(
                    "participant",
                    ArrayType(
                        Appointment_ParticipantSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A set of date ranges (potentially including times) that the appointment is
                # preferred to be scheduled within. When using these values, the minutes
                # duration should be provided to indicate the length of the appointment to fill
                # and populate the start/end times for the actual allocated time.
                StructField(
                    "requestedPeriod",
                    ArrayType(
                        PeriodSchema.get_schema(
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
