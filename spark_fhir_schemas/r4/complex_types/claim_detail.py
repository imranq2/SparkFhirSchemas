from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Claim_DetailSchema:
    """
    A provider issued list of professional services and products which have been
    provided, or are to be provided, to a patient which is sent to an insurer for
    reimbursement.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A provider issued list of professional services and products which have been
        provided, or are to be provided, to a patient which is sent to an insurer for
        reimbursement.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        sequence: A number to uniquely identify item entries.

        revenue: The type of revenue or cost center providing the product and/or service.

        category: Code to identify the general type of benefits under which products and
            services are provided.

        productOrService: When the value is a group code then this item collects a set of related claim
            details, otherwise this contains the product, service, drug or other billing
            code for the item.

        modifier: Item typification or modifiers codes to convey additional context for the
            product or service.

        programCode: Identifies the program under which this may be recovered.

        quantity: The number of repetitions of a service or product.

        unitPrice: If the item is not a group then this is the fee for the product or service,
            otherwise this is the total of the fees for the details of the group.

        factor: A real number that represents a multiplier used in determining the overall
            value of services delivered and/or goods received. The concept of a Factor
            allows for a discount or surcharge multiplier to be applied to a monetary
            amount.

        net: The quantity times the unit price for an additional service or product or
            charge.

        udi: Unique Device Identifiers associated with this line item.

        subDetail: A claim detail line. Either a simple (a product or service) or a 'group' of
            sub-details which are simple items.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveIntSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.money import MoneySchema
        from spark_fhir_schemas.r4.simple_types.decimal import decimalSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.claim_subdetail import Claim_SubDetailSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # A number to uniquely identify item entries.
                StructField(
                    "sequence",
                    positiveIntSchema.get_schema(recursion_depth + 1), True
                ),
                # The type of revenue or cost center providing the product and/or service.
                StructField(
                    "revenue",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Code to identify the general type of benefits under which products and
                # services are provided.
                StructField(
                    "category",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # When the value is a group code then this item collects a set of related claim
                # details, otherwise this contains the product, service, drug or other billing
                # code for the item.
                StructField(
                    "productOrService",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Item typification or modifiers codes to convey additional context for the
                # product or service.
                StructField(
                    "modifier",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies the program under which this may be recovered.
                StructField(
                    "programCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The number of repetitions of a service or product.
                StructField(
                    "quantity", QuantitySchema.get_schema(recursion_depth + 1),
                    True
                ),
                # If the item is not a group then this is the fee for the product or service,
                # otherwise this is the total of the fees for the details of the group.
                StructField(
                    "unitPrice", MoneySchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A real number that represents a multiplier used in determining the overall
                # value of services delivered and/or goods received. The concept of a Factor
                # allows for a discount or surcharge multiplier to be applied to a monetary
                # amount.
                StructField(
                    "factor", decimalSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The quantity times the unit price for an additional service or product or
                # charge.
                StructField(
                    "net", MoneySchema.get_schema(recursion_depth + 1), True
                ),
                # Unique Device Identifiers associated with this line item.
                StructField(
                    "udi",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # A claim detail line. Either a simple (a product or service) or a 'group' of
                # sub-details which are simple items.
                StructField(
                    "subDetail",
                    ArrayType(
                        Claim_SubDetailSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
