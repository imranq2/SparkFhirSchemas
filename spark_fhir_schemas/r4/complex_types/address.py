from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class AddressSchema:
    """
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey addresses
    for use in delivering mail as well as for visiting locations which might not
    be valid for mail delivery.  There are a variety of postal address formats
    defined around the world.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An address expressed using postal conventions (as opposed to GPS or other
        location definition formats).  This data type may be used to convey addresses
        for use in delivering mail as well as for visiting locations which might not
        be valid for mail delivery.  There are a variety of postal address formats
        defined around the world.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        use: The purpose of this address.

        type: Distinguishes between physical addresses (those you can visit) and mailing
            addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.

        text: Specifies the entire address as it should be displayed e.g. on a postal label.
            This may be provided instead of or as well as the specific parts.

        line: This component contains the house number, apartment number, street name,
            street direction,  P.O. Box number, delivery hints, and similar address
            information.

        city: The name of the city, town, suburb, village or other community or delivery
            center.

        district: The name of the administrative area (county).

        state: Sub-unit of a country with limited sovereignty in a federally organized
            country. A code may be used if codes are in common use (e.g. US 2 letter state
            codes).

        postalCode: A postal code designating a region defined by the postal service.

        country: Country - a nation as commonly understood or generally accepted.

        period: Time period when address was/is in use.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        if recursion_depth > 3:
            return StructType([])
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The purpose of this address.
                StructField("use", StringType(), True),
                # Distinguishes between physical addresses (those you can visit) and mailing
                # addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.
                StructField("type", StringType(), True),
                # Specifies the entire address as it should be displayed e.g. on a postal label.
                # This may be provided instead of or as well as the specific parts.
                StructField("text", StringType(), True),
                # This component contains the house number, apartment number, street name,
                # street direction,  P.O. Box number, delivery hints, and similar address
                # information.
                StructField("line", ArrayType(StringType()), True),
                # The name of the city, town, suburb, village or other community or delivery
                # center.
                StructField("city", StringType(), True),
                # The name of the administrative area (county).
                StructField("district", StringType(), True),
                # Sub-unit of a country with limited sovereignty in a federally organized
                # country. A code may be used if codes are in common use (e.g. US 2 letter state
                # codes).
                StructField("state", StringType(), True),
                # A postal code designating a region defined by the postal service.
                StructField("postalCode", StringType(), True),
                # Country - a nation as commonly understood or generally accepted.
                StructField("country", StringType(), True),
                # Time period when address was/is in use.
                StructField(
                    "period", PeriodSchema.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
