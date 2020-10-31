from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImagingStudy:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Representation of the content produced in a DICOM imaging study. A study
        comprises a set of series, each of which includes a set of Service-Object Pair
        Instances (SOP Instances - images or other data) acquired or produced in a
        common context.  A series is of only one modality (e.g. X-ray, CT, MR,
        ultrasound), but a study may have multiple series of different modalities.


        resourceType: This is a ImagingStudy resource

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

        identifier: Identifiers for the ImagingStudy such as DICOM Study Instance UID, and
            Accession Number.

        status: The current state of the ImagingStudy.

        modality: A list of all the series.modality values that are actual acquisition
            modalities, i.e. those in the DICOM Context Group 29 (value set OID
            1.2.840.10008.6.1.19).

        subject: The subject, typically a patient, of the imaging study.

        encounter: The healthcare event (e.g. a patient and healthcare provider interaction)
            during which this ImagingStudy is made.

        started: Date and time the study started.

        basedOn: A list of the diagnostic requests that resulted in this imaging study being
            performed.

        referrer: The requesting/referring physician.

        interpreter: Who read the study and interpreted the images or other content.

        endpoint: The network service providing access (e.g., query, view, or retrieval) for the
            study. See implementation notes for information about using DICOM endpoints. A
            study-level endpoint applies to each series in the study, unless overridden by
            a series-level endpoint with the same Endpoint.connectionType.

        numberOfSeries: Number of Series in the Study. This value given may be larger than the number
            of series elements this Resource contains due to resource availability,
            security, or other factors. This element should be present if any series
            elements are present.

        numberOfInstances: Number of SOP Instances in Study. This value given may be larger than the
            number of instance elements this resource contains due to resource
            availability, security, or other factors. This element should be present if
            any instance elements are present.

        procedureReference: The procedure which this ImagingStudy was part of.

        procedureCode: The code for the performed procedure type.

        location: The principal physical location where the ImagingStudy was performed.

        reasonCode: Description of clinical condition indicating why the ImagingStudy was
            requested.

        reasonReference: Indicates another resource whose existence justifies this Study.

        note: Per the recommended DICOM mapping, this element is derived from the Study
            Description attribute (0008,1030). Observations or findings about the imaging
            study should be recorded in another resource, e.g. Observation, and not in
            this element.

        description: The Imaging Manager description of the study. Institution-generated
            description or classification of the Study (component) performed.

        series: Each study has one or more series of images or other content.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.imagingstudy_series import ImagingStudy_Series
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ImagingStudy resource
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
                # Identifiers for the ImagingStudy such as DICOM Study Instance UID, and
                # Accession Number.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The current state of the ImagingStudy.
                StructField("status", StringType(), True),
                # A list of all the series.modality values that are actual acquisition
                # modalities, i.e. those in the DICOM Context Group 29 (value set OID
                # 1.2.840.10008.6.1.19).
                StructField(
                    "modality",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                # The subject, typically a patient, of the imaging study.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The healthcare event (e.g. a patient and healthcare provider interaction)
                # during which this ImagingStudy is made.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Date and time the study started.
                StructField(
                    "started", dateTime.get_schema(recursion_depth + 1), True
                ),
                # A list of the diagnostic requests that resulted in this imaging study being
                # performed.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The requesting/referring physician.
                StructField(
                    "referrer", Reference.get_schema(recursion_depth + 1), True
                ),
                # Who read the study and interpreted the images or other content.
                StructField(
                    "interpreter",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The network service providing access (e.g., query, view, or retrieval) for the
                # study. See implementation notes for information about using DICOM endpoints. A
                # study-level endpoint applies to each series in the study, unless overridden by
                # a series-level endpoint with the same Endpoint.connectionType.
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Number of Series in the Study. This value given may be larger than the number
                # of series elements this Resource contains due to resource availability,
                # security, or other factors. This element should be present if any series
                # elements are present.
                StructField(
                    "numberOfSeries",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # Number of SOP Instances in Study. This value given may be larger than the
                # number of instance elements this resource contains due to resource
                # availability, security, or other factors. This element should be present if
                # any instance elements are present.
                StructField(
                    "numberOfInstances",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # The procedure which this ImagingStudy was part of.
                StructField(
                    "procedureReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The code for the performed procedure type.
                StructField(
                    "procedureCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The principal physical location where the ImagingStudy was performed.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # Description of clinical condition indicating why the ImagingStudy was
                # requested.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource whose existence justifies this Study.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Per the recommended DICOM mapping, this element is derived from the Study
                # Description attribute (0008,1030). Observations or findings about the imaging
                # study should be recorded in another resource, e.g. Observation, and not in
                # this element.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # The Imaging Manager description of the study. Institution-generated
                # description or classification of the Study (component) performed.
                StructField("description", StringType(), True),
                # Each study has one or more series of images or other content.
                StructField(
                    "series",
                    ArrayType(
                        ImagingStudy_Series.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
