from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NarrativeSchema:
    """
    A human-readable summary of the resource conveying the essential clinical and
    business information for the resource.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A human-readable summary of the resource conveying the essential clinical and
        business information for the resource.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        status: The status of the narrative - whether it's entirely generated (from just the
            defined data or the extensions too), or whether a human authored it and it may
            contain additional data.

        div: The actual narrative content, a stripped down version of XHTML.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.xhtml import xhtmlSchema
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
                # The status of the narrative - whether it's entirely generated (from just the
                # defined data or the extensions too), or whether a human authored it and it may
                # contain additional data.
                StructField("status", StringType(), True),
                # The actual narrative content, a stripped down version of XHTML.
                StructField(
                    "div", xhtmlSchema.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
