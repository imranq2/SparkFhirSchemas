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
class MarketingStatusSchema:
    """
    The marketing status describes the date when a medicinal product is actually
    put on the market or the date as of which it is no longer available.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
        """
        The marketing status describes the date when a medicinal product is actually
        put on the market or the date as of which it is no longer available.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        country: The country in which the marketing authorisation has been granted shall be
            specified It should be specified using the ISO 3166 ‑ 1 alpha-2 code elements.

        jurisdiction: Where a Medicines Regulatory Agency has granted a marketing authorisation for
            which specific provisions within a jurisdiction apply, the jurisdiction can be
            specified using an appropriate controlled terminology The controlled term and
            the controlled term identifier shall be specified.

        status: This attribute provides information on the status of the marketing of the
            medicinal product See ISO/TS 20443 for more information and examples.

        dateRange: The date when the Medicinal Product is placed on the market by the Marketing
            Authorisation Holder (or where applicable, the manufacturer/distributor) in a
            country and/or jurisdiction shall be provided A complete date consisting of
            day, month and year shall be specified using the ISO 8601 date format NOTE
            “Placed on the market” refers to the release of the Medicinal Product into the
            distribution chain.

        restoreDate: The date when the Medicinal Product is placed on the market by the Marketing
            Authorisation Holder (or where applicable, the manufacturer/distributor) in a
            country and/or jurisdiction shall be provided A complete date consisting of
            day, month and year shall be specified using the ISO 8601 date format NOTE
            “Placed on the market” refers to the release of the Medicinal Product into the
            distribution chain.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        if (
            max_recursion_limit
            and nesting_list.count("MarketingStatus") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MarketingStatus"]
        schema = StructType(
            [
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The country in which the marketing authorisation has been granted shall be
                # specified It should be specified using the ISO 3166 ‑ 1 alpha-2 code elements.
                StructField(
                    "country",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where a Medicines Regulatory Agency has granted a marketing authorisation for
                # which specific provisions within a jurisdiction apply, the jurisdiction can be
                # specified using an appropriate controlled terminology The controlled term and
                # the controlled term identifier shall be specified.
                StructField(
                    "jurisdiction",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # This attribute provides information on the status of the marketing of the
                # medicinal product See ISO/TS 20443 for more information and examples.
                StructField(
                    "status",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The date when the Medicinal Product is placed on the market by the Marketing
                # Authorisation Holder (or where applicable, the manufacturer/distributor) in a
                # country and/or jurisdiction shall be provided A complete date consisting of
                # day, month and year shall be specified using the ISO 8601 date format NOTE
                # “Placed on the market” refers to the release of the Medicinal Product into the
                # distribution chain.
                StructField(
                    "dateRange",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The date when the Medicinal Product is placed on the market by the Marketing
                # Authorisation Holder (or where applicable, the manufacturer/distributor) in a
                # country and/or jurisdiction shall be provided A complete date consisting of
                # day, month and year shall be specified using the ISO 8601 date format NOTE
                # “Placed on the market” refers to the release of the Medicinal Product into the
                # distribution chain.
                StructField(
                    "restoreDate",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
            ]
        )
        return schema
