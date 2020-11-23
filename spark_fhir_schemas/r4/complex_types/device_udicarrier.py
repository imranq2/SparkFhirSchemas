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
class Device_UdiCarrierSchema:
    """
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may be a
    medical or non-medical device.
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
        A type of a manufactured item that is used in the provision of healthcare
        without being substantially changed through that activity. The device may be a
        medical or non-medical device.


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

        deviceIdentifier: The device identifier (DI) is a mandatory, fixed portion of a UDI that
            identifies the labeler and the specific version or model of a device.

        issuer: Organization that is charged with issuing UDIs for devices.  For example, the
            US FDA issuers include :
            1) GS1:
            http://hl7.org/fhir/NamingSystem/gs1-di,
            2) HIBCC:
            http://hl7.org/fhir/NamingSystem/hibcc-dI,
            3) ICCBBA for blood containers:
            http://hl7.org/fhir/NamingSystem/iccbba-blood-di,
            4) ICCBA for other devices:
            http://hl7.org/fhir/NamingSystem/iccbba-other-di.

        jurisdiction: The identity of the authoritative source for UDI generation within a
            jurisdiction.  All UDIs are globally unique within a single namespace with the
            appropriate repository uri as the system.  For example,  UDIs of devices
            managed in the U.S. by the FDA, the value is
            http://hl7.org/fhir/NamingSystem/fda-udi.

        carrierAIDC: The full UDI carrier of the Automatic Identification and Data Capture (AIDC)
            technology representation of the barcode string as printed on the packaging of
            the device - e.g., a barcode or RFID.   Because of limitations on character
            sets in XML and the need to round-trip JSON data through XML, AIDC Formats
            *SHALL* be base64 encoded.

        carrierHRF: The full UDI carrier as the human readable form (HRF) representation of the
            barcode string as printed on the packaging of the device.

        entryType: A coded entry to indicate how the data was entered.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.base64binary import base64BinarySchema
        if (
            max_recursion_limit
            and nesting_list.count("Device_UdiCarrier") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Device_UdiCarrier"]
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
                # The device identifier (DI) is a mandatory, fixed portion of a UDI that
                # identifies the labeler and the specific version or model of a device.
                StructField("deviceIdentifier", StringType(), True),
                # Organization that is charged with issuing UDIs for devices.  For example, the
                # US FDA issuers include :
                # 1) GS1:
                # http://hl7.org/fhir/NamingSystem/gs1-di,
                # 2) HIBCC:
                # http://hl7.org/fhir/NamingSystem/hibcc-dI,
                # 3) ICCBBA for blood containers:
                # http://hl7.org/fhir/NamingSystem/iccbba-blood-di,
                # 4) ICCBA for other devices:
                # http://hl7.org/fhir/NamingSystem/iccbba-other-di.
                StructField(
                    "issuer",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The identity of the authoritative source for UDI generation within a
                # jurisdiction.  All UDIs are globally unique within a single namespace with the
                # appropriate repository uri as the system.  For example,  UDIs of devices
                # managed in the U.S. by the FDA, the value is
                # http://hl7.org/fhir/NamingSystem/fda-udi.
                StructField(
                    "jurisdiction",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The full UDI carrier of the Automatic Identification and Data Capture (AIDC)
                # technology representation of the barcode string as printed on the packaging of
                # the device - e.g., a barcode or RFID.   Because of limitations on character
                # sets in XML and the need to round-trip JSON data through XML, AIDC Formats
                # *SHALL* be base64 encoded.
                StructField(
                    "carrierAIDC",
                    base64BinarySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The full UDI carrier as the human readable form (HRF) representation of the
                # barcode string as printed on the packaging of the device.
                StructField("carrierHRF", StringType(), True),
                # A coded entry to indicate how the data was entered.
                StructField("entryType", StringType(), True),
            ]
        )
        return schema
