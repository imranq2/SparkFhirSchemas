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
class Observation_ComponentSchema:
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


        code: Describes what was observed. Sometimes this is called the observation "code".

        valueQuantity: The information determined as a result of making the observation, if the
            information has a simple value.

        valueCodeableConcept: The information determined as a result of making the observation, if the
            information has a simple value.

        valueString: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRange: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRatio: The information determined as a result of making the observation, if the
            information has a simple value.

        valueSampledData: The information determined as a result of making the observation, if the
            information has a simple value.

        valueAttachment: The information determined as a result of making the observation, if the
            information has a simple value.

        valueTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valueDateTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valuePeriod: The information determined as a result of making the observation, if the
            information has a simple value.

        dataAbsentReason: Provides a reason why the expected value in the element Observation.value[x]
            is missing.

        interpretation: The assessment made based on the result of the observation.  Intended as a
            simple compact code often placed adjacent to the result value in reports and
            flow sheets to signal the meaning/normalcy status of the result. Otherwise
            known as abnormal flag.

        referenceRange: Guidance on how to interpret the value by comparison to a normal or
            recommended range.

        """
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        from spark_fhir_schemas.stu3.complex_types.ratio import RatioSchema
        from spark_fhir_schemas.stu3.complex_types.sampleddata import SampledDataSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.observation_referencerange import Observation_ReferenceRangeSchema
        if (
            max_recursion_limit and
            nesting_list.count("Observation_Component") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Observation_Component"]
        schema = StructType(
            [
                # Describes what was observed. Sometimes this is called the observation "code".
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
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueString", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRatio",
                    RatioSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueSampledData",
                    SampledDataSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueDateTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valuePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Provides a reason why the expected value in the element Observation.value[x]
                # is missing.
                StructField(
                    "dataAbsentReason",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The assessment made based on the result of the observation.  Intended as a
                # simple compact code often placed adjacent to the result value in reports and
                # flow sheets to signal the meaning/normalcy status of the result. Otherwise
                # known as abnormal flag.
                StructField(
                    "interpretation",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Guidance on how to interpret the value by comparison to a normal or
                # recommended range.
                StructField(
                    "referenceRange",
                    ArrayType(
                        Observation_ReferenceRangeSchema.get_schema(
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
