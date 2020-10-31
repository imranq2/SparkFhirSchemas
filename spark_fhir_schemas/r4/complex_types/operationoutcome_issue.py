from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class OperationOutcome_Issue:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A collection of error, warning, or information messages that result from a
        system action.


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

        severity: Indicates whether the issue indicates a variation from successful processing.

        code: Describes the type of the issue. The system that creates an OperationOutcome
            SHALL choose the most applicable code from the IssueType value set, and may
            additional provide its own code for the error in the details element.

        details: Additional details about the error. This may be a text description of the
            error or a system code that identifies the error.

        diagnostics: Additional diagnostic information about the issue.

        location: This element is deprecated because it is XML specific. It is replaced by
            issue.expression, which is format independent, and simpler to parse.

            For resource issues, this will be a simple XPath limited to element names,
            repetition indicators and the default child accessor that identifies one of
            the elements in the resource that caused this issue to be raised.  For HTTP
            errors, will be "http." + the parameter name.

        expression: A [simple subset of FHIRPath](fhirpath.html#simple) limited to element names,
            repetition indicators and the default child accessor that identifies one of
            the elements in the resource that caused this issue to be raised.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
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
                # Indicates whether the issue indicates a variation from successful processing.
                StructField("severity", StringType(), True),
                # Describes the type of the issue. The system that creates an OperationOutcome
                # SHALL choose the most applicable code from the IssueType value set, and may
                # additional provide its own code for the error in the details element.
                StructField("code", StringType(), True),
                # Additional details about the error. This may be a text description of the
                # error or a system code that identifies the error.
                StructField(
                    "details", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Additional diagnostic information about the issue.
                StructField("diagnostics", StringType(), True),
                # This element is deprecated because it is XML specific. It is replaced by
                # issue.expression, which is format independent, and simpler to parse.
                #
                # For resource issues, this will be a simple XPath limited to element names,
                # repetition indicators and the default child accessor that identifies one of
                # the elements in the resource that caused this issue to be raised.  For HTTP
                # errors, will be "http." + the parameter name.
                StructField("location", ArrayType(StringType()), True),
                # A [simple subset of FHIRPath](fhirpath.html#simple) limited to element names,
                # repetition indicators and the default child accessor that identifies one of
                # the elements in the resource that caused this issue to be raised.
                StructField("expression", ArrayType(StringType()), True),
            ]
        )
        return schema
