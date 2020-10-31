from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Condition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A clinical condition, problem, diagnosis, or other event, situation, issue, or
        clinical concept that has risen to a level of concern.


        resourceType: This is a Condition resource

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

        identifier: Business identifiers assigned to this condition by the performer or other
            systems which remain constant as the resource is updated and propagates from
            server to server.

        clinicalStatus: The clinical status of the condition.

        verificationStatus: The verification status to support the clinical status of the condition.

        category: A category assigned to the condition.

        severity: A subjective assessment of the severity of the condition as evaluated by the
            clinician.

        code: Identification of the condition, problem or diagnosis.

        bodySite: The anatomical location where this condition manifests itself.

        subject: Indicates the patient or group who the condition record is associated with.

        encounter: The Encounter during which this Condition was created or to which the creation
            of this record is tightly associated.

        onsetDateTime: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetAge: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetPeriod: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetRange: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetString: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        abatementDateTime: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementAge: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementPeriod: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementRange: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementString: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        recordedDate: The recordedDate represents when this particular Condition record was created
            in the system, which is often a system-generated date.

        recorder: Individual who recorded the record and takes responsibility for its content.

        asserter: Individual who is making the condition statement.

        stage: Clinical stage or grade of a condition. May include formal severity
            assessments.

        evidence: Supporting evidence / manifestations that are the basis of the Condition's
            verification status, such as evidence that confirmed or refuted the condition.

        note: Additional information about the Condition. This is a general notes/comments
            entry  for description of the Condition, its diagnosis and prognosis.

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
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.condition_stage import Condition_Stage
        from spark_fhir_schemas.r4.complex_types.condition_evidence import Condition_Evidence
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Condition resource
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
                # Business identifiers assigned to this condition by the performer or other
                # systems which remain constant as the resource is updated and propagates from
                # server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The clinical status of the condition.
                StructField(
                    "clinicalStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The verification status to support the clinical status of the condition.
                StructField(
                    "verificationStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A category assigned to the condition.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A subjective assessment of the severity of the condition as evaluated by the
                # clinician.
                StructField(
                    "severity",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identification of the condition, problem or diagnosis.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The anatomical location where this condition manifests itself.
                StructField(
                    "bodySite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates the patient or group who the condition record is associated with.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Encounter during which this Condition was created or to which the creation
                # of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField("onsetDateTime", StringType(), True),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetAge", Age.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetRange", Range.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField("onsetString", StringType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementDateTime", StringType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementAge", Age.get_schema(recursion_depth + 1), True
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementString", StringType(), True),
                # The recordedDate represents when this particular Condition record was created
                # in the system, which is often a system-generated date.
                StructField(
                    "recordedDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Individual who recorded the record and takes responsibility for its content.
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                # Individual who is making the condition statement.
                StructField(
                    "asserter", Reference.get_schema(recursion_depth + 1), True
                ),
                # Clinical stage or grade of a condition. May include formal severity
                # assessments.
                StructField(
                    "stage",
                    ArrayType(Condition_Stage.get_schema(recursion_depth + 1)),
                    True
                ),
                # Supporting evidence / manifestations that are the basis of the Condition's
                # verification status, such as evidence that confirmed or refuted the condition.
                StructField(
                    "evidence",
                    ArrayType(
                        Condition_Evidence.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Additional information about the Condition. This is a general notes/comments
                # entry  for description of the Condition, its diagnosis and prognosis.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
