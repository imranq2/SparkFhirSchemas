from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Encounter_DiagnosisSchema:
    """
    An interaction between a patient and healthcare provider(s) for the purpose of
    providing healthcare service(s) or assessing the health status of a patient.
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
        An interaction between a patient and healthcare provider(s) for the purpose of
        providing healthcare service(s) or assessing the health status of a patient.


        condition: Reason the encounter takes place, as specified using information from another
            resource. For admissions, this is the admission diagnosis. The indication will
            typically be a Condition (with other resources referenced in the
            evidence.detail), or a Procedure.

        role: Role that this diagnosis has within the encounter (e.g. admission, billing,
            discharge …).

        rank: Ranking of the diagnosis (for each role type).

        """
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit and
            nesting_list.count("Encounter_Diagnosis") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Encounter_Diagnosis"]
        schema = StructType(
            [
                # Reason the encounter takes place, as specified using information from another
                # resource. For admissions, this is the admission diagnosis. The indication will
                # typically be a Condition (with other resources referenced in the
                # evidence.detail), or a Procedure.
                StructField(
                    "condition",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Role that this diagnosis has within the encounter (e.g. admission, billing,
                # discharge …).
                StructField(
                    "role",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Ranking of the diagnosis (for each role type).
                StructField("rank", IntegerType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
