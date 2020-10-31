from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DataRequirement_CodeFilter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes a required data item for evaluation in terms of the type of data,
        and optional code or date-based filters of the data.


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

        path: The code-valued attribute of the filter. The specified path SHALL be a
            FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
            consist only of identifiers, constant indexers, and .resolve(). The path is
            allowed to contain qualifiers (.) to traverse sub-elements, as well as
            indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
            FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
            must be an integer constant. The path must resolve to an element of type code,
            Coding, or CodeableConcept.

        searchParam: A token parameter that refers to a search parameter defined on the specified
            type of the DataRequirement, and which searches on elements of type code,
            Coding, or CodeableConcept.

        valueSet: The valueset for the code filter. The valueSet and code elements are additive.
            If valueSet is specified, the filter will return only those data items for
            which the value of the code-valued element specified in the path is a member
            of the specified valueset.

        code: The codes for the code filter. If values are given, the filter will return
            only those data items for which the code-valued attribute specified by the
            path has a value that is one of the specified codes. If codes are specified in
            addition to a value set, the filter returns items matching a code in the value
            set or one of the specified codes.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.coding import Coding
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
                # The code-valued attribute of the filter. The specified path SHALL be a
                # FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
                # consist only of identifiers, constant indexers, and .resolve(). The path is
                # allowed to contain qualifiers (.) to traverse sub-elements, as well as
                # indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
                # FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
                # must be an integer constant. The path must resolve to an element of type code,
                # Coding, or CodeableConcept.
                StructField("path", StringType(), True),
                # A token parameter that refers to a search parameter defined on the specified
                # type of the DataRequirement, and which searches on elements of type code,
                # Coding, or CodeableConcept.
                StructField("searchParam", StringType(), True),
                # The valueset for the code filter. The valueSet and code elements are additive.
                # If valueSet is specified, the filter will return only those data items for
                # which the value of the code-valued element specified in the path is a member
                # of the specified valueset.
                StructField(
                    "valueSet", canonical.get_schema(recursion_depth + 1), True
                ),
                # The codes for the code filter. If values are given, the filter will return
                # only those data items for which the code-valued attribute specified by the
                # path has a value that is one of the specified codes. If codes are specified in
                # addition to a value set, the filter returns items matching a code in the value
                # set or one of the specified codes.
                StructField(
                    "code", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
