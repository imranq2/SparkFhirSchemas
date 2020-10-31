from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class HumanName:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A human's name with the ability to identify parts and usage.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        use: Identifies the purpose for this name.

        text: Specifies the entire name as it should be displayed e.g. on an application UI.
            This may be provided instead of or as well as the specific parts.

        family: The part of a name that links to the genealogy. In some cultures (e.g.
            Eritrea) the family name of a son is the first name of his father.

        given: Given name.

        prefix: Part of the name that is acquired as a title due to academic, legal,
            employment or nobility status, etc. and that appears at the start of the name.

        suffix: Part of the name that is acquired as a title due to academic, legal,
            employment or nobility status, etc. and that appears at the end of the name.

        period: Indicates the period of time when this name was valid for the named person.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
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
                # Identifies the purpose for this name.
                StructField("use", StringType(), True),
                # Specifies the entire name as it should be displayed e.g. on an application UI.
                # This may be provided instead of or as well as the specific parts.
                StructField("text", StringType(), True),
                # The part of a name that links to the genealogy. In some cultures (e.g.
                # Eritrea) the family name of a son is the first name of his father.
                StructField("family", StringType(), True),
                # Given name.
                StructField("given", ArrayType(StringType()), True),
                # Part of the name that is acquired as a title due to academic, legal,
                # employment or nobility status, etc. and that appears at the start of the name.
                StructField("prefix", ArrayType(StringType()), True),
                # Part of the name that is acquired as a title due to academic, legal,
                # employment or nobility status, etc. and that appears at the end of the name.
                StructField("suffix", ArrayType(StringType()), True),
                # Indicates the period of time when this name was valid for the named person.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
