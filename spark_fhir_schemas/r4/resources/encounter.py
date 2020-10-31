from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Encounter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An interaction between a patient and healthcare provider(s) for the purpose of
        providing healthcare service(s) or assessing the health status of a patient.


        resourceType: This is a Encounter resource

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

        identifier: Identifier(s) by which this encounter is known.

        status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +.

        statusHistory: The status history permits the encounter resource to contain the status
            history without needing to read through the historical versions of the
            resource, or even have the server store them.

        class: Concepts representing classification of patient encounter such as ambulatory
            (outpatient), inpatient, emergency, home health or others due to local
            variations.

        classHistory: The class history permits the tracking of the encounters transitions without
            needing to go  through the resource history.  This would be used for a case
            where an admission starts of as an emergency encounter, then transitions into
            an inpatient scenario. Doing this and not restarting a new encounter ensures
            that any lab/diagnostic results can more easily follow the patient and not
            require re-processing and not get lost or cancelled during a kind of discharge
            from emergency to inpatient.

        type: Specific type of encounter (e.g. e-mail consultation, surgical day-care,
            skilled nursing, rehabilitation).

        serviceType: Broad categorization of the service that is to be provided (e.g. cardiology).

        priority: Indicates the urgency of the encounter.

        subject: The patient or group present at the encounter.

        episodeOfCare: Where a specific encounter should be classified as a part of a specific
            episode(s) of care this field should be used. This association can facilitate
            grouping of related encounters together for a specific purpose, such as
            government reporting, issue tracking, association via a common problem.  The
            association is recorded on the encounter as these are typically created after
            the episode of care and grouped on entry rather than editing the episode of
            care to append another encounter to it (the episode of care could span years).

        basedOn: The request this encounter satisfies (e.g. incoming referral or procedure
            request).

        participant: The list of people responsible for providing the service.

        appointment: The appointment that scheduled this encounter.

        period: The start and end time of the encounter.

        length: Quantity of time the encounter lasted. This excludes the time during leaves of
            absence.

        reasonCode: Reason the encounter takes place, expressed as a code. For admissions, this
            can be used for a coded admission diagnosis.

        reasonReference: Reason the encounter takes place, expressed as a code. For admissions, this
            can be used for a coded admission diagnosis.

        diagnosis: The list of diagnosis relevant to this encounter.

        account: The set of accounts that may be used for billing for this Encounter.

        hospitalization: Details about the admission to a healthcare service.

        location: List of locations where  the patient has been during this encounter.

        serviceProvider: The organization that is primarily responsible for this Encounter's services.
            This MAY be the same as the organization on the Patient record, however it
            could be different, such as if the actor performing the services was from an
            external organization (which may be billed seperately) for an external
            consultation.  Refer to the example bundle showing an abbreviated set of
            Encounters for a colonoscopy.

        partOf: Another Encounter of which this encounter is a part of (administratively or in
            time).

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.encounter_statushistory import Encounter_StatusHistory
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.encounter_classhistory import Encounter_ClassHistory
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.encounter_participant import Encounter_Participant
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.encounter_diagnosis import Encounter_Diagnosis
        from spark_fhir_schemas.r4.complex_types.encounter_hospitalization import Encounter_Hospitalization
        from spark_fhir_schemas.r4.complex_types.encounter_location import Encounter_Location
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Encounter resource
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
                # Identifier(s) by which this encounter is known.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # planned | arrived | triaged | in-progress | onleave | finished | cancelled +.
                StructField("status", StringType(), True),
                # The status history permits the encounter resource to contain the status
                # history without needing to read through the historical versions of the
                # resource, or even have the server store them.
                StructField(
                    "statusHistory",
                    ArrayType(
                        Encounter_StatusHistory.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Concepts representing classification of patient encounter such as ambulatory
                # (outpatient), inpatient, emergency, home health or others due to local
                # variations.
                StructField(
                    "class", Coding.get_schema(recursion_depth + 1), True
                ),
                # The class history permits the tracking of the encounters transitions without
                # needing to go  through the resource history.  This would be used for a case
                # where an admission starts of as an emergency encounter, then transitions into
                # an inpatient scenario. Doing this and not restarting a new encounter ensures
                # that any lab/diagnostic results can more easily follow the patient and not
                # require re-processing and not get lost or cancelled during a kind of discharge
                # from emergency to inpatient.
                StructField(
                    "classHistory",
                    ArrayType(
                        Encounter_ClassHistory.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Specific type of encounter (e.g. e-mail consultation, surgical day-care,
                # skilled nursing, rehabilitation).
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Broad categorization of the service that is to be provided (e.g. cardiology).
                StructField(
                    "serviceType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates the urgency of the encounter.
                StructField(
                    "priority",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The patient or group present at the encounter.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # Where a specific encounter should be classified as a part of a specific
                # episode(s) of care this field should be used. This association can facilitate
                # grouping of related encounters together for a specific purpose, such as
                # government reporting, issue tracking, association via a common problem.  The
                # association is recorded on the encounter as these are typically created after
                # the episode of care and grouped on entry rather than editing the episode of
                # care to append another encounter to it (the episode of care could span years).
                StructField(
                    "episodeOfCare",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The request this encounter satisfies (e.g. incoming referral or procedure
                # request).
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The list of people responsible for providing the service.
                StructField(
                    "participant",
                    ArrayType(
                        Encounter_Participant.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The appointment that scheduled this encounter.
                StructField(
                    "appointment",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The start and end time of the encounter.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # Quantity of time the encounter lasted. This excludes the time during leaves of
                # absence.
                StructField(
                    "length", Duration.get_schema(recursion_depth + 1), True
                ),
                # Reason the encounter takes place, expressed as a code. For admissions, this
                # can be used for a coded admission diagnosis.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Reason the encounter takes place, expressed as a code. For admissions, this
                # can be used for a coded admission diagnosis.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The list of diagnosis relevant to this encounter.
                StructField(
                    "diagnosis",
                    ArrayType(
                        Encounter_Diagnosis.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The set of accounts that may be used for billing for this Encounter.
                StructField(
                    "account",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Details about the admission to a healthcare service.
                StructField(
                    "hospitalization",
                    Encounter_Hospitalization.get_schema(recursion_depth + 1),
                    True
                ),
                # List of locations where  the patient has been during this encounter.
                StructField(
                    "location",
                    ArrayType(
                        Encounter_Location.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The organization that is primarily responsible for this Encounter's services.
                # This MAY be the same as the organization on the Patient record, however it
                # could be different, such as if the actor performing the services was from an
                # external organization (which may be billed seperately) for an external
                # consultation.  Refer to the example bundle showing an abbreviated set of
                # Encounters for a colonoscopy.
                StructField(
                    "serviceProvider",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Another Encounter of which this encounter is a part of (administratively or in
                # time).
                StructField(
                    "partOf", Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
