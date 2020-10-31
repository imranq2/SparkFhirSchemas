from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DeviceDefinitionSchema:
    """
    The characteristics, operational status and capabilities of a medical-related
    component of a medical device.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        The characteristics, operational status and capabilities of a medical-related
        component of a medical device.


        resourceType: This is a DeviceDefinition resource

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

        identifier: Unique instance identifiers assigned to a device by the software,
            manufacturers, other organizations or owners. For example: handle ID.

        udiDeviceIdentifier: Unique device identifier (UDI) assigned to device label or package.  Note that
            the Device may include multiple udiCarriers as it either may include just the
            udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
            could have been sold.

        manufacturerString: A name of the manufacturer.

        manufacturerReference: A name of the manufacturer.

        deviceName: A name given to the device to identify it.

        modelNumber: The model number for the device.

        type: What kind of device or device system this is.

        specialization: The capabilities supported on a  device, the standards to which the device
            conforms for a particular purpose, and used for the communication.

        version: The available versions of the device, e.g., software versions.

        safety: Safety characteristics of the device.

        shelfLifeStorage: Shelf Life and storage information.

        physicalCharacteristics: Dimensions, color etc.

        languageCode: Language code for the human-readable text strings produced by the device (all
            supported).

        capability: Device capabilities.

        property: The actual configuration settings of a device as it actually operates, e.g.,
            regulation status, time properties.

        owner: An organization that is responsible for the provision and ongoing maintenance
            of the device.

        contact: Contact details for an organization or a particular human that is responsible
            for the device.

        url: A network address on which the device may be contacted directly.

        onlineInformation: Access to on-line information about the device.

        note: Descriptive information, usage information or implantation information that is
            not captured in an existing element.

        quantity: The quantity of the device present in the packaging (e.g. the number of
            devices present in a pack, or the number of devices in the same package of the
            medicinal product).

        parentDevice: The parent device it can be part of.

        material: A substance used to create the material(s) of which the device is made.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.devicedefinition_udideviceidentifier import DeviceDefinition_UdiDeviceIdentifierSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.devicedefinition_devicename import DeviceDefinition_DeviceNameSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.devicedefinition_specialization import DeviceDefinition_SpecializationSchema
        from spark_fhir_schemas.r4.complex_types.productshelflife import ProductShelfLifeSchema
        from spark_fhir_schemas.r4.complex_types.prodcharacteristic import ProdCharacteristicSchema
        from spark_fhir_schemas.r4.complex_types.devicedefinition_capability import DeviceDefinition_CapabilitySchema
        from spark_fhir_schemas.r4.complex_types.devicedefinition_property import DeviceDefinition_PropertySchema
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPointSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.devicedefinition_material import DeviceDefinition_MaterialSchema
        if recursion_list.count(
            "DeviceDefinition"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["DeviceDefinition"]
        schema = StructType(
            [
                # This is a DeviceDefinition resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Unique instance identifiers assigned to a device by the software,
                # manufacturers, other organizations or owners. For example: handle ID.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Unique device identifier (UDI) assigned to device label or package.  Note that
                # the Device may include multiple udiCarriers as it either may include just the
                # udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
                # could have been sold.
                StructField(
                    "udiDeviceIdentifier",
                    ArrayType(
                        DeviceDefinition_UdiDeviceIdentifierSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # A name of the manufacturer.
                StructField("manufacturerString", StringType(), True),
                # A name of the manufacturer.
                StructField(
                    "manufacturerReference",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A name given to the device to identify it.
                StructField(
                    "deviceName",
                    ArrayType(
                        DeviceDefinition_DeviceNameSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The model number for the device.
                StructField("modelNumber", StringType(), True),
                # What kind of device or device system this is.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The capabilities supported on a  device, the standards to which the device
                # conforms for a particular purpose, and used for the communication.
                StructField(
                    "specialization",
                    ArrayType(
                        DeviceDefinition_SpecializationSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The available versions of the device, e.g., software versions.
                StructField("version", ArrayType(StringType()), True),
                # Safety characteristics of the device.
                StructField(
                    "safety",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Shelf Life and storage information.
                StructField(
                    "shelfLifeStorage",
                    ArrayType(
                        ProductShelfLifeSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Dimensions, color etc.
                StructField(
                    "physicalCharacteristics",
                    ProdCharacteristicSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Language code for the human-readable text strings produced by the device (all
                # supported).
                StructField(
                    "languageCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Device capabilities.
                StructField(
                    "capability",
                    ArrayType(
                        DeviceDefinition_CapabilitySchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The actual configuration settings of a device as it actually operates, e.g.,
                # regulation status, time properties.
                StructField(
                    "property",
                    ArrayType(
                        DeviceDefinition_PropertySchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # An organization that is responsible for the provision and ongoing maintenance
                # of the device.
                StructField(
                    "owner",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Contact details for an organization or a particular human that is responsible
                # for the device.
                StructField(
                    "contact",
                    ArrayType(
                        ContactPointSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # A network address on which the device may be contacted directly.
                StructField(
                    "url",
                    uriSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Access to on-line information about the device.
                StructField(
                    "onlineInformation",
                    uriSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Descriptive information, usage information or implantation information that is
                # not captured in an existing element.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The quantity of the device present in the packaging (e.g. the number of
                # devices present in a pack, or the number of devices in the same package of the
                # medicinal product).
                StructField(
                    "quantity",
                    QuantitySchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The parent device it can be part of.
                StructField(
                    "parentDevice",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A substance used to create the material(s) of which the device is made.
                StructField(
                    "material",
                    ArrayType(
                        DeviceDefinition_MaterialSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
            ]
        )
        return schema
