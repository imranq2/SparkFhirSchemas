from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatement_MessagingSchema:
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR
    Server that may be used as a statement of actual server functionality or a
    statement of required or desired server implementation.
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
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server that may be used as a statement of actual server functionality or a
        statement of required or desired server implementation.


        endpoint: An endpoint (network accessible address) to which messages and/or replies are
            to be sent.

        reliableCache: Length if the receiver's reliable messaging cache in minutes (if a receiver)
            or how long the cache length on the receiver should be (if a sender).

        documentation: Documentation about the system's messaging capabilities for this endpoint not
            otherwise documented by the capability statement.  For example, the process
            for becoming an authorized messaging exchange partner.

        supportedMessage: References to message definitions for messages this system can send or
            receive.

        event: A description of the solution's support for an event at this end-point.

        """
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_endpoint import CapabilityStatement_EndpointSchema
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_supportedmessage import CapabilityStatement_SupportedMessageSchema
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_event import CapabilityStatement_EventSchema
        if (
            max_recursion_limit
            and nesting_list.count("CapabilityStatement_Messaging") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "CapabilityStatement_Messaging"
        ]
        schema = StructType(
            [
                # An endpoint (network accessible address) to which messages and/or replies are
                # to be sent.
                StructField(
                    "endpoint",
                    ArrayType(
                        CapabilityStatement_EndpointSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Length if the receiver's reliable messaging cache in minutes (if a receiver)
                # or how long the cache length on the receiver should be (if a sender).
                StructField("reliableCache", IntegerType(), True),
                # Documentation about the system's messaging capabilities for this endpoint not
                # otherwise documented by the capability statement.  For example, the process
                # for becoming an authorized messaging exchange partner.
                StructField("documentation", StringType(), True),
                # References to message definitions for messages this system can send or
                # receive.
                StructField(
                    "supportedMessage",
                    ArrayType(
                        CapabilityStatement_SupportedMessageSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A description of the solution's support for an event at this end-point.
                StructField(
                    "event",
                    ArrayType(
                        CapabilityStatement_EventSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
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
