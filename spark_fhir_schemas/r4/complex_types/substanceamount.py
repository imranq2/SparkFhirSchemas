from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceAmount:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Chemical substances are a single substance type whose primary defining element
        is the molecular structure. Chemical substances shall be defined on the basis
        of their complete covalent molecular structure; the presence of a salt
        (counter-ion) and/or solvates (water, alcohols) is also captured. Purity,
        grade, physical form or particle size are not taken into account in the
        definition of a chemical substance or in the assignment of a Substance ID.


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

        amountQuantity: Used to capture quantitative values for a variety of elements. If only limits
            are given, the arithmetic mean would be the average. If only a single definite
            value for a given element is given, it would be captured in this field.

        amountRange: Used to capture quantitative values for a variety of elements. If only limits
            are given, the arithmetic mean would be the average. If only a single definite
            value for a given element is given, it would be captured in this field.

        amountString: Used to capture quantitative values for a variety of elements. If only limits
            are given, the arithmetic mean would be the average. If only a single definite
            value for a given element is given, it would be captured in this field.

        amountType: Most elements that require a quantitative value will also have a field called
            amount type. Amount type should always be specified because the actual value
            of the amount is often dependent on it. EXAMPLE: In capturing the actual
            relative amounts of substances or molecular fragments it is essential to
            indicate whether the amount refers to a mole ratio or weight ratio. For any
            given element an effort should be made to use same the amount type for all
            related definitional elements.

        amountText: A textual comment on a numeric value.

        referenceRange: Reference range of possible or expected values.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substanceamount_referencerange import SubstanceAmount_ReferenceRange
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
                # Used to capture quantitative values for a variety of elements. If only limits
                # are given, the arithmetic mean would be the average. If only a single definite
                # value for a given element is given, it would be captured in this field.
                StructField(
                    "amountQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Used to capture quantitative values for a variety of elements. If only limits
                # are given, the arithmetic mean would be the average. If only a single definite
                # value for a given element is given, it would be captured in this field.
                StructField(
                    "amountRange", Range.get_schema(recursion_depth + 1), True
                ),
                # Used to capture quantitative values for a variety of elements. If only limits
                # are given, the arithmetic mean would be the average. If only a single definite
                # value for a given element is given, it would be captured in this field.
                StructField("amountString", StringType(), True),
                # Most elements that require a quantitative value will also have a field called
                # amount type. Amount type should always be specified because the actual value
                # of the amount is often dependent on it. EXAMPLE: In capturing the actual
                # relative amounts of substances or molecular fragments it is essential to
                # indicate whether the amount refers to a mole ratio or weight ratio. For any
                # given element an effort should be made to use same the amount type for all
                # related definitional elements.
                StructField(
                    "amountType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A textual comment on a numeric value.
                StructField("amountText", StringType(), True),
                # Reference range of possible or expected values.
                StructField(
                    "referenceRange",
                    SubstanceAmount_ReferenceRange.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
