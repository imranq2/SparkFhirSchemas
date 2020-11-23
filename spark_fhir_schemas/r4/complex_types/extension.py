from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ExtensionSchema:
    """
    Optional Extension Element - found in all resources.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        Optional Extension Element - found in all resources.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        url: Source of the definition for the extension code - a logical name or a URL.

        valueBoolean: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCode: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDate: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDateTime: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDecimal: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueId: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueInteger: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valuePositiveInt: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueString: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueTime: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUnsignedInt: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUri: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUrl: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCoding: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCount: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueIdentifier: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueMoney: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valuePeriod: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueQuantity: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueRange: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueReference: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        """
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4.complex_types.count import CountSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.money import MoneySchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        if (
            max_recursion_limit
            and nesting_list.count("Extension") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Extension"]
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
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Source of the definition for the extension code - a logical name or a URL.
                StructField(
                    "url",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueBoolean", BooleanType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueCode", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDate", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDateTime", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDecimal", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueId", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueInteger", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valuePositiveInt", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueString", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueTime", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUnsignedInt", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUri", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUrl", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCoding",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCount",
                    CountSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueMoney",
                    MoneySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valuePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
