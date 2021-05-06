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
class DiagnosticReportSchema:
    """
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
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
        The findings and interpretation of diagnostic  tests performed on patients,
        groups of patients, devices, and locations, and/or specimens derived from
        these. The report includes clinical context such as requesting and provider
        information, and some mix of atomic results, images, textual and coded
        interpretations, and formatted representation of diagnostic reports.


        resourceType: This is a DiagnosticReport resource

        identifier: Identifiers assigned to this report by the performer or other systems.

        basedOn: Details concerning a test or procedure requested.

        status: The status of the diagnostic report as a whole.

        category: A code that classifies the clinical discipline, department or diagnostic
            service that created the report (e.g. cardiology, biochemistry, hematology,
            MRI). This is used for searching, sorting and display purposes.

        code: A code or name that describes this diagnostic report.

        subject: The subject of the report. Usually, but not always, this is a patient. However
            diagnostic services also perform analyses on specimens collected from a
            variety of other sources.

        context: The healthcare event  (e.g. a patient and healthcare provider interaction)
            which this DiagnosticReport per is about.

        effectiveDateTime: The time or time-period the observed values are related to. When the subject
            of the report is a patient, this is usually either the time of the procedure
            or of specimen collection(s), but very often the source of the date/time is
            not known, only the date/time itself.

        effectivePeriod: The time or time-period the observed values are related to. When the subject
            of the report is a patient, this is usually either the time of the procedure
            or of specimen collection(s), but very often the source of the date/time is
            not known, only the date/time itself.

        issued: The date and time that this version of the report was released from the source
            diagnostic service.

        performer: Indicates who or what participated in producing the report.

        specimen: Details about the specimens on which this diagnostic report is based.

        result: Observations that are part of this diagnostic report. Observations can be
            simple name/value pairs (e.g. "atomic" results), or they can be grouping
            observations that include references to other members of the group (e.g.
            "panels").

        imagingStudy: One or more links to full details of any imaging performed during the
            diagnostic investigation. Typically, this is imaging performed by DICOM
            enabled modalities, but this is not required. A fully enabled PACS viewer can
            use this information to provide views of the source images.

        image: A list of key images associated with this report. The images are generally
            created during the diagnostic process, and may be directly of the patient, or
            of treated specimens (i.e. slides of interest).

        conclusion: Concise and clinically contextualized impression / summary of the diagnostic
            report.

        codedDiagnosis: Codes for the conclusion.

        presentedForm: Rich text representation of the entire result as issued by the diagnostic
            service. Multiple formats are allowed but they SHALL be semantically
            equivalent.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.diagnosticreport_performer import DiagnosticReport_PerformerSchema
        from spark_fhir_schemas.stu3.complex_types.diagnosticreport_image import DiagnosticReport_ImageSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        if (
            max_recursion_limit
            and nesting_list.count("DiagnosticReport") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DiagnosticReport"]
        schema = StructType(
            [
                # This is a DiagnosticReport resource
                StructField("resourceType", StringType(), True),
                # Identifiers assigned to this report by the performer or other systems.
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
                # Details concerning a test or procedure requested.
                StructField(
                    "basedOn",
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
                # The status of the diagnostic report as a whole.
                StructField("status", StringType(), True),
                # A code that classifies the clinical discipline, department or diagnostic
                # service that created the report (e.g. cardiology, biochemistry, hematology,
                # MRI). This is used for searching, sorting and display purposes.
                StructField(
                    "category",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A code or name that describes this diagnostic report.
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
                # The subject of the report. Usually, but not always, this is a patient. However
                # diagnostic services also perform analyses on specimens collected from a
                # variety of other sources.
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
                # The healthcare event  (e.g. a patient and healthcare provider interaction)
                # which this DiagnosticReport per is about.
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
                # The time or time-period the observed values are related to. When the subject
                # of the report is a patient, this is usually either the time of the procedure
                # or of specimen collection(s), but very often the source of the date/time is
                # not known, only the date/time itself.
                StructField("effectiveDateTime", StringType(), True),
                # The time or time-period the observed values are related to. When the subject
                # of the report is a patient, this is usually either the time of the procedure
                # or of specimen collection(s), but very often the source of the date/time is
                # not known, only the date/time itself.
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
                # The date and time that this version of the report was released from the source
                # diagnostic service.
                StructField("issued", StringType(), True),
                # Indicates who or what participated in producing the report.
                StructField(
                    "performer",
                    ArrayType(
                        DiagnosticReport_PerformerSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Details about the specimens on which this diagnostic report is based.
                StructField(
                    "specimen",
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
                # Observations that are part of this diagnostic report. Observations can be
                # simple name/value pairs (e.g. "atomic" results), or they can be grouping
                # observations that include references to other members of the group (e.g.
                # "panels").
                StructField(
                    "result",
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
                # One or more links to full details of any imaging performed during the
                # diagnostic investigation. Typically, this is imaging performed by DICOM
                # enabled modalities, but this is not required. A fully enabled PACS viewer can
                # use this information to provide views of the source images.
                StructField(
                    "imagingStudy",
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
                # A list of key images associated with this report. The images are generally
                # created during the diagnostic process, and may be directly of the patient, or
                # of treated specimens (i.e. slides of interest).
                StructField(
                    "image",
                    ArrayType(
                        DiagnosticReport_ImageSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Concise and clinically contextualized impression / summary of the diagnostic
                # report.
                StructField("conclusion", StringType(), True),
                # Codes for the conclusion.
                StructField(
                    "codedDiagnosis",
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
                # Rich text representation of the entire result as issued by the diagnostic
                # service. Multiple formats are allowed but they SHALL be semantically
                # equivalent.
                StructField(
                    "presentedForm",
                    ArrayType(
                        AttachmentSchema.get_schema(
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
