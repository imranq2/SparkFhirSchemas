from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TestScript_Variable:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.


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

        name: Descriptive name for this variable.

        defaultValue: A default, hard-coded, or user-defined value for this variable.

        description: A free text natural language description of the variable and its purpose.

        expression: The FHIRPath expression to evaluate against the fixture body. When variables
            are defined, only one of either expression, headerField or path must be
            specified.

        headerField: Will be used to grab the HTTP header field value from the headers that
            sourceId is pointing to.

        hint: Displayable text string with hint help information to the user when entering a
            default value.

        path: XPath or JSONPath to evaluate against the fixture body.  When variables are
            defined, only one of either expression, headerField or path must be specified.

        sourceId: Fixture to evaluate the XPath/JSONPath expression or the headerField  against
            within this variable.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
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
                # Descriptive name for this variable.
                StructField("name", StringType(), True),
                # A default, hard-coded, or user-defined value for this variable.
                StructField("defaultValue", StringType(), True),
                # A free text natural language description of the variable and its purpose.
                StructField("description", StringType(), True),
                # The FHIRPath expression to evaluate against the fixture body. When variables
                # are defined, only one of either expression, headerField or path must be
                # specified.
                StructField("expression", StringType(), True),
                # Will be used to grab the HTTP header field value from the headers that
                # sourceId is pointing to.
                StructField("headerField", StringType(), True),
                # Displayable text string with hint help information to the user when entering a
                # default value.
                StructField("hint", StringType(), True),
                # XPath or JSONPath to evaluate against the fixture body.  When variables are
                # defined, only one of either expression, headerField or path must be specified.
                StructField("path", StringType(), True),
                # Fixture to evaluate the XPath/JSONPath expression or the headerField  against
                # within this variable.
                StructField(
                    "sourceId", id.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
