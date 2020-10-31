from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Device:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A type of a manufactured item that is used in the provision of healthcare
        without being substantially changed through that activity. The device may be a
        medical or non-medical device.


        resourceType: This is a Device resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: Unique instance identifiers assigned to a device by manufacturers other
            organizations or owners.

        definition: The reference to the definition for the device.

        udiCarrier: Unique device identifier (UDI) assigned to device label or package.  Note that
            the Device may include multiple udiCarriers as it either may include just the
            udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
            could have been sold.

        status: Status of the Device availability.

        statusReason: Reason for the dtatus of the Device availability.

        distinctIdentifier: The distinct identification string as required by regulation for a human cell,
            tissue, or cellular and tissue-based product.

        manufacturer: A name of the manufacturer.

        manufactureDate: The date and time when the device was manufactured.

        expirationDate: The date and time beyond which this device is no longer valid or should not be
            used (if applicable).

        lotNumber: Lot number assigned by the manufacturer.

        serialNumber: The serial number assigned by the organization when the device was
            manufactured.

        deviceName: This represents the manufacturer's name of the device as provided by the
            device, from a UDI label, or by a person describing the Device.  This
            typically would be used when a person provides the name(s) or when the device
            represents one of the names available from DeviceDefinition.

        modelNumber: The model number for the device.

        partNumber: The part number of the device.

        type: The kind or type of device.

        specialization: The capabilities supported on a  device, the standards to which the device
            conforms for a particular purpose, and used for the communication.

        version: The actual design of the device or software version running on the device.

        property: The actual configuration settings of a device as it actually operates, e.g.,
            regulation status, time properties.

        patient: Patient information, If the device is affixed to a person.

        owner: An organization that is responsible for the provision and ongoing maintenance
            of the device.

        contact: Contact details for an organization or a particular human that is responsible
            for the device.

        location: The place where the device can be found.

        url: A network address on which the device may be contacted directly.

        note: Descriptive information, usage information or implantation information that is
            not captured in an existing element.

        safety: Provides additional safety characteristics about a medical device.  For
            example devices containing latex.

        parent: The parent device.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.device_udicarrier import Device_UdiCarrier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.device_devicename import Device_DeviceName
        from spark_fhir_schemas.r4.complex_types.device_specialization import Device_Specialization
        from spark_fhir_schemas.r4.complex_types.device_version import Device_Version
        from spark_fhir_schemas.r4.complex_types.device_property import Device_Property
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Device resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Unique instance identifiers assigned to a device by manufacturers other
                # organizations or owners.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The reference to the definition for the device.
                StructField(
                    "definition", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Unique device identifier (UDI) assigned to device label or package.  Note that
                # the Device may include multiple udiCarriers as it either may include just the
                # udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
                # could have been sold.
                StructField(
                    "udiCarrier",
                    ArrayType(
                        Device_UdiCarrier.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Status of the Device availability.
                StructField("status", StringType(), True),
                # Reason for the dtatus of the Device availability.
                StructField(
                    "statusReason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The distinct identification string as required by regulation for a human cell,
                # tissue, or cellular and tissue-based product.
                StructField("distinctIdentifier", StringType(), True),
                # A name of the manufacturer.
                StructField("manufacturer", StringType(), True),
                # The date and time when the device was manufactured.
                StructField(
                    "manufactureDate",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                # The date and time beyond which this device is no longer valid or should not be
                # used (if applicable).
                StructField(
                    "expirationDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Lot number assigned by the manufacturer.
                StructField("lotNumber", StringType(), True),
                # The serial number assigned by the organization when the device was
                # manufactured.
                StructField("serialNumber", StringType(), True),
                # This represents the manufacturer's name of the device as provided by the
                # device, from a UDI label, or by a person describing the Device.  This
                # typically would be used when a person provides the name(s) or when the device
                # represents one of the names available from DeviceDefinition.
                StructField(
                    "deviceName",
                    ArrayType(
                        Device_DeviceName.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The model number for the device.
                StructField("modelNumber", StringType(), True),
                # The part number of the device.
                StructField("partNumber", StringType(), True),
                # The kind or type of device.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The capabilities supported on a  device, the standards to which the device
                # conforms for a particular purpose, and used for the communication.
                StructField(
                    "specialization",
                    ArrayType(
                        Device_Specialization.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The actual design of the device or software version running on the device.
                StructField(
                    "version",
                    ArrayType(Device_Version.get_schema(recursion_depth + 1)),
                    True
                ),
                # The actual configuration settings of a device as it actually operates, e.g.,
                # regulation status, time properties.
                StructField(
                    "property",
                    ArrayType(Device_Property.get_schema(recursion_depth + 1)),
                    True
                ),
                # Patient information, If the device is affixed to a person.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # An organization that is responsible for the provision and ongoing maintenance
                # of the device.
                StructField(
                    "owner", Reference.get_schema(recursion_depth + 1), True
                ),
                # Contact details for an organization or a particular human that is responsible
                # for the device.
                StructField(
                    "contact",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                # The place where the device can be found.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # A network address on which the device may be contacted directly.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # Descriptive information, usage information or implantation information that is
                # not captured in an existing element.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Provides additional safety characteristics about a medical device.  For
                # example devices containing latex.
                StructField(
                    "safety",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The parent device.
                StructField(
                    "parent", Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
