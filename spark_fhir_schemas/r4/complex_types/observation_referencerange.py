from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Observation_ReferenceRange:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Measurements and simple assertions made about a patient, device or other
        subject.


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

        low: The value of the low bound of the reference range.  The low bound of the
            reference range endpoint is inclusive of the value (e.g.  reference range is
            >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless
            (e.g. reference range is <=2.3).

        high: The value of the high bound of the reference range.  The high bound of the
            reference range endpoint is inclusive of the value (e.g.  reference range is
            >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless
            (e.g. reference range is >= 2.3).

        type: Codes to indicate the what part of the targeted reference population it
            applies to. For example, the normal or therapeutic range.

        appliesTo: Codes to indicate the target population this reference range applies to.  For
            example, a reference range may be based on the normal population or a
            particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of
            the target populations.  For example, to represent a target population of
            African American females, both a code of female and a code for African
            American would be used.

        age: The age at which this reference range is applicable. This is a neonatal age
            (e.g. number of weeks at term) if the meaning says so.

        text: Text based reference range in an observation which may be used when a
            quantitative range is not appropriate for an observation.  An example would be
            a reference value of "Negative" or a list or table of "normals".

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.range import Range
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
                # The value of the low bound of the reference range.  The low bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is <=2.3).
                StructField(
                    "low", Quantity.get_schema(recursion_depth + 1), True
                ),
                # The value of the high bound of the reference range.  The high bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is >= 2.3).
                StructField(
                    "high", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Codes to indicate the what part of the targeted reference population it
                # applies to. For example, the normal or therapeutic range.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Codes to indicate the target population this reference range applies to.  For
                # example, a reference range may be based on the normal population or a
                # particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of
                # the target populations.  For example, to represent a target population of
                # African American females, both a code of female and a code for African
                # American would be used.
                StructField(
                    "appliesTo",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The age at which this reference range is applicable. This is a neonatal age
                # (e.g. number of weeks at term) if the meaning says so.
                StructField(
                    "age", Range.get_schema(recursion_depth + 1), True
                ),
                # Text based reference range in an observation which may be used when a
                # quantitative range is not appropriate for an observation.  An example would be
                # a reference value of "Negative" or a list or table of "normals".
                StructField("text", StringType(), True),
            ]
        )
        return schema
