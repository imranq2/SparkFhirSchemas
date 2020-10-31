from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ResearchStudy:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A process where a researcher or organization plans and then executes a series
        of steps intended to increase the field of healthcare-related knowledge.  This
        includes studies of safety, efficacy, comparative effectiveness and other
        information about medications, devices, therapies and other interventional and
        investigative techniques.  A ResearchStudy involves the gathering of
        information about human or animal subjects.


        resourceType: This is a ResearchStudy resource

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

        identifier: Identifiers assigned to this research study by the sponsor or other systems.

        title: A short, descriptive user-friendly label for the study.

        protocol: The set of steps expected to be performed as part of the execution of the
            study.

        partOf: A larger research study of which this particular study is a component or step.

        status: The current state of the study.

        primaryPurposeType: The type of study based upon the intent of the study's activities. A
            classification of the intent of the study.

        phase: The stage in the progression of a therapy from initial experimental use in
            humans in clinical trials to post-market evaluation.

        category: Codes categorizing the type of study such as investigational vs.
            observational, type of blinding, type of randomization, safety vs. efficacy,
            etc.

        focus: The medication(s), food(s), therapy(ies), device(s) or other concerns or
            interventions that the study is seeking to gain more information about.

        condition: The condition that is the focus of the study.  For example, In a study to
            examine risk factors for Lupus, might have as an inclusion criterion "healthy
            volunteer", but the target condition code would be a Lupus SNOMED code.

        contact: Contact details to assist a user in learning more about or engaging with the
            study.

        relatedArtifact: Citations, references and other related documents.

        keyword: Key terms to aid in searching for or filtering the study.

        location: Indicates a country, state or other region where the study is taking place.

        description: A full description of how the study is being conducted.

        enrollment: Reference to a Group that defines the criteria for and quantity of subjects
            participating in the study.  E.g. " 200 female Europeans between the ages of
            20 and 45 with early onset diabetes".

        period: Identifies the start date and the expected (or actual, depending on status)
            end date for the study.

        sponsor: An organization that initiates the investigation and is legally responsible
            for the study.

        principalInvestigator: A researcher in a study who oversees multiple aspects of the study, such as
            concept development, protocol writing, protocol submission for IRB approval,
            participant recruitment, informed consent, data collection, analysis,
            interpretation and presentation.

        site: A facility in which study activities are conducted.

        reasonStopped: A description and/or code explaining the premature termination of the study.

        note: Comments made about the study by the performer, subject or other participants.

        arm: Describes an expected sequence of events for one of the participants of a
            study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
            follow-up.

        objective: A goal that the study is aiming to achieve in terms of a scientific question
            to be answered by the analysis of data collected during the study.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.researchstudy_arm import ResearchStudy_Arm
        from spark_fhir_schemas.r4.complex_types.researchstudy_objective import ResearchStudy_Objective
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ResearchStudy resource
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
                # Identifiers assigned to this research study by the sponsor or other systems.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # A short, descriptive user-friendly label for the study.
                StructField("title", StringType(), True),
                # The set of steps expected to be performed as part of the execution of the
                # study.
                StructField(
                    "protocol",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A larger research study of which this particular study is a component or step.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The current state of the study.
                StructField("status", StringType(), True),
                # The type of study based upon the intent of the study's activities. A
                # classification of the intent of the study.
                StructField(
                    "primaryPurposeType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The stage in the progression of a therapy from initial experimental use in
                # humans in clinical trials to post-market evaluation.
                StructField(
                    "phase", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Codes categorizing the type of study such as investigational vs.
                # observational, type of blinding, type of randomization, safety vs. efficacy,
                # etc.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The medication(s), food(s), therapy(ies), device(s) or other concerns or
                # interventions that the study is seeking to gain more information about.
                StructField(
                    "focus",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The condition that is the focus of the study.  For example, In a study to
                # examine risk factors for Lupus, might have as an inclusion criterion "healthy
                # volunteer", but the target condition code would be a Lupus SNOMED code.
                StructField(
                    "condition",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Contact details to assist a user in learning more about or engaging with the
                # study.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # Citations, references and other related documents.
                StructField(
                    "relatedArtifact",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                # Key terms to aid in searching for or filtering the study.
                StructField(
                    "keyword",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates a country, state or other region where the study is taking place.
                StructField(
                    "location",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A full description of how the study is being conducted.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # Reference to a Group that defines the criteria for and quantity of subjects
                # participating in the study.  E.g. " 200 female Europeans between the ages of
                # 20 and 45 with early onset diabetes".
                StructField(
                    "enrollment",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the start date and the expected (or actual, depending on status)
                # end date for the study.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # An organization that initiates the investigation and is legally responsible
                # for the study.
                StructField(
                    "sponsor", Reference.get_schema(recursion_depth + 1), True
                ),
                # A researcher in a study who oversees multiple aspects of the study, such as
                # concept development, protocol writing, protocol submission for IRB approval,
                # participant recruitment, informed consent, data collection, analysis,
                # interpretation and presentation.
                StructField(
                    "principalInvestigator",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A facility in which study activities are conducted.
                StructField(
                    "site",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A description and/or code explaining the premature termination of the study.
                StructField(
                    "reasonStopped",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Comments made about the study by the performer, subject or other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Describes an expected sequence of events for one of the participants of a
                # study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
                # follow-up.
                StructField(
                    "arm",
                    ArrayType(
                        ResearchStudy_Arm.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A goal that the study is aiming to achieve in terms of a scientific question
                # to be answered by the analysis of data collected during the study.
                StructField(
                    "objective",
                    ArrayType(
                        ResearchStudy_Objective.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
