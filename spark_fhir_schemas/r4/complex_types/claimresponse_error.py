from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ClaimResponse_ErrorSchema:
    """
    This resource provides the adjudication details from the processing of a Claim
    resource.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        itemSequence: The sequence number of the line item submitted which contains the error. This
            value is omitted when the error occurs outside of the item structure.

        detailSequence: The sequence number of the detail within the line item submitted which
            contains the error. This value is omitted when the error occurs outside of the
            item structure.

        subDetailSequence: The sequence number of the sub-detail within the detail within the line item
            submitted which contains the error. This value is omitted when the error
            occurs outside of the item structure.

        code: An error code, from a specified code system, which details why the claim could
            not be adjudicated.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveIntSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        if recursion_depth > 3:
            return StructType([])
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
                # The sequence number of the line item submitted which contains the error. This
                # value is omitted when the error occurs outside of the item structure.
                StructField(
                    "itemSequence",
                    positiveIntSchema.get_schema(recursion_depth + 1), True
                ),
                # The sequence number of the detail within the line item submitted which
                # contains the error. This value is omitted when the error occurs outside of the
                # item structure.
                StructField(
                    "detailSequence",
                    positiveIntSchema.get_schema(recursion_depth + 1), True
                ),
                # The sequence number of the sub-detail within the detail within the line item
                # submitted which contains the error. This value is omitted when the error
                # occurs outside of the item structure.
                StructField(
                    "subDetailSequence",
                    positiveIntSchema.get_schema(recursion_depth + 1), True
                ),
                # An error code, from a specified code system, which details why the claim could
                # not be adjudicated.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
