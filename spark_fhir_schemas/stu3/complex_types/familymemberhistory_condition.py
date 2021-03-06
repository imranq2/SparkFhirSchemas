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
class FamilyMemberHistory_ConditionSchema:
    """
    Significant health events and conditions for a person related to the patient
    relevant in the context of care for the patient.
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
        Significant health events and conditions for a person related to the patient
        relevant in the context of care for the patient.


        code: The actual condition specified. Could be a coded condition (like MI or
            Diabetes) or a less specific string like 'cancer' depending on how much is
            known about the condition and the capabilities of the creating system.

        outcome: Indicates what happened as a result of this condition.  If the condition
            resulted in death, deceased date is captured on the relation.

        onsetAge: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        onsetRange: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        onsetPeriod: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        onsetString: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        note: An area where general notes can be placed about this specific condition.

        """
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.age import AgeSchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema
        if (
            max_recursion_limit
            and nesting_list.count("FamilyMemberHistory_Condition") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "FamilyMemberHistory_Condition"
        ]
        schema = StructType(
            [
                # The actual condition specified. Could be a coded condition (like MI or
                # Diabetes) or a less specific string like 'cancer' depending on how much is
                # known about the condition and the capabilities of the creating system.
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
                # Indicates what happened as a result of this condition.  If the condition
                # resulted in death, deceased date is captured on the relation.
                StructField(
                    "outcome",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField(
                    "onsetAge",
                    AgeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField(
                    "onsetRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField(
                    "onsetPeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField("onsetString", StringType(), True),
                # An area where general notes can be placed about this specific condition.
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
