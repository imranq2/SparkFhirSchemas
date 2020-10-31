from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImagingStudy_Series:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Representation of the content produced in a DICOM imaging study. A study
        comprises a set of series, each of which includes a set of Service-Object Pair
        Instances (SOP Instances - images or other data) acquired or produced in a
        common context.  A series is of only one modality (e.g. X-ray, CT, MR,
        ultrasound), but a study may have multiple series of different modalities.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        uid: The DICOM Series Instance UID for the series.

        number: The numeric identifier of this series in the study.

        modality: The modality of this series sequence.

        description: A description of the series.

        numberOfInstances: Number of SOP Instances in the Study. The value given may be larger than the
            number of instance elements this resource contains due to resource
            availability, security, or other factors. This element should be present if
            any instance elements are present.

        endpoint: The network service providing access (e.g., query, view, or retrieval) for
            this series. See implementation notes for information about using DICOM
            endpoints. A series-level endpoint, if present, has precedence over a study-
            level endpoint with the same Endpoint.connectionType.

        bodySite: The anatomic structures examined. See DICOM Part 16 Annex L (http://dicom.nema
            .org/medical/dicom/current/output/chtml/part16/chapter_L.html) for DICOM to
            SNOMED-CT mappings. The bodySite may indicate the laterality of body part
            imaged; if so, it shall be consistent with any content of
            ImagingStudy.series.laterality.

        laterality: The laterality of the (possibly paired) anatomic structures examined. E.g.,
            the left knee, both lungs, or unpaired abdomen. If present, shall be
            consistent with any laterality information indicated in
            ImagingStudy.series.bodySite.

        specimen: The specimen imaged, e.g., for whole slide imaging of a biopsy.

        started: The date and time the series was started.

        performer: Indicates who or what performed the series and how they were involved.

        instance: A single SOP instance within the series, e.g. an image, or presentation state.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.imagingstudy_performer import ImagingStudy_Performer
        from spark_fhir_schemas.r4.complex_types.imagingstudy_instance import ImagingStudy_Instance
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The DICOM Series Instance UID for the series.
                StructField("uid", id.get_schema(recursion_depth + 1), True),
                # The numeric identifier of this series in the study.
                StructField(
                    "number", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # The modality of this series sequence.
                StructField(
                    "modality", Coding.get_schema(recursion_depth + 1), True
                ),
                # A description of the series.
                StructField("description", StringType(), True),
                # Number of SOP Instances in the Study. The value given may be larger than the
                # number of instance elements this resource contains due to resource
                # availability, security, or other factors. This element should be present if
                # any instance elements are present.
                StructField(
                    "numberOfInstances",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # The network service providing access (e.g., query, view, or retrieval) for
                # this series. See implementation notes for information about using DICOM
                # endpoints. A series-level endpoint, if present, has precedence over a study-
                # level endpoint with the same Endpoint.connectionType.
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The anatomic structures examined. See DICOM Part 16 Annex L (http://dicom.nema
                # .org/medical/dicom/current/output/chtml/part16/chapter_L.html) for DICOM to
                # SNOMED-CT mappings. The bodySite may indicate the laterality of body part
                # imaged; if so, it shall be consistent with any content of
                # ImagingStudy.series.laterality.
                StructField(
                    "bodySite", Coding.get_schema(recursion_depth + 1), True
                ),
                # The laterality of the (possibly paired) anatomic structures examined. E.g.,
                # the left knee, both lungs, or unpaired abdomen. If present, shall be
                # consistent with any laterality information indicated in
                # ImagingStudy.series.bodySite.
                StructField(
                    "laterality", Coding.get_schema(recursion_depth + 1), True
                ),
                # The specimen imaged, e.g., for whole slide imaging of a biopsy.
                StructField(
                    "specimen",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The date and time the series was started.
                StructField(
                    "started", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Indicates who or what performed the series and how they were involved.
                StructField(
                    "performer",
                    ArrayType(
                        ImagingStudy_Performer.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A single SOP instance within the series, e.g. an image, or presentation state.
                StructField(
                    "instance",
                    ArrayType(
                        ImagingStudy_Instance.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
