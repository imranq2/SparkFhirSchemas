from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class SubstanceSpecification_RelationshipSchema:
    """
    The detailed description of a substance, typically at a level beyond what is
    used for prescribing.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The detailed description of a substance, typically at a level beyond what is
        used for prescribing.


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

        substanceReference: A pointer to another substance, as a resource or just a representational code.

        substanceCodeableConcept: A pointer to another substance, as a resource or just a representational code.

        relationship: For example "salt to parent", "active moiety", "starting material".

        isDefining: For example where an enzyme strongly bonds with a particular substance, this
            is a defining relationship for that enzyme, out of several possible substance
            relationships.

        amountQuantity: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountRange: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountRatio: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountString: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountRatioLowLimit: For use when the numeric.

        amountType: An operator for the amount, for example "average", "approximately", "less
            than".

        source: Supporting literature.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.ratio import RatioSchema
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
                # A pointer to another substance, as a resource or just a representational code.
                StructField(
                    "substanceReference",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # A pointer to another substance, as a resource or just a representational code.
                StructField(
                    "substanceCodeableConcept",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # For example "salt to parent", "active moiety", "starting material".
                StructField(
                    "relationship",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # For example where an enzyme strongly bonds with a particular substance, this
                # is a defining relationship for that enzyme, out of several possible substance
                # relationships.
                StructField("isDefining", BooleanType(), True),
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
                StructField(
                    "amountQuantity",
                    QuantitySchema.get_schema(recursion_depth + 1), True
                ),
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
                StructField(
                    "amountRange", RangeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
                StructField(
                    "amountRatio", RatioSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
                StructField("amountString", StringType(), True),
                # For use when the numeric.
                StructField(
                    "amountRatioLowLimit",
                    RatioSchema.get_schema(recursion_depth + 1), True
                ),
                # An operator for the amount, for example "average", "approximately", "less
                # than".
                StructField(
                    "amountType",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Supporting literature.
                StructField(
                    "source",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
