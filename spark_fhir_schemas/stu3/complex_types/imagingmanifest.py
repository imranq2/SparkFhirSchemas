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
class ImagingManifestSchema:
    """
    A text description of the DICOM SOP instances selected in the ImagingManifest;
    or the reason for, or significance of, the selection.
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
        A text description of the DICOM SOP instances selected in the ImagingManifest;
        or the reason for, or significance of, the selection.


        resourceType: This is a ImagingManifest resource

        identifier: Unique identifier of the DICOM Key Object Selection (KOS) that this resource
            represents.

        patient: A patient resource reference which is the patient subject of all DICOM SOP
            Instances in this ImagingManifest.

        authoringTime: Date and time when the selection of the referenced instances were made. It is
            (typically) different from the creation date of the selection resource, and
            from dates associated with the referenced instances (e.g. capture time of the
            referenced image).

        author: Author of ImagingManifest. It can be a human author or a device which made the
            decision of the SOP instances selected. For example, a radiologist selected a
            set of imaging SOP instances to attach in a diagnostic report, and a CAD
            application may author a selection to describe SOP instances it used to
            generate a detection conclusion.

        description: Free text narrative description of the ImagingManifest.
            The value may be derived from the DICOM Standard Part 16, CID-7010
            descriptions (e.g. Best in Set, Complete Study Content). Note that those
            values cover the wide range of uses of the DICOM Key Object Selection object,
            several of which are not supported by ImagingManifest. Specifically, there is
            no expected behavior associated with descriptions that suggest referenced
            images be removed or not used.

        study: Study identity and locating information of the DICOM SOP instances in the
            selection.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.imagingmanifest_study import ImagingManifest_StudySchema
        if (
            max_recursion_limit
            and nesting_list.count("ImagingManifest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImagingManifest"]
        schema = StructType(
            [
                # This is a ImagingManifest resource
                StructField("resourceType", StringType(), True),
                # Unique identifier of the DICOM Key Object Selection (KOS) that this resource
                # represents.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A patient resource reference which is the patient subject of all DICOM SOP
                # Instances in this ImagingManifest.
                StructField(
                    "patient",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Date and time when the selection of the referenced instances were made. It is
                # (typically) different from the creation date of the selection resource, and
                # from dates associated with the referenced instances (e.g. capture time of the
                # referenced image).
                StructField("authoringTime", StringType(), True),
                # Author of ImagingManifest. It can be a human author or a device which made the
                # decision of the SOP instances selected. For example, a radiologist selected a
                # set of imaging SOP instances to attach in a diagnostic report, and a CAD
                # application may author a selection to describe SOP instances it used to
                # generate a detection conclusion.
                StructField(
                    "author",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Free text narrative description of the ImagingManifest.
                # The value may be derived from the DICOM Standard Part 16, CID-7010
                # descriptions (e.g. Best in Set, Complete Study Content). Note that those
                # values cover the wide range of uses of the DICOM Key Object Selection object,
                # several of which are not supported by ImagingManifest. Specifically, there is
                # no expected behavior associated with descriptions that suggest referenced
                # images be removed or not used.
                StructField("description", StringType(), True),
                # Study identity and locating information of the DICOM SOP instances in the
                # selection.
                StructField(
                    "study",
                    ArrayType(
                        ImagingManifest_StudySchema.get_schema(
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
