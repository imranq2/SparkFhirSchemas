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
class ClaimResponse_SubDetail1Schema:
    """
    This resource provides the adjudication details from the processing of a Claim
    resource.
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
        This resource provides the adjudication details from the processing of a Claim
        resource.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        productOrService: When the value is a group code then this item collects a set of related claim
            details, otherwise this contains the product, service, drug or other billing
            code for the item.

        modifier: Item typification or modifiers codes to convey additional context for the
            product or service.

        quantity: The number of repetitions of a service or product.

        unitPrice: If the item is not a group then this is the fee for the product or service,
            otherwise this is the total of the fees for the details of the group.

        factor: A real number that represents a multiplier used in determining the overall
            value of services delivered and/or goods received. The concept of a Factor
            allows for a discount or surcharge multiplier to be applied to a monetary
            amount.

        net: The quantity times the unit price for an additional service or product or
            charge.

        noteNumber: The numbers associated with notes below which apply to the adjudication of
            this item.

        adjudication: The adjudication results.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.money import MoneySchema
        from spark_fhir_schemas.r4.simple_types.decimal import decimalSchema
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveIntSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_AdjudicationSchema
        if (
            max_recursion_limit
            and nesting_list.count("ClaimResponse_SubDetail1") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ClaimResponse_SubDetail1"
        ]
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
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # When the value is a group code then this item collects a set of related claim
                # details, otherwise this contains the product, service, drug or other billing
                # code for the item.
                StructField(
                    "productOrService",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Item typification or modifiers codes to convey additional context for the
                # product or service.
                StructField(
                    "modifier",
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
                # The number of repetitions of a service or product.
                StructField(
                    "quantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # If the item is not a group then this is the fee for the product or service,
                # otherwise this is the total of the fees for the details of the group.
                StructField(
                    "unitPrice",
                    MoneySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A real number that represents a multiplier used in determining the overall
                # value of services delivered and/or goods received. The concept of a Factor
                # allows for a discount or surcharge multiplier to be applied to a monetary
                # amount.
                StructField(
                    "factor",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The quantity times the unit price for an additional service or product or
                # charge.
                StructField(
                    "net",
                    MoneySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The numbers associated with notes below which apply to the adjudication of
                # this item.
                StructField(
                    "noteNumber",
                    ArrayType(
                        positiveIntSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The adjudication results.
                StructField(
                    "adjudication",
                    ArrayType(
                        ClaimResponse_AdjudicationSchema.get_schema(
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
