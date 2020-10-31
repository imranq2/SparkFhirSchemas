from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CapabilityStatement_Messaging:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server for a particular version of FHIR that may be used as a statement of
        actual server functionality or a statement of required or desired server
        implementation.


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

        endpoint: An endpoint (network accessible address) to which messages and/or replies are
            to be sent.

        reliableCache: Length if the receiver's reliable messaging cache in minutes (if a receiver)
            or how long the cache length on the receiver should be (if a sender).

        documentation: Documentation about the system's messaging capabilities for this endpoint not
            otherwise documented by the capability statement.  For example, the process
            for becoming an authorized messaging exchange partner.

        supportedMessage: References to message definitions for messages this system can send or
            receive.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_endpoint import CapabilityStatement_Endpoint
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_supportedmessage import CapabilityStatement_SupportedMessage
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
                # An endpoint (network accessible address) to which messages and/or replies are
                # to be sent.
                StructField(
                    "endpoint",
                    ArrayType(
                        CapabilityStatement_Endpoint.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Length if the receiver's reliable messaging cache in minutes (if a receiver)
                # or how long the cache length on the receiver should be (if a sender).
                StructField(
                    "reliableCache",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # Documentation about the system's messaging capabilities for this endpoint not
                # otherwise documented by the capability statement.  For example, the process
                # for becoming an authorized messaging exchange partner.
                StructField(
                    "documentation", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # References to message definitions for messages this system can send or
                # receive.
                StructField(
                    "supportedMessage",
                    ArrayType(
                        CapabilityStatement_SupportedMessage.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
