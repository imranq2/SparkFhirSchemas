from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DataRequirementSchema:
    """
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
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

        type: The type of the required data, specified as the type name of a resource. For
            profiles, this value is set to the type of the base resource of the profile.

        profile: The profile of the required data, specified as the uri of the profile
            definition.

        subjectCodeableConcept: The intended subjects of the data requirement. If this element is not
            provided, a Patient subject is assumed.

        subjectReference: The intended subjects of the data requirement. If this element is not
            provided, a Patient subject is assumed.

        mustSupport: Indicates that specific elements of the type are referenced by the knowledge
            module and must be supported by the consumer in order to obtain an effective
            evaluation. This does not mean that a value is required for this element, only
            that the consuming system must understand the element and be able to provide
            values for it if they are available.

            The value of mustSupport SHALL be a FHIRPath resolveable on the type of the
            DataRequirement. The path SHALL consist only of identifiers, constant
            indexers, and .resolve() (see the [Simple FHIRPath
            Profile](fhirpath.html#simple) for full details).

        codeFilter: Code filters specify additional constraints on the data, specifying the value
            set of interest for a particular element of the data. Each code filter defines
            an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.

        dateFilter: Date filters specify additional constraints on the data in terms of the
            applicable date range for specific elements. Each date filter specifies an
            additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.

        limit: Specifies a maximum number of results that are required (uses the _count
            search parameter).

        sort: Specifies the order of the results to be returned.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.datarequirement_codefilter import DataRequirement_CodeFilterSchema
        from spark_fhir_schemas.r4.complex_types.datarequirement_datefilter import DataRequirement_DateFilterSchema
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveIntSchema
        from spark_fhir_schemas.r4.complex_types.datarequirement_sort import DataRequirement_SortSchema
        if recursion_list.count(
            "DataRequirement"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["DataRequirement"]
        schema = StructType(
            [
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The type of the required data, specified as the type name of a resource. For
                # profiles, this value is set to the type of the base resource of the profile.
                StructField(
                    "type",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The profile of the required data, specified as the uri of the profile
                # definition.
                StructField(
                    "profile",
                    ArrayType(
                        canonicalSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The intended subjects of the data requirement. If this element is not
                # provided, a Patient subject is assumed.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The intended subjects of the data requirement. If this element is not
                # provided, a Patient subject is assumed.
                StructField(
                    "subjectReference",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates that specific elements of the type are referenced by the knowledge
                # module and must be supported by the consumer in order to obtain an effective
                # evaluation. This does not mean that a value is required for this element, only
                # that the consuming system must understand the element and be able to provide
                # values for it if they are available.
                #
                # The value of mustSupport SHALL be a FHIRPath resolveable on the type of the
                # DataRequirement. The path SHALL consist only of identifiers, constant
                # indexers, and .resolve() (see the [Simple FHIRPath
                # Profile](fhirpath.html#simple) for full details).
                StructField("mustSupport", ArrayType(StringType()), True),
                # Code filters specify additional constraints on the data, specifying the value
                # set of interest for a particular element of the data. Each code filter defines
                # an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.
                StructField(
                    "codeFilter",
                    ArrayType(
                        DataRequirement_CodeFilterSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Date filters specify additional constraints on the data in terms of the
                # applicable date range for specific elements. Each date filter specifies an
                # additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
                StructField(
                    "dateFilter",
                    ArrayType(
                        DataRequirement_DateFilterSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Specifies a maximum number of results that are required (uses the _count
                # search parameter).
                StructField(
                    "limit",
                    positiveIntSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Specifies the order of the results to be returned.
                StructField(
                    "sort",
                    ArrayType(
                        DataRequirement_SortSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
            ]
        )
        return schema
