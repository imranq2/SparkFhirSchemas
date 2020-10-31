from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ObservationDefinition_QualifiedInterval:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Set of definitional characteristics for a kind of observation or measurement
        produced or consumed by an orderable health care service.


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

        category: The category of interval of values for continuous or ordinal observations
            conforming to this ObservationDefinition.

        range: The low and high values determining the interval. There may be only one of the
            two.

        context: Codes to indicate the health context the range applies to. For example, the
            normal or therapeutic range.

        appliesTo: Codes to indicate the target population this reference range applies to.

        gender: Sex of the population the range applies to.

        age: The age at which this reference range is applicable. This is a neonatal age
            (e.g. number of weeks at term) if the meaning says so.

        gestationalAge: The gestational age to which this reference range is applicable, in the
            context of pregnancy.

        condition: Text based condition for which the reference range is valid.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                # The category of interval of values for continuous or ordinal observations
                # conforming to this ObservationDefinition.
                StructField("category", StringType(), True),
                # The low and high values determining the interval. There may be only one of the
                # two.
                StructField(
                    "range", Range.get_schema(recursion_depth + 1), True
                ),
                # Codes to indicate the health context the range applies to. For example, the
                # normal or therapeutic range.
                StructField(
                    "context", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Codes to indicate the target population this reference range applies to.
                StructField(
                    "appliesTo",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Sex of the population the range applies to.
                StructField("gender", StringType(), True),
                # The age at which this reference range is applicable. This is a neonatal age
                # (e.g. number of weeks at term) if the meaning says so.
                StructField(
                    "age", Range.get_schema(recursion_depth + 1), True
                ),
                # The gestational age to which this reference range is applicable, in the
                # context of pregnancy.
                StructField(
                    "gestationalAge", Range.get_schema(recursion_depth + 1),
                    True
                ),
                # Text based condition for which the reference range is valid.
                StructField("condition", StringType(), True),
            ]
        )
        return schema
