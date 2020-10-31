from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PaymentReconciliation_Detail:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource provides the details including amount of a payment and allocates
        the payment items being paid.


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

        identifier: Unique identifier for the current payment item for the referenced payable.

        predecessor: Unique identifier for the prior payment item for the referenced payable.

        type: Code to indicate the nature of the payment.

        request: A resource, such as a Claim, the evaluation of which could lead to payment.

        submitter: The party which submitted the claim or financial transaction.

        response: A resource, such as a ClaimResponse, which contains a commitment to payment.

        date: The date from the response resource containing a commitment to pay.

        responsible: A reference to the individual who is responsible for inquiries regarding the
            response and its payment.

        payee: The party which is receiving the payment.

        amount: The monetary amount allocated from the total payment to the payable.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.money import Money
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Unique identifier for the current payment item for the referenced payable.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # Unique identifier for the prior payment item for the referenced payable.
                StructField(
                    "predecessor", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # Code to indicate the nature of the payment.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A resource, such as a Claim, the evaluation of which could lead to payment.
                StructField(
                    "request", Reference.get_schema(recursion_depth + 1), True
                ),
                # The party which submitted the claim or financial transaction.
                StructField(
                    "submitter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # A resource, such as a ClaimResponse, which contains a commitment to payment.
                StructField(
                    "response", Reference.get_schema(recursion_depth + 1), True
                ),
                # The date from the response resource containing a commitment to pay.
                StructField("date", DateType(), True),
                # A reference to the individual who is responsible for inquiries regarding the
                # response and its payment.
                StructField(
                    "responsible", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The party which is receiving the payment.
                StructField(
                    "payee", Reference.get_schema(recursion_depth + 1), True
                ),
                # The monetary amount allocated from the total payment to the payable.
                StructField(
                    "amount", Money.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
