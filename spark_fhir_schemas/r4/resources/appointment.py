from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Appointment:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A booking of a healthcare event among patient(s), practitioner(s), related
        person(s) and/or device(s) for a specific date/time. This may result in one or
        more Encounter(s).


        resourceType: This is a Appointment resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: This records identifiers associated with this appointment concern that are
            defined by business processes and/or used to refer to it when a direct URL
            reference to the resource itself is not appropriate (e.g. in CDA documents, or
            in written / printed documentation).

        status: The overall status of the Appointment. Each of the participants has their own
            participation status which indicates their involvement in the process, however
            this status indicates the shared status.

        cancelationReason: The coded reason for the appointment being cancelled. This is often used in
            reporting/billing/futher processing to determine if further actions are
            required, or specific fees apply.

        serviceCategory: A broad categorization of the service that is to be performed during this
            appointment.

        serviceType: The specific service that is to be performed during this appointment.

        specialty: The specialty of a practitioner that would be required to perform the service
            requested in this appointment.

        appointmentType: The style of appointment or patient that has been booked in the slot (not
            service type).

        reasonCode: The coded reason that this appointment is being scheduled. This is more
            clinical than administrative.

        reasonReference: Reason the appointment has been scheduled to take place, as specified using
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
            duration between the start and end times.  For example, where the actual time
            of appointment is only an estimate or if a 30 minute appointment is being
            requested, but any time would work.  Also, if there is, for example, a planned
            15 minute break in the middle of a long appointment, the duration may be 15
            minutes less than the difference between the start and end.

        slot: The slots from the participants' schedules that will be filled by the
            appointment.

        created: The date that this appointment was initially created. This could be different
            to the meta.lastModified value on the initial entry, as this could have been
            before the resource was created on the FHIR server, and should remain
            unchanged over the lifespan of the appointment.

        comment: Additional comments about the appointment.

        patientInstruction: While Appointment.comment contains information for internal use,
            Appointment.patientInstructions is used to capture patient facing information
            about the Appointment (e.g. please bring your referral or fast from 8pm night
            before).

        basedOn: The service request this appointment is allocated to assess (e.g. incoming
            referral or procedure request).

        participant: List of participants involved in the appointment.

        requestedPeriod: A set of date ranges (potentially including times) that the appointment is
            preferred to be scheduled within.

            The duration (usually in minutes) could also be provided to indicate the
            length of the appointment to fill and populate the start/end times for the
            actual allocated time. However, in other situations the duration may be
            calculated by the scheduling system.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.appointment_participant import Appointment_Participant
        from spark_fhir_schemas.r4.complex_types.period import Period
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Appointment resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # This records identifiers associated with this appointment concern that are
                # defined by business processes and/or used to refer to it when a direct URL
                # reference to the resource itself is not appropriate (e.g. in CDA documents, or
                # in written / printed documentation).
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The overall status of the Appointment. Each of the participants has their own
                # participation status which indicates their involvement in the process, however
                # this status indicates the shared status.
                StructField("status", StringType(), True),
                # The coded reason for the appointment being cancelled. This is often used in
                # reporting/billing/futher processing to determine if further actions are
                # required, or specific fees apply.
                StructField(
                    "cancelationReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A broad categorization of the service that is to be performed during this
                # appointment.
                StructField(
                    "serviceCategory",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The specific service that is to be performed during this appointment.
                StructField(
                    "serviceType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The specialty of a practitioner that would be required to perform the service
                # requested in this appointment.
                StructField(
                    "specialty",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The style of appointment or patient that has been booked in the slot (not
                # service type).
                StructField(
                    "appointmentType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The coded reason that this appointment is being scheduled. This is more
                # clinical than administrative.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Reason the appointment has been scheduled to take place, as specified using
                # information from another resource. When the patient arrives and the encounter
                # begins it may be used as the admission diagnosis. The indication will
                # typically be a Condition (with other resources referenced in the
                # evidence.detail), or a Procedure.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The priority of the appointment. Can be used to make informed decisions if
                # needing to re-prioritize appointments. (The iCal Standard specifies 0 as
                # undefined, 1 as highest, 9 as lowest priority).
                StructField(
                    "priority", unsignedInt.get_schema(recursion_depth + 1),
                    True
                ),
                # The brief description of the appointment as would be shown on a subject line
                # in a meeting request, or appointment list. Detailed or expanded information
                # should be put in the comment field.
                StructField("description", StringType(), True),
                # Additional information to support the appointment provided when making the
                # appointment.
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Date/Time that the appointment is to take place.
                StructField(
                    "start", instant.get_schema(recursion_depth + 1), True
                ),
                # Date/Time that the appointment is to conclude.
                StructField(
                    "end", instant.get_schema(recursion_depth + 1), True
                ),
                # Number of minutes that the appointment is to take. This can be less than the
                # duration between the start and end times.  For example, where the actual time
                # of appointment is only an estimate or if a 30 minute appointment is being
                # requested, but any time would work.  Also, if there is, for example, a planned
                # 15 minute break in the middle of a long appointment, the duration may be 15
                # minutes less than the difference between the start and end.
                StructField(
                    "minutesDuration",
                    positiveInt.get_schema(recursion_depth + 1), True
                ),
                # The slots from the participants' schedules that will be filled by the
                # appointment.
                StructField(
                    "slot",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The date that this appointment was initially created. This could be different
                # to the meta.lastModified value on the initial entry, as this could have been
                # before the resource was created on the FHIR server, and should remain
                # unchanged over the lifespan of the appointment.
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Additional comments about the appointment.
                StructField("comment", StringType(), True),
                # While Appointment.comment contains information for internal use,
                # Appointment.patientInstructions is used to capture patient facing information
                # about the Appointment (e.g. please bring your referral or fast from 8pm night
                # before).
                StructField("patientInstruction", StringType(), True),
                # The service request this appointment is allocated to assess (e.g. incoming
                # referral or procedure request).
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # List of participants involved in the appointment.
                StructField(
                    "participant",
                    ArrayType(
                        Appointment_Participant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A set of date ranges (potentially including times) that the appointment is
                # preferred to be scheduled within.
                #
                # The duration (usually in minutes) could also be provided to indicate the
                # length of the appointment to fill and populate the start/end times for the
                # actual allocated time. However, in other situations the duration may be
                # calculated by the scheduling system.
                StructField(
                    "requestedPeriod",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
