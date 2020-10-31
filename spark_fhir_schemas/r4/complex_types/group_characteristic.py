from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Group_Characteristic:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Represents a defined collection of entities that may be discussed or acted
        upon collectively but which are not expected to act collectively, and are not
        formally or legally recognized; i.e. a collection of entities that isn't an
        Organization.


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

        code: A code that identifies the kind of trait being asserted.

        valueCodeableConcept: The value of the trait that holds (or does not hold - see 'exclude') for
            members of the group.

        valueBoolean: The value of the trait that holds (or does not hold - see 'exclude') for
            members of the group.

        valueQuantity: The value of the trait that holds (or does not hold - see 'exclude') for
            members of the group.

        valueRange: The value of the trait that holds (or does not hold - see 'exclude') for
            members of the group.

        valueReference: The value of the trait that holds (or does not hold - see 'exclude') for
            members of the group.

        exclude: If true, indicates the characteristic is one that is NOT held by members of
            the group.

        period: The period over which the characteristic is tested; e.g. the patient had an
            operation during the month of June.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
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
                # A code that identifies the kind of trait being asserted.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the trait that holds (or does not hold - see 'exclude') for
                # members of the group.
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The value of the trait that holds (or does not hold - see 'exclude') for
                # members of the group.
                StructField("valueBoolean", BooleanType(), True),
                # The value of the trait that holds (or does not hold - see 'exclude') for
                # members of the group.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the trait that holds (or does not hold - see 'exclude') for
                # members of the group.
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # The value of the trait that holds (or does not hold - see 'exclude') for
                # members of the group.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # If true, indicates the characteristic is one that is NOT held by members of
                # the group.
                StructField("exclude", BooleanType(), True),
                # The period over which the characteristic is tested; e.g. the patient had an
                # operation during the month of June.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
