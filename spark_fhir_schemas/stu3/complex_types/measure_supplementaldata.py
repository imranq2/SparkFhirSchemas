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
class Measure_SupplementalDataSchema:
    """
    The Measure resource provides the definition of a quality measure.
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
        The Measure resource provides the definition of a quality measure.


        identifier: An identifier for the supplemental data.

        usage: An indicator of the intended usage for the supplemental data element.
            Supplemental data indicates the data is additional information requested to
            augment the measure information. Risk adjustment factor indicates the data is
            additional information used to calculate risk adjustment factors when applying
            a risk model to the measure calculation.

        criteria: The criteria for the supplemental data. This must be the name of a valid
            expression defined within a referenced library, and defines the data to be
            returned for this element.

        path: The supplemental data to be supplied as part of the measure response,
            specified as a valid FHIR Resource Path.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit
            and nesting_list.count("Measure_SupplementalData") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "Measure_SupplementalData"
        ]
        schema = StructType(
            [
                # An identifier for the supplemental data.
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
                # An indicator of the intended usage for the supplemental data element.
                # Supplemental data indicates the data is additional information requested to
                # augment the measure information. Risk adjustment factor indicates the data is
                # additional information used to calculate risk adjustment factors when applying
                # a risk model to the measure calculation.
                StructField(
                    "usage",
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
                # The criteria for the supplemental data. This must be the name of a valid
                # expression defined within a referenced library, and defines the data to be
                # returned for this element.
                StructField("criteria", StringType(), True),
                # The supplemental data to be supplied as part of the measure response,
                # specified as a valid FHIR Resource Path.
                StructField("path", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
