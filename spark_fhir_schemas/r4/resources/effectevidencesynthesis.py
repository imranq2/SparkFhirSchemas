from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class EffectEvidenceSynthesis:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The EffectEvidenceSynthesis resource describes the difference in an outcome
        between exposures states in a population where the effect estimate is derived
        from a combination of research studies.


        resourceType: This is a EffectEvidenceSynthesis resource

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

        url: An absolute URI that is used to identify this effect evidence synthesis when
            it is referenced in a specification, model, design or an instance; also called
            its canonical identifier. This SHOULD be globally unique and SHOULD be a
            literal address at which at which an authoritative instance of this effect
            evidence synthesis is (or will be) published. This URL can be the target of a
            canonical reference. It SHALL remain the same when the effect evidence
            synthesis is stored on different servers.

        identifier: A formal identifier that is used to identify this effect evidence synthesis
            when it is represented in other formats, or referenced in a specification,
            model, design or an instance.

        version: The identifier that is used to identify this version of the effect evidence
            synthesis when it is referenced in a specification, model, design or instance.
            This is an arbitrary value managed by the effect evidence synthesis author and
            is not expected to be globally unique. For example, it might be a timestamp
            (e.g. yyyymmdd) if a managed version is not available. There is also no
            expectation that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the effect evidence synthesis. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.

        title: A short, descriptive, user-friendly title for the effect evidence synthesis.

        status: The status of this effect evidence synthesis. Enables tracking the life-cycle
            of the content.

        date: The date  (and optionally time) when the effect evidence synthesis was
            published. The date must change when the business version changes and it must
            change if the status code changes. In addition, it should change when the
            substantive content of the effect evidence synthesis changes.

        publisher: The name of the organization or individual that published the effect evidence
            synthesis.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the effect evidence synthesis from
            a consumer's perspective.

        note: A human-readable string to clarify or explain concepts about the resource.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate effect
            evidence synthesis instances.

        jurisdiction: A legal or geographic region in which the effect evidence synthesis is
            intended to be used.

        copyright: A copyright statement relating to the effect evidence synthesis and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the effect evidence synthesis.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the effect evidence synthesis content was or is
            planned to be in active use.

        topic: Descriptive topics related to the content of the EffectEvidenceSynthesis.
            Topics provide a high-level categorization grouping types of
            EffectEvidenceSynthesiss that can be useful for filtering and searching.

        author: An individiual or organization primarily involved in the creation and
            maintenance of the content.

        editor: An individual or organization primarily responsible for internal coherence of
            the content.

        reviewer: An individual or organization primarily responsible for review of some aspect
            of the content.

        endorser: An individual or organization responsible for officially endorsing the content
            for use in some setting.

        relatedArtifact: Related artifacts such as additional documentation, justification, or
            bibliographic references.

        synthesisType: Type of synthesis eg meta-analysis.

        studyType: Type of study eg randomized trial.

        population: A reference to a EvidenceVariable resource that defines the population for the
            research.

        exposure: A reference to a EvidenceVariable resource that defines the exposure for the
            research.

        exposureAlternative: A reference to a EvidenceVariable resource that defines the comparison
            exposure for the research.

        outcome: A reference to a EvidenceVariable resomece that defines the outcome for the
            research.

        sampleSize: A description of the size of the sample involved in the synthesis.

        resultsByExposure: A description of the results for each exposure considered in the effect
            estimate.

        effectEstimate: The estimated effect of the exposure variant.

        certainty: A description of the certainty of the effect estimate.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_samplesize import EffectEvidenceSynthesis_SampleSize
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_resultsbyexposure import EffectEvidenceSynthesis_ResultsByExposure
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_effectestimate import EffectEvidenceSynthesis_EffectEstimate
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_certainty import EffectEvidenceSynthesis_Certainty
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a EffectEvidenceSynthesis resource
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
                # An absolute URI that is used to identify this effect evidence synthesis when
                # it is referenced in a specification, model, design or an instance; also called
                # its canonical identifier. This SHOULD be globally unique and SHOULD be a
                # literal address at which at which an authoritative instance of this effect
                # evidence synthesis is (or will be) published. This URL can be the target of a
                # canonical reference. It SHALL remain the same when the effect evidence
                # synthesis is stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # A formal identifier that is used to identify this effect evidence synthesis
                # when it is represented in other formats, or referenced in a specification,
                # model, design or an instance.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The identifier that is used to identify this version of the effect evidence
                # synthesis when it is referenced in a specification, model, design or instance.
                # This is an arbitrary value managed by the effect evidence synthesis author and
                # is not expected to be globally unique. For example, it might be a timestamp
                # (e.g. yyyymmdd) if a managed version is not available. There is also no
                # expectation that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the effect evidence synthesis. This name
                # should be usable as an identifier for the module by machine processing
                # applications such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the effect evidence synthesis.
                StructField("title", StringType(), True),
                # The status of this effect evidence synthesis. Enables tracking the life-cycle
                # of the content.
                StructField("status", StringType(), True),
                # The date  (and optionally time) when the effect evidence synthesis was
                # published. The date must change when the business version changes and it must
                # change if the status code changes. In addition, it should change when the
                # substantive content of the effect evidence synthesis changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the effect evidence
                # synthesis.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the effect evidence synthesis from
                # a consumer's perspective.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # A human-readable string to clarify or explain concepts about the resource.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate effect
                # evidence synthesis instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the effect evidence synthesis is
                # intended to be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A copyright statement relating to the effect evidence synthesis and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the effect evidence synthesis.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", DateType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval but does not change the original approval date.
                StructField("lastReviewDate", DateType(), True),
                # The period during which the effect evidence synthesis content was or is
                # planned to be in active use.
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Descriptive topics related to the content of the EffectEvidenceSynthesis.
                # Topics provide a high-level categorization grouping types of
                # EffectEvidenceSynthesiss that can be useful for filtering and searching.
                StructField(
                    "topic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individiual or organization primarily involved in the creation and
                # maintenance of the content.
                StructField(
                    "author",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individual or organization primarily responsible for internal coherence of
                # the content.
                StructField(
                    "editor",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individual or organization primarily responsible for review of some aspect
                # of the content.
                StructField(
                    "reviewer",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individual or organization responsible for officially endorsing the content
                # for use in some setting.
                StructField(
                    "endorser",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # Related artifacts such as additional documentation, justification, or
                # bibliographic references.
                StructField(
                    "relatedArtifact",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                # Type of synthesis eg meta-analysis.
                StructField(
                    "synthesisType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Type of study eg randomized trial.
                StructField(
                    "studyType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A reference to a EvidenceVariable resource that defines the population for the
                # research.
                StructField(
                    "population", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # A reference to a EvidenceVariable resource that defines the exposure for the
                # research.
                StructField(
                    "exposure", Reference.get_schema(recursion_depth + 1), True
                ),
                # A reference to a EvidenceVariable resource that defines the comparison
                # exposure for the research.
                StructField(
                    "exposureAlternative",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A reference to a EvidenceVariable resomece that defines the outcome for the
                # research.
                StructField(
                    "outcome", Reference.get_schema(recursion_depth + 1), True
                ),
                # A description of the size of the sample involved in the synthesis.
                StructField(
                    "sampleSize",
                    EffectEvidenceSynthesis_SampleSize.
                    get_schema(recursion_depth + 1), True
                ),
                # A description of the results for each exposure considered in the effect
                # estimate.
                StructField(
                    "resultsByExposure",
                    ArrayType(
                        EffectEvidenceSynthesis_ResultsByExposure.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The estimated effect of the exposure variant.
                StructField(
                    "effectEstimate",
                    ArrayType(
                        EffectEvidenceSynthesis_EffectEstimate.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A description of the certainty of the effect estimate.
                StructField(
                    "certainty",
                    ArrayType(
                        EffectEvidenceSynthesis_Certainty.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
