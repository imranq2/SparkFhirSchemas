from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OperationDefinition_ParameterSchema:
    """
    A formal computable definition of an operation (on the RESTful interface) or a
    named query (using the search interaction).
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
        """
        A formal computable definition of an operation (on the RESTful interface) or a
        named query (using the search interaction).


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

        name: The name of used to identify the parameter.

        use: Whether this is an input or an output parameter.

        min: The minimum number of times this parameter SHALL appear in the request or
            response.

        max: The maximum number of times this element is permitted to appear in the request
            or response.

        documentation: Describes the meaning or use of this parameter.

        type: The type for this parameter.

        targetProfile: Used when the type is "Reference" or "canonical", and identifies a profile
            structure or implementation Guide that applies to the target of the reference
            this parameter refers to. If any profiles are specified, then the content must
            conform to at least one of them. The URL can be a local reference - to a
            contained StructureDefinition, or a reference to another StructureDefinition
            or Implementation Guide by a canonical URL. When an implementation guide is
            specified, the target resource SHALL conform to at least one profile defined
            in the implementation guide.

        searchType: How the parameter is understood as a search parameter. This is only used if
            the parameter type is 'string'.

        binding: Binds to a value set if this parameter is coded (code, Coding,
            CodeableConcept).

        referencedFrom: Identifies other resource parameters within the operation invocation that are
            expected to resolve to this resource.

        part: The parts of a nested Parameter.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.simple_types.integer import integerSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.operationdefinition_binding import OperationDefinition_BindingSchema
        from spark_fhir_schemas.r4.complex_types.operationdefinition_referencedfrom import OperationDefinition_ReferencedFromSchema
        if (
            max_recursion_limit
            and nesting_list.count("OperationDefinition_Parameter") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "OperationDefinition_Parameter"
        ]
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
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The name of used to identify the parameter.
                StructField(
                    "name",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Whether this is an input or an output parameter.
                StructField("use", StringType(), True),
                # The minimum number of times this parameter SHALL appear in the request or
                # response.
                StructField(
                    "min",
                    integerSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The maximum number of times this element is permitted to appear in the request
                # or response.
                StructField("max", StringType(), True),
                # Describes the meaning or use of this parameter.
                StructField("documentation", StringType(), True),
                # The type for this parameter.
                StructField(
                    "type",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Used when the type is "Reference" or "canonical", and identifies a profile
                # structure or implementation Guide that applies to the target of the reference
                # this parameter refers to. If any profiles are specified, then the content must
                # conform to at least one of them. The URL can be a local reference - to a
                # contained StructureDefinition, or a reference to another StructureDefinition
                # or Implementation Guide by a canonical URL. When an implementation guide is
                # specified, the target resource SHALL conform to at least one profile defined
                # in the implementation guide.
                StructField(
                    "targetProfile",
                    ArrayType(
                        canonicalSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # How the parameter is understood as a search parameter. This is only used if
                # the parameter type is 'string'.
                StructField("searchType", StringType(), True),
                # Binds to a value set if this parameter is coded (code, Coding,
                # CodeableConcept).
                StructField(
                    "binding",
                    OperationDefinition_BindingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Identifies other resource parameters within the operation invocation that are
                # expected to resolve to this resource.
                StructField(
                    "referencedFrom",
                    ArrayType(
                        OperationDefinition_ReferencedFromSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The parts of a nested Parameter.
                StructField(
                    "part",
                    ArrayType(
                        OperationDefinition_ParameterSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
