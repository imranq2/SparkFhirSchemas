from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet_Parameter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).


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

        name: Name of the input parameter to the $expand operation; may be a server-assigned
            name for additional default or other server-supplied parameters used to
            control the expansion process.

        valueString: The value of the parameter.

        valueBoolean: The value of the parameter.

        valueInteger: The value of the parameter.

        valueDecimal: The value of the parameter.

        valueUri: The value of the parameter.

        valueCode: The value of the parameter.

        valueDateTime: The value of the parameter.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
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
                # Name of the input parameter to the $expand operation; may be a server-assigned
                # name for additional default or other server-supplied parameters used to
                # control the expansion process.
                StructField("name", StringType(), True),
                # The value of the parameter.
                StructField("valueString", StringType(), True),
                # The value of the parameter.
                StructField("valueBoolean", BooleanType(), True),
                # The value of the parameter.
                StructField("valueInteger", IntegerType(), True),
                # The value of the parameter.
                StructField("valueDecimal", IntegerType(), True),
                # The value of the parameter.
                StructField("valueUri", StringType(), True),
                # The value of the parameter.
                StructField("valueCode", StringType(), True),
                # The value of the parameter.
                StructField("valueDateTime", StringType(), True),
            ]
        )
        return schema
