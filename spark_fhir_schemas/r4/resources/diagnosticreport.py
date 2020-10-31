from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DiagnosticReport:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The findings and interpretation of diagnostic  tests performed on patients,
        groups of patients, devices, and locations, and/or specimens derived from
        these. The report includes clinical context such as requesting and provider
        information, and some mix of atomic results, images, textual and coded
        interpretations, and formatted representation of diagnostic reports.


        resourceType: This is a DiagnosticReport resource

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

        identifier: Identifiers assigned to this report by the performer or other systems.

        basedOn: Details concerning a service requested.

        status: The status of the diagnostic report.

        category: A code that classifies the clinical discipline, department or diagnostic
            service that created the report (e.g. cardiology, biochemistry, hematology,
            MRI). This is used for searching, sorting and display purposes.

        code: A code or name that describes this diagnostic report.

        subject: The subject of the report. Usually, but not always, this is a patient.
            However, diagnostic services also perform analyses on specimens collected from
            a variety of other sources.

        encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
            which this DiagnosticReport is about.

        effectiveDateTime: The time or time-period the observed values are related to. When the subject
            of the report is a patient, this is usually either the time of the procedure
            or of specimen collection(s), but very often the source of the date/time is
            not known, only the date/time itself.

        effectivePeriod: The time or time-period the observed values are related to. When the subject
            of the report is a patient, this is usually either the time of the procedure
            or of specimen collection(s), but very often the source of the date/time is
            not known, only the date/time itself.

        issued: The date and time that this version of the report was made available to
            providers, typically after the report was reviewed and verified.

        performer: The diagnostic service that is responsible for issuing the report.

        resultsInterpreter: The practitioner or organization that is responsible for the report's
            conclusions and interpretations.

        specimen: Details about the specimens on which this diagnostic report is based.

        result: [Observations](observation.html)  that are part of this diagnostic report.

        imagingStudy: One or more links to full details of any imaging performed during the
            diagnostic investigation. Typically, this is imaging performed by DICOM
            enabled modalities, but this is not required. A fully enabled PACS viewer can
            use this information to provide views of the source images.

        media: A list of key images associated with this report. The images are generally
            created during the diagnostic process, and may be directly of the patient, or
            of treated specimens (i.e. slides of interest).

        conclusion: Concise and clinically contextualized summary conclusion
            (interpretation/impression) of the diagnostic report.

        conclusionCode: One or more codes that represent the summary conclusion
            (interpretation/impression) of the diagnostic report.

        presentedForm: Rich text representation of the entire result as issued by the diagnostic
            service. Multiple formats are allowed but they SHALL be semantically
            equivalent.

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
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.diagnosticreport_media import DiagnosticReport_Media
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a DiagnosticReport resource
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
                # Identifiers assigned to this report by the performer or other systems.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Details concerning a service requested.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The status of the diagnostic report.
                StructField("status", StringType(), True),
                # A code that classifies the clinical discipline, department or diagnostic
                # service that created the report (e.g. cardiology, biochemistry, hematology,
                # MRI). This is used for searching, sorting and display purposes.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A code or name that describes this diagnostic report.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The subject of the report. Usually, but not always, this is a patient.
                # However, diagnostic services also perform analyses on specimens collected from
                # a variety of other sources.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The healthcare event  (e.g. a patient and healthcare provider interaction)
                # which this DiagnosticReport is about.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
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
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date and time that this version of the report was made available to
                # providers, typically after the report was reviewed and verified.
                StructField(
                    "issued", instant.get_schema(recursion_depth + 1), True
                ),
                # The diagnostic service that is responsible for issuing the report.
                StructField(
                    "performer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The practitioner or organization that is responsible for the report's
                # conclusions and interpretations.
                StructField(
                    "resultsInterpreter",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Details about the specimens on which this diagnostic report is based.
                StructField(
                    "specimen",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # [Observations](observation.html)  that are part of this diagnostic report.
                StructField(
                    "result",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # One or more links to full details of any imaging performed during the
                # diagnostic investigation. Typically, this is imaging performed by DICOM
                # enabled modalities, but this is not required. A fully enabled PACS viewer can
                # use this information to provide views of the source images.
                StructField(
                    "imagingStudy",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A list of key images associated with this report. The images are generally
                # created during the diagnostic process, and may be directly of the patient, or
                # of treated specimens (i.e. slides of interest).
                StructField(
                    "media",
                    ArrayType(
                        DiagnosticReport_Media.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Concise and clinically contextualized summary conclusion
                # (interpretation/impression) of the diagnostic report.
                StructField("conclusion", StringType(), True),
                # One or more codes that represent the summary conclusion
                # (interpretation/impression) of the diagnostic report.
                StructField(
                    "conclusionCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Rich text representation of the entire result as issued by the diagnostic
                # service. Multiple formats are allowed but they SHALL be semantically
                # equivalent.
                StructField(
                    "presentedForm",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
