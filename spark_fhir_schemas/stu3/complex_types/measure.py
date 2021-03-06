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
class MeasureSchema:
    """
    The Measure resource provides the definition of a quality measure.
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
        The Measure resource provides the definition of a quality measure.


        resourceType: This is a Measure resource

        url: An absolute URI that is used to identify this measure when it is referenced in
            a specification, model, design or an instance. This SHALL be a URL, SHOULD be
            globally unique, and SHOULD be an address at which this measure is (or will
            be) published. The URL SHOULD include the major version of the measure. For
            more information see [Technical and Business
            Versions](resource.html#versions).

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

        status: The status of this measure. Enables tracking the life-cycle of the content.

        experimental: A boolean value to indicate that this measure is authored for testing purposes
            (or education/evaluation/marketing), and is not intended to be used for
            genuine usage.

        date: The date  (and optionally time) when the measure was published. The date must
            change if and when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the measure changes.

        publisher: The name of the individual or organization that published the measure.

        description: A free text natural language description of the measure from a consumer's
            perspective.

        purpose: Explaination of why this measure is needed and why it has been designed as it
            has.

        usage: A detailed description of how the measure is used from a clinical perspective.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval, but doesn't change the original approval date.

        effectivePeriod: The period during which the measure content was or is planned to be in active
            use.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These terms may be used to assist with indexing and searching
            for appropriate measure instances.

        jurisdiction: A legal or geographic region in which the measure is intended to be used.

        topic: Descriptive topics related to the content of the measure. Topics provide a
            high-level categorization of the type of the measure that can be useful for
            filtering and searching.

        contributor: A contributor to the content of the measure, including authors, editors,
            reviewers, and endorsers.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        copyright: A copyright statement relating to the measure and/or its contents. Copyright
            statements are generally legal restrictions on the use and publishing of the
            measure.

        relatedArtifact: Related artifacts such as additional documentation, justification, or
            bibliographic references.

        library: A reference to a Library resource containing the formal logic used by the
            measure.

        disclaimer: Notices and disclaimers regarding the use of the measure, or related to
            intellectual property (such as code systems) referenced by the measure.

        scoring: Indicates how the calculation is performed for the measure, including
            proportion, ratio, continuous variable, and cohort. The value set is
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

        rationale: Provides a succint statement of the need for the measure. Usually includes
            statements pertaining to importance criterion: impact, gap in care, and
            evidence.

        clinicalRecommendationStatement: Provides a summary of relevant clinical guidelines or other clinical
            recommendations supporting the measure.

        improvementNotation: Information on whether an increase or decrease in score is the preferred
            result (e.g., a higher score indicates better quality OR a lower score
            indicates better quality OR quality is whthin a range).

        definition: Provides a description of an individual term used within the measure.

        guidance: Additional guidance for the measure including how it can be used in a clinical
            context, and the intent of the measure.

        set: The measure set, e.g. Preventive Care and Screening.

        group: A group of population criteria for the measure.

        supplementalData: The supplemental data criteria for the measure report, specified as either the
            name of a valid CQL expression within a referenced library, or a valid FHIR
            Resource Path.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.contributor import ContributorSchema
        from spark_fhir_schemas.stu3.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.stu3.complex_types.relatedartifact import RelatedArtifactSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.measure_group import Measure_GroupSchema
        from spark_fhir_schemas.stu3.complex_types.measure_supplementaldata import Measure_SupplementalDataSchema
        if (
            max_recursion_limit
            and nesting_list.count("Measure") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Measure"]
        schema = StructType(
            [
                # This is a Measure resource
                StructField("resourceType", StringType(), True),
                # An absolute URI that is used to identify this measure when it is referenced in
                # a specification, model, design or an instance. This SHALL be a URL, SHOULD be
                # globally unique, and SHOULD be an address at which this measure is (or will
                # be) published. The URL SHOULD include the major version of the measure. For
                # more information see [Technical and Business
                # Versions](resource.html#versions).
                StructField("url", StringType(), True),
                # A formal identifier that is used to identify this measure when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
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
                # The status of this measure. Enables tracking the life-cycle of the content.
                StructField("status", StringType(), True),
                # A boolean value to indicate that this measure is authored for testing purposes
                # (or education/evaluation/marketing), and is not intended to be used for
                # genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the measure was published. The date must
                # change if and when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the measure changes.
                StructField("date", StringType(), True),
                # The name of the individual or organization that published the measure.
                StructField("publisher", StringType(), True),
                # A free text natural language description of the measure from a consumer's
                # perspective.
                StructField("description", StringType(), True),
                # Explaination of why this measure is needed and why it has been designed as it
                # has.
                StructField("purpose", StringType(), True),
                # A detailed description of how the measure is used from a clinical perspective.
                StructField("usage", StringType(), True),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", StringType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval, but doesn't change the original approval date.
                StructField("lastReviewDate", StringType(), True),
                # The period during which the measure content was or is planned to be in active
                # use.
                StructField(
                    "effectivePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # for appropriate measure instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A legal or geographic region in which the measure is intended to be used.
                StructField(
                    "jurisdiction",
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
                # Descriptive topics related to the content of the measure. Topics provide a
                # high-level categorization of the type of the measure that can be useful for
                # filtering and searching.
                StructField(
                    "topic",
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
                # A contributor to the content of the measure, including authors, editors,
                # reviewers, and endorsers.
                StructField(
                    "contributor",
                    ArrayType(
                        ContributorSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A copyright statement relating to the measure and/or its contents. Copyright
                # statements are generally legal restrictions on the use and publishing of the
                # measure.
                StructField("copyright", StringType(), True),
                # Related artifacts such as additional documentation, justification, or
                # bibliographic references.
                StructField(
                    "relatedArtifact",
                    ArrayType(
                        RelatedArtifactSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A reference to a Library resource containing the formal logic used by the
                # measure.
                StructField(
                    "library",
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
                # Notices and disclaimers regarding the use of the measure, or related to
                # intellectual property (such as code systems) referenced by the measure.
                StructField("disclaimer", StringType(), True),
                # Indicates how the calculation is performed for the measure, including
                # proportion, ratio, continuous variable, and cohort. The value set is
                # extensible, allowing additional measure scoring types to be represented.
                StructField(
                    "scoring",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # If this is a composite measure, the scoring method used to combine the
                # component measures to determine the composite score.
                StructField(
                    "compositeScoring",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates whether the measure is used to examine a process, an outcome over
                # time, a patient-reported outcome, or a structure measure such as utilization.
                StructField(
                    "type",
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
                # A description of the risk adjustment factors that may impact the resulting
                # score for the measure and how they may be accounted for when computing and
                # reporting measure results.
                StructField("riskAdjustment", StringType(), True),
                # Describes how to combine the information calculated, based on logic in each of
                # several populations, into one summarized result.
                StructField("rateAggregation", StringType(), True),
                # Provides a succint statement of the need for the measure. Usually includes
                # statements pertaining to importance criterion: impact, gap in care, and
                # evidence.
                StructField("rationale", StringType(), True),
                # Provides a summary of relevant clinical guidelines or other clinical
                # recommendations supporting the measure.
                StructField(
                    "clinicalRecommendationStatement", StringType(), True
                ),
                # Information on whether an increase or decrease in score is the preferred
                # result (e.g., a higher score indicates better quality OR a lower score
                # indicates better quality OR quality is whthin a range).
                StructField("improvementNotation", StringType(), True),
                # Provides a description of an individual term used within the measure.
                # Additional guidance for the measure including how it can be used in a clinical
                # context, and the intent of the measure.
                StructField("guidance", StringType(), True),
                # The measure set, e.g. Preventive Care and Screening.
                StructField("set", StringType(), True),
                # A group of population criteria for the measure.
                StructField(
                    "group",
                    ArrayType(
                        Measure_GroupSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The supplemental data criteria for the measure report, specified as either the
                # name of a valid CQL expression within a referenced library, or a valid FHIR
                # Resource Path.
                StructField(
                    "supplementalData",
                    ArrayType(
                        Measure_SupplementalDataSchema.get_schema(
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
