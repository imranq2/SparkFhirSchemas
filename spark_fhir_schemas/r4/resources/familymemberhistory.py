from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class FamilyMemberHistorySchema:
    """
    Significant health conditions for a person related to the patient relevant in
    the context of care for the patient.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Significant health conditions for a person related to the patient relevant in
        the context of care for the patient.


        resourceType: This is a FamilyMemberHistory resource

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

        identifier: Business identifiers assigned to this family member history by the performer
            or other systems which remain constant as the resource is updated and
            propagates from server to server.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this FamilyMemberHistory.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            FamilyMemberHistory.

        status: A code specifying the status of the record of the family history of a specific
            family member.

        dataAbsentReason: Describes why the family member's history is not available.

        patient: The person who this history concerns.

        date: The date (and possibly time) when the family member history was recorded or
            last updated.

        name: This will either be a name or a description; e.g. "Aunt Susan", "my cousin
            with the red hair".

        relationship: The type of relationship this person has to the patient (father, mother,
            brother etc.).

        sex: The birth sex of the family member.

        bornPeriod: The actual or approximate date of birth of the relative.

        bornDate: The actual or approximate date of birth of the relative.

        bornString: The actual or approximate date of birth of the relative.

        ageAge: The age of the relative at the time the family member history is recorded.

        ageRange: The age of the relative at the time the family member history is recorded.

        ageString: The age of the relative at the time the family member history is recorded.

        estimatedAge: If true, indicates that the age value specified is an estimated value.

        deceasedBoolean: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedAge: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedRange: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedDate: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedString: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        reasonCode: Describes why the family member history occurred in coded or textual form.

        reasonReference: Indicates a Condition, Observation, AllergyIntolerance, or
            QuestionnaireResponse that justifies this family member history event.

        note: This property allows a non condition-specific note to the made about the
            related person. Ideally, the note would be in the condition property, but this
            is not always possible.

        condition: The significant Conditions (or condition) that the family member had. This is
            a repeating section to allow a system to represent more than one condition per
            resource, though there is nothing stopping multiple resources - one per
            condition.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.age import AgeSchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.r4.complex_types.familymemberhistory_condition import FamilyMemberHistory_ConditionSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a FamilyMemberHistory resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id", idSchema.get_schema(recursion_depth + 1), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", MetaSchema.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uriSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", codeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", NarrativeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Business identifiers assigned to this family member history by the performer
                # or other systems which remain constant as the resource is updated and
                # propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this FamilyMemberHistory.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonicalSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # FamilyMemberHistory.
                StructField(
                    "instantiatesUri",
                    ArrayType(uriSchema.get_schema(recursion_depth + 1)), True
                ),
                # A code specifying the status of the record of the family history of a specific
                # family member.
                StructField("status", StringType(), True),
                # Describes why the family member's history is not available.
                StructField(
                    "dataAbsentReason",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The person who this history concerns.
                StructField(
                    "patient", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The date (and possibly time) when the family member history was recorded or
                # last updated.
                StructField(
                    "date", dateTimeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # This will either be a name or a description; e.g. "Aunt Susan", "my cousin
                # with the red hair".
                StructField("name", StringType(), True),
                # The type of relationship this person has to the patient (father, mother,
                # brother etc.).
                StructField(
                    "relationship",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The birth sex of the family member.
                StructField(
                    "sex",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The actual or approximate date of birth of the relative.
                StructField(
                    "bornPeriod", PeriodSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual or approximate date of birth of the relative.
                StructField("bornDate", StringType(), True),
                # The actual or approximate date of birth of the relative.
                StructField("bornString", StringType(), True),
                # The age of the relative at the time the family member history is recorded.
                StructField(
                    "ageAge", AgeSchema.get_schema(recursion_depth + 1), True
                ),
                # The age of the relative at the time the family member history is recorded.
                StructField(
                    "ageRange", RangeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The age of the relative at the time the family member history is recorded.
                StructField("ageString", StringType(), True),
                # If true, indicates that the age value specified is an estimated value.
                StructField("estimatedAge", BooleanType(), True),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField("deceasedBoolean", BooleanType(), True),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField(
                    "deceasedAge", AgeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField(
                    "deceasedRange",
                    RangeSchema.get_schema(recursion_depth + 1), True
                ),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField("deceasedDate", StringType(), True),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField("deceasedString", StringType(), True),
                # Describes why the family member history occurred in coded or textual form.
                StructField(
                    "reasonCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Indicates a Condition, Observation, AllergyIntolerance, or
                # QuestionnaireResponse that justifies this family member history event.
                StructField(
                    "reasonReference",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # This property allows a non condition-specific note to the made about the
                # related person. Ideally, the note would be in the condition property, but this
                # is not always possible.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The significant Conditions (or condition) that the family member had. This is
                # a repeating section to allow a system to represent more than one condition per
                # resource, though there is nothing stopping multiple resources - one per
                # condition.
                StructField(
                    "condition",
                    ArrayType(
                        FamilyMemberHistory_ConditionSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
