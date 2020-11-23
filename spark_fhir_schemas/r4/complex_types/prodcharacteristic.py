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
class ProdCharacteristicSchema:
    """
    The marketing status describes the date when a medicinal product is actually
    put on the market or the date as of which it is no longer available.
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
        The marketing status describes the date when a medicinal product is actually
        put on the market or the date as of which it is no longer available.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        height: Where applicable, the height can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        width: Where applicable, the width can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        depth: Where applicable, the depth can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        weight: Where applicable, the weight can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        nominalVolume: Where applicable, the nominal volume can be specified using a numerical value
            and its unit of measurement The unit of measurement shall be specified in
            accordance with ISO 11240 and the resulting terminology The symbol and the
            symbol identifier shall be used.

        externalDiameter: Where applicable, the external diameter can be specified using a numerical
            value and its unit of measurement The unit of measurement shall be specified
            in accordance with ISO 11240 and the resulting terminology The symbol and the
            symbol identifier shall be used.

        shape: Where applicable, the shape can be specified An appropriate controlled
            vocabulary shall be used The term and the term identifier shall be used.

        color: Where applicable, the color can be specified An appropriate controlled
            vocabulary shall be used The term and the term identifier shall be used.

        imprint: Where applicable, the imprint can be specified as text.

        image: Where applicable, the image can be provided The format of the image attachment
            shall be specified by regional implementations.

        scoring: Where applicable, the scoring can be specified An appropriate controlled
            vocabulary shall be used The term and the term identifier shall be used.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit
            and nesting_list.count("ProdCharacteristic") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ProdCharacteristic"]
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
                # Where applicable, the height can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "height",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where applicable, the width can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "width",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where applicable, the depth can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "depth",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where applicable, the weight can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "weight",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where applicable, the nominal volume can be specified using a numerical value
                # and its unit of measurement The unit of measurement shall be specified in
                # accordance with ISO 11240 and the resulting terminology The symbol and the
                # symbol identifier shall be used.
                StructField(
                    "nominalVolume",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where applicable, the external diameter can be specified using a numerical
                # value and its unit of measurement The unit of measurement shall be specified
                # in accordance with ISO 11240 and the resulting terminology The symbol and the
                # symbol identifier shall be used.
                StructField(
                    "externalDiameter",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Where applicable, the shape can be specified An appropriate controlled
                # vocabulary shall be used The term and the term identifier shall be used.
                StructField("shape", StringType(), True),
                # Where applicable, the color can be specified An appropriate controlled
                # vocabulary shall be used The term and the term identifier shall be used.
                StructField("color", ArrayType(StringType()), True),
                # Where applicable, the imprint can be specified as text.
                StructField("imprint", ArrayType(StringType()), True),
                # Where applicable, the image can be provided The format of the image attachment
                # shall be specified by regional implementations.
                StructField(
                    "image",
                    ArrayType(
                        AttachmentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Where applicable, the scoring can be specified An appropriate controlled
                # vocabulary shall be used The term and the term identifier shall be used.
                StructField(
                    "scoring",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
            ]
        )
        return schema
