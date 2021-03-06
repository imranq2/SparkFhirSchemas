from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ClinicalImpressionSchema:
    """
    A record of a clinical assessment performed to determine what problem(s) may
    affect the patient and before planning the treatments or management strategies
    that are best to manage a patient's condition. Assessments are often 1:1 with
    a clinical consultation / encounter,  but this varies greatly depending on the
    clinical workflow. This resource is called "ClinicalImpression" rather than
    "ClinicalAssessment" to avoid confusion with the recording of assessment tools
    such as Apgar score.
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
        A record of a clinical assessment performed to determine what problem(s) may
        affect the patient and before planning the treatments or management strategies
        that are best to manage a patient's condition. Assessments are often 1:1 with
        a clinical consultation / encounter,  but this varies greatly depending on the
        clinical workflow. This resource is called "ClinicalImpression" rather than
        "ClinicalAssessment" to avoid confusion with the recording of assessment tools
        such as Apgar score.


        resourceType: This is a ClinicalImpression resource

        identifier: A unique identifier assigned to the clinical impression that remains
            consistent regardless of what server the impression is stored on.

        status: Identifies the workflow status of the assessment.

        code: Categorizes the type of clinical assessment performed.

        description: A summary of the context and/or cause of the assessment - why / where was it
            performed, and what patient events/status prompted it.

        subject: The patient or group of individuals assessed as part of this record.

        context: The encounter or episode of care this impression was created as part of.

        effectiveDateTime: The point in time or period over which the subject was assessed.

        effectivePeriod: The point in time or period over which the subject was assessed.

        date: Indicates when the documentation of the assessment was complete.

        assessor: The clinician performing the assessment.

        previous: A reference to the last assesment that was conducted bon this patient.
            Assessments are often/usually ongoing in nature; a care provider (practitioner
            or team) will make new assessments on an ongoing basis as new data arises or
            the patient's conditions changes.

        problem: This a list of the relevant problems/conditions for a patient.

        investigation: One or more sets of investigations (signs, symptions, etc.). The actual
            grouping of investigations vary greatly depending on the type and context of
            the assessment. These investigations may include data generated during the
            assessment process, or data previously generated and recorded that is
            pertinent to the outcomes.

        protocol: Reference to a specific published clinical protocol that was followed during
            this assessment, and/or that provides evidence in support of the diagnosis.

        summary: A text summary of the investigations and the diagnosis.

        finding: Specific findings or diagnoses that was considered likely or relevant to
            ongoing treatment.

        prognosisCodeableConcept: Estimate of likely outcome.

        prognosisReference: RiskAssessment expressing likely outcome.

        action: Action taken as part of assessment procedure.

        note: Commentary about the impression, typically recorded after the impression
            itself was made, though supplemental notes by the original author could also
            appear.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.clinicalimpression_investigation import ClinicalImpression_InvestigationSchema
        from spark_fhir_schemas.stu3.complex_types.clinicalimpression_finding import ClinicalImpression_FindingSchema
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema
        if (
            max_recursion_limit
            and nesting_list.count("ClinicalImpression") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ClinicalImpression"]
        schema = StructType(
            [
                # This is a ClinicalImpression resource
                StructField("resourceType", StringType(), True),
                # A unique identifier assigned to the clinical impression that remains
                # consistent regardless of what server the impression is stored on.
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
                # Identifies the workflow status of the assessment.
                StructField("status", StringType(), True),
                # Categorizes the type of clinical assessment performed.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A summary of the context and/or cause of the assessment - why / where was it
                # performed, and what patient events/status prompted it.
                StructField("description", StringType(), True),
                # The patient or group of individuals assessed as part of this record.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The encounter or episode of care this impression was created as part of.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The point in time or period over which the subject was assessed.
                StructField("effectiveDateTime", StringType(), True),
                # The point in time or period over which the subject was assessed.
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
                # Indicates when the documentation of the assessment was complete.
                StructField("date", StringType(), True),
                # The clinician performing the assessment.
                StructField(
                    "assessor",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A reference to the last assesment that was conducted bon this patient.
                # Assessments are often/usually ongoing in nature; a care provider (practitioner
                # or team) will make new assessments on an ongoing basis as new data arises or
                # the patient's conditions changes.
                StructField(
                    "previous",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # This a list of the relevant problems/conditions for a patient.
                StructField(
                    "problem",
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
                # One or more sets of investigations (signs, symptions, etc.). The actual
                # grouping of investigations vary greatly depending on the type and context of
                # the assessment. These investigations may include data generated during the
                # assessment process, or data previously generated and recorded that is
                # pertinent to the outcomes.
                StructField(
                    "investigation",
                    ArrayType(
                        ClinicalImpression_InvestigationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Reference to a specific published clinical protocol that was followed during
                # this assessment, and/or that provides evidence in support of the diagnosis.
                # A text summary of the investigations and the diagnosis.
                StructField("summary", StringType(), True),
                # Specific findings or diagnoses that was considered likely or relevant to
                # ongoing treatment.
                StructField(
                    "finding",
                    ArrayType(
                        ClinicalImpression_FindingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Estimate of likely outcome.
                StructField(
                    "prognosisCodeableConcept",
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
                # RiskAssessment expressing likely outcome.
                StructField(
                    "prognosisReference",
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
                # Action taken as part of assessment procedure.
                StructField(
                    "action",
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
                # Commentary about the impression, typically recorded after the impression
                # itself was made, though supplemental notes by the original author could also
                # appear.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
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
