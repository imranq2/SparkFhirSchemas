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
class DetectedIssueSchema:
    """
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
    Ineffective treatment frequency, Procedure-condition conflict, etc.
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
        Indicates an actual or potential clinical issue with or between one or more
        active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
        Ineffective treatment frequency, Procedure-condition conflict, etc.


        resourceType: This is a DetectedIssue resource

        identifier: Business identifier associated with the detected issue record.

        status: Indicates the status of the detected issue.

        category: Identifies the general type of issue identified.

        severity: Indicates the degree of importance associated with the identified issue based
            on the potential impact on the patient.

        patient: Indicates the patient whose record the detected issue is associated with.

        date: The date or date-time when the detected issue was initially identified.

        author: Individual or device responsible for the issue being raised.  For example, a
            decision support application or a pharmacist conducting a medication review.

        implicated: Indicates the resource representing the current activity or proposed activity
            that is potentially problematic.

        detail: A textual explanation of the detected issue.

        reference: The literature, knowledge-base or similar reference that describes the
            propensity for the detected issue identified.

        mitigation: Indicates an action that has been taken or is committed to to reduce or
            eliminate the likelihood of the risk identified by the detected issue from
            manifesting.  Can also reflect an observation of known mitigating factors that
            may reduce/eliminate the need for any action.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.detectedissue_mitigation import DetectedIssue_MitigationSchema
        if (
            max_recursion_limit
            and nesting_list.count("DetectedIssue") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DetectedIssue"]
        schema = StructType(
            [
                # This is a DetectedIssue resource
                StructField("resourceType", StringType(), True),
                # Business identifier associated with the detected issue record.
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
                # Indicates the status of the detected issue.
                StructField("status", StringType(), True),
                # Identifies the general type of issue identified.
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
                # Indicates the degree of importance associated with the identified issue based
                # on the potential impact on the patient.
                StructField("severity", StringType(), True),
                # Indicates the patient whose record the detected issue is associated with.
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
                # The date or date-time when the detected issue was initially identified.
                StructField("date", StringType(), True),
                # Individual or device responsible for the issue being raised.  For example, a
                # decision support application or a pharmacist conducting a medication review.
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
                # Indicates the resource representing the current activity or proposed activity
                # that is potentially problematic.
                StructField(
                    "implicated",
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
                # A textual explanation of the detected issue.
                StructField("detail", StringType(), True),
                # The literature, knowledge-base or similar reference that describes the
                # propensity for the detected issue identified.
                StructField("reference", StringType(), True),
                # Indicates an action that has been taken or is committed to to reduce or
                # eliminate the likelihood of the risk identified by the detected issue from
                # manifesting.  Can also reflect an observation of known mitigating factors that
                # may reduce/eliminate the need for any action.
                StructField(
                    "mitigation",
                    ArrayType(
                        DetectedIssue_MitigationSchema.get_schema(
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
