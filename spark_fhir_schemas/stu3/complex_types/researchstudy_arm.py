from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ResearchStudy_ArmSchema:
    """
    A process where a researcher or organization plans and then executes a series
    of steps intended to increase the field of healthcare-related knowledge.  This
    includes studies of safety, efficacy, comparative effectiveness and other
    information about medications, devices, therapies and other interventional and
    investigative techniques.  A ResearchStudy involves the gathering of
    information about human or animal subjects.
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
        A process where a researcher or organization plans and then executes a series
        of steps intended to increase the field of healthcare-related knowledge.  This
        includes studies of safety, efficacy, comparative effectiveness and other
        information about medications, devices, therapies and other interventional and
        investigative techniques.  A ResearchStudy involves the gathering of
        information about human or animal subjects.


        name: Unique, human-readable label for this arm of the study.

        code: Categorization of study arm, e.g. experimental, active comparator, placebo
            comparater.

        description: A succinct description of the path through the study that would be followed by
            a subject adhering to this arm.

        """
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit
            and nesting_list.count("ResearchStudy_Arm") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ResearchStudy_Arm"]
        schema = StructType(
            [
                # Unique, human-readable label for this arm of the study.
                StructField("name", StringType(), True),
                # Categorization of study arm, e.g. experimental, active comparator, placebo
                # comparater.
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
                # A succinct description of the path through the study that would be followed by
                # a subject adhering to this arm.
                StructField("description", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
