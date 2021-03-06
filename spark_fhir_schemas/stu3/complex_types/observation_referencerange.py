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
class Observation_ReferenceRangeSchema:
    """
    Measurements and simple assertions made about a patient, device or other
    subject.
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
        Measurements and simple assertions made about a patient, device or other
        subject.


        low: The value of the low bound of the reference range.  The low bound of the
            reference range endpoint is inclusive of the value (e.g.  reference range is
            >=5 - <=9).   If the low bound is omitted,  it is assumed to be meaningless
            (e.g. reference range is <=2.3).

        high: The value of the high bound of the reference range.  The high bound of the
            reference range endpoint is inclusive of the value (e.g.  reference range is
            >=5 - <=9).   If the high bound is omitted,  it is assumed to be meaningless
            (e.g. reference range is >= 2.3).

        type: Codes to indicate the what part of the targeted reference population it
            applies to. For example, the normal or therapeutic range.

        appliesTo: Codes to indicate the target population this reference range applies to.  For
            example, a reference range may be based on the normal population or a
            particular sex or race.

        age: The age at which this reference range is applicable. This is a neonatal age
            (e.g. number of weeks at term) if the meaning says so.

        text: Text based reference range in an observation which may be used when a
            quantitative range is not appropriate for an observation.  An example would be
            a reference value of "Negative" or a list or table of 'normals'.

        """
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        if (
            max_recursion_limit
            and nesting_list.count("Observation_ReferenceRange") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "Observation_ReferenceRange"
        ]
        schema = StructType(
            [
                # The value of the low bound of the reference range.  The low bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9).   If the low bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is <=2.3).
                StructField(
                    "low",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The value of the high bound of the reference range.  The high bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9).   If the high bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is >= 2.3).
                StructField(
                    "high",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Codes to indicate the what part of the targeted reference population it
                # applies to. For example, the normal or therapeutic range.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Codes to indicate the target population this reference range applies to.  For
                # example, a reference range may be based on the normal population or a
                # particular sex or race.
                StructField(
                    "appliesTo",
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
                # The age at which this reference range is applicable. This is a neonatal age
                # (e.g. number of weeks at term) if the meaning says so.
                StructField(
                    "age",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Text based reference range in an observation which may be used when a
                # quantitative range is not appropriate for an observation.  An example would be
                # a reference value of "Negative" or a list or table of 'normals'.
                StructField("text", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
