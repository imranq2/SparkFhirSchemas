from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Measure:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The Measure resource provides the definition of a quality measure.


        resourceType: This is a Measure resource

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

        url: An absolute URI that is used to identify this measure when it is referenced in
            a specification, model, design or an instance; also called its canonical
            identifier. This SHOULD be globally unique and SHOULD be a literal address at
            which at which an authoritative instance of this measure is (or will be)
            published. This URL can be the target of a canonical reference. It SHALL
            remain the same when the measure is stored on different servers.

        identifier: A formal identifier that is used to identify this measure when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the measure when it is
            referenced in a specification, model, design or instance. This is an arbitrary
            value managed by the measure author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
            not available. There is also no expectation that versions can be placed in a
            lexicographical sequence. To provide a version consistent with the Decision
            Support Service specification, use the format Major.Minor.Revision (e.g.
            1.0.0). For more information on versioning knowledge assets, refer to the
            Decision Support Service specification. Note that a version is required for
            non-experimental active artifacts.

        name: A natural language name identifying the measure. This name should be usable as
            an identifier for the module by machine processing applications such as code
            generation.

        title: A short, descriptive, user-friendly title for the measure.

        subtitle: An explanatory or alternate title for the measure giving additional
            information about its content.

        status: The status of this measure. Enables tracking the life-cycle of the content.

        experimental: A Boolean value to indicate that this measure is authored for testing purposes
            (or education/evaluation/marketing) and is not intended to be used for genuine
            usage.

        subjectCodeableConcept: The intended subjects for the measure. If this element is not provided, a
            Patient subject is assumed, but the subject of the measure can be anything.

        subjectReference: The intended subjects for the measure. If this element is not provided, a
            Patient subject is assumed, but the subject of the measure can be anything.

        date: The date  (and optionally time) when the measure was published. The date must
            change when the business version changes and it must change if the status code
            changes. In addition, it should change when the substantive content of the
            measure changes.

        publisher: The name of the organization or individual that published the measure.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the measure from a consumer's
            perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate measure
            instances.

        jurisdiction: A legal or geographic region in which the measure is intended to be used.

        purpose: Explanation of why this measure is needed and why it has been designed as it
            has.

        usage: A detailed description, from a clinical perspective, of how the measure is
            used.

        copyright: A copyright statement relating to the measure and/or its contents. Copyright
            statements are generally legal restrictions on the use and publishing of the
            measure.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the measure content was or is planned to be in active
            use.

        topic: Descriptive topics related to the content of the measure. Topics provide a
            high-level categorization grouping types of measures that can be useful for
            filtering and searching.

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

        library: A reference to a Library resource containing the formal logic used by the
            measure.

        disclaimer: Notices and disclaimers regarding the use of the measure or related to
            intellectual property (such as code systems) referenced by the measure.

        scoring: Indicates how the calculation is performed for the measure, including
            proportion, ratio, continuous-variable, and cohort. The value set is
            extensible, allowing additional measure scoring types to be represented.

        compositeScoring: If this is a composite measure, the scoring method used to combine the
            component measures to determine the composite score.

        type: Indicates whether the measure is used to examine a process, an outcome over
            time, a patient-reported outcome, or a structure measure such as utilization.

        riskAdjustment: A description of the risk adjustment factors that may impact the resulting
            score for the measure and how they may be accounted for when computing and
            reporting measure results.

        rateAggregation: Describes how to combine the information calculated, based on logic in each of
            several populations, into one summarized result.

        rationale: Provides a succinct statement of the need for the measure. Usually includes
            statements pertaining to importance criterion: impact, gap in care, and
            evidence.

        clinicalRecommendationStatement: Provides a summary of relevant clinical guidelines or other clinical
            recommendations supporting the measure.

        improvementNotation: Information on whether an increase or decrease in score is the preferred
            result (e.g., a higher score indicates better quality OR a lower score
            indicates better quality OR quality is within a range).

        definition: Provides a description of an individual term used within the measure.

        guidance: Additional guidance for the measure including how it can be used in a clinical
            context, and the intent of the measure.

        group: A group of population criteria for the measure.

        supplementalData: The supplemental data criteria for the measure report, specified as either the
            name of a valid CQL expression within a referenced library, or a valid FHIR
            Resource Path.

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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.measure_group import Measure_Group
        from spark_fhir_schemas.r4.complex_types.measure_supplementaldata import Measure_SupplementalData
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Measure resource
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
                # An absolute URI that is used to identify this measure when it is referenced in
                # a specification, model, design or an instance; also called its canonical
                # identifier. This SHOULD be globally unique and SHOULD be a literal address at
                # which at which an authoritative instance of this measure is (or will be)
                # published. This URL can be the target of a canonical reference. It SHALL
                # remain the same when the measure is stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # A formal identifier that is used to identify this measure when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The identifier that is used to identify this version of the measure when it is
                # referenced in a specification, model, design or instance. This is an arbitrary
                # value managed by the measure author and is not expected to be globally unique.
                # For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
                # not available. There is also no expectation that versions can be placed in a
                # lexicographical sequence. To provide a version consistent with the Decision
                # Support Service specification, use the format Major.Minor.Revision (e.g.
                # 1.0.0). For more information on versioning knowledge assets, refer to the
                # Decision Support Service specification. Note that a version is required for
                # non-experimental active artifacts.
                StructField("version", StringType(), True),
                # A natural language name identifying the measure. This name should be usable as
                # an identifier for the module by machine processing applications such as code
                # generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the measure.
                StructField("title", StringType(), True),
                # An explanatory or alternate title for the measure giving additional
                # information about its content.
                StructField("subtitle", StringType(), True),
                # The status of this measure. Enables tracking the life-cycle of the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this measure is authored for testing purposes
                # (or education/evaluation/marketing) and is not intended to be used for genuine
                # usage.
                StructField("experimental", BooleanType(), True),
                # The intended subjects for the measure. If this element is not provided, a
                # Patient subject is assumed, but the subject of the measure can be anything.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The intended subjects for the measure. If this element is not provided, a
                # Patient subject is assumed, but the subject of the measure can be anything.
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The date  (and optionally time) when the measure was published. The date must
                # change when the business version changes and it must change if the status code
                # changes. In addition, it should change when the substantive content of the
                # measure changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the measure.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the measure from a consumer's
                # perspective.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate measure
                # instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the measure is intended to be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Explanation of why this measure is needed and why it has been designed as it
                # has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # A detailed description, from a clinical perspective, of how the measure is
                # used.
                StructField("usage", StringType(), True),
                # A copyright statement relating to the measure and/or its contents. Copyright
                # statements are generally legal restrictions on the use and publishing of the
                # measure.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", DateType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval but does not change the original approval date.
                StructField("lastReviewDate", DateType(), True),
                # The period during which the measure content was or is planned to be in active
                # use.
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Descriptive topics related to the content of the measure. Topics provide a
                # high-level categorization grouping types of measures that can be useful for
                # filtering and searching.
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
                # A reference to a Library resource containing the formal logic used by the
                # measure.
                StructField(
                    "library",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # Notices and disclaimers regarding the use of the measure or related to
                # intellectual property (such as code systems) referenced by the measure.
                StructField(
                    "disclaimer", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates how the calculation is performed for the measure, including
                # proportion, ratio, continuous-variable, and cohort. The value set is
                # extensible, allowing additional measure scoring types to be represented.
                StructField(
                    "scoring", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # If this is a composite measure, the scoring method used to combine the
                # component measures to determine the composite score.
                StructField(
                    "compositeScoring",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates whether the measure is used to examine a process, an outcome over
                # time, a patient-reported outcome, or a structure measure such as utilization.
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A description of the risk adjustment factors that may impact the resulting
                # score for the measure and how they may be accounted for when computing and
                # reporting measure results.
                StructField("riskAdjustment", StringType(), True),
                # Describes how to combine the information calculated, based on logic in each of
                # several populations, into one summarized result.
                StructField("rateAggregation", StringType(), True),
                # Provides a succinct statement of the need for the measure. Usually includes
                # statements pertaining to importance criterion: impact, gap in care, and
                # evidence.
                StructField(
                    "rationale", markdown.get_schema(recursion_depth + 1), True
                ),
                # Provides a summary of relevant clinical guidelines or other clinical
                # recommendations supporting the measure.
                StructField(
                    "clinicalRecommendationStatement",
                    markdown.get_schema(recursion_depth + 1), True
                ),
                # Information on whether an increase or decrease in score is the preferred
                # result (e.g., a higher score indicates better quality OR a lower score
                # indicates better quality OR quality is within a range).
                StructField(
                    "improvementNotation",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Provides a description of an individual term used within the measure.
                StructField(
                    "definition",
                    ArrayType(markdown.get_schema(recursion_depth + 1)), True
                ),
                # Additional guidance for the measure including how it can be used in a clinical
                # context, and the intent of the measure.
                StructField(
                    "guidance", markdown.get_schema(recursion_depth + 1), True
                ),
                # A group of population criteria for the measure.
                StructField(
                    "group",
                    ArrayType(Measure_Group.get_schema(recursion_depth + 1)),
                    True
                ),
                # The supplemental data criteria for the measure report, specified as either the
                # name of a valid CQL expression within a referenced library, or a valid FHIR
                # Resource Path.
                StructField(
                    "supplementalData",
                    ArrayType(
                        Measure_SupplementalData.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
