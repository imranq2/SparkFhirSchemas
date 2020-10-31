from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TestScript_Operation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.


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

        type: Server interaction or operation type.

        resource: The type of the resource.  See http://build.fhir.org/resourcelist.html.

        label: The label would be used for tracking/logging purposes by test engines.

        description: The description would be used by test engines for tracking and reporting
            purposes.

        accept: The mime-type to use for RESTful operation in the 'Accept' header.

        contentType: The mime-type to use for RESTful operation in the 'Content-Type' header.

        destination: The server where the request message is destined for.  Must be one of the
            server numbers listed in TestScript.destination section.

        encodeRequestUrl: Whether or not to implicitly send the request url in encoded format. The
            default is true to match the standard RESTful client behavior. Set to false
            when communicating with a server that does not support encoded url paths.

        method: The HTTP method the test engine MUST use for this operation regardless of any
            other operation details.

        origin: The server where the request message originates from.  Must be one of the
            server numbers listed in TestScript.origin section.

        params: Path plus parameters after [type].  Used to set parts of the request URL
            explicitly.

        requestHeader: Header elements would be used to set HTTP headers.

        requestId: The fixture id (maybe new) to map to the request.

        responseId: The fixture id (maybe new) to map to the response.

        sourceId: The id of the fixture used as the body of a PUT or POST request.

        targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET
            requests.

        url: Complete request URL.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.testscript_requestheader import TestScript_RequestHeader
        from spark_fhir_schemas.r4.simple_types.id import id
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
                # Server interaction or operation type.
                StructField(
                    "type", Coding.get_schema(recursion_depth + 1), True
                ),
                # The type of the resource.  See http://build.fhir.org/resourcelist.html.
                StructField(
                    "resource", code.get_schema(recursion_depth + 1), True
                ),
                # The label would be used for tracking/logging purposes by test engines.
                StructField("label", StringType(), True),
                # The description would be used by test engines for tracking and reporting
                # purposes.
                StructField("description", StringType(), True),
                # The mime-type to use for RESTful operation in the 'Accept' header.
                StructField(
                    "accept", code.get_schema(recursion_depth + 1), True
                ),
                # The mime-type to use for RESTful operation in the 'Content-Type' header.
                StructField(
                    "contentType", code.get_schema(recursion_depth + 1), True
                ),
                # The server where the request message is destined for.  Must be one of the
                # server numbers listed in TestScript.destination section.
                StructField(
                    "destination", integer.get_schema(recursion_depth + 1),
                    True
                ),
                # Whether or not to implicitly send the request url in encoded format. The
                # default is true to match the standard RESTful client behavior. Set to false
                # when communicating with a server that does not support encoded url paths.
                StructField("encodeRequestUrl", BooleanType(), True),
                # The HTTP method the test engine MUST use for this operation regardless of any
                # other operation details.
                StructField("method", StringType(), True),
                # The server where the request message originates from.  Must be one of the
                # server numbers listed in TestScript.origin section.
                StructField(
                    "origin", integer.get_schema(recursion_depth + 1), True
                ),
                # Path plus parameters after [type].  Used to set parts of the request URL
                # explicitly.
                StructField("params", StringType(), True),
                # Header elements would be used to set HTTP headers.
                StructField(
                    "requestHeader",
                    ArrayType(
                        TestScript_RequestHeader.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The fixture id (maybe new) to map to the request.
                StructField(
                    "requestId", id.get_schema(recursion_depth + 1), True
                ),
                # The fixture id (maybe new) to map to the response.
                StructField(
                    "responseId", id.get_schema(recursion_depth + 1), True
                ),
                # The id of the fixture used as the body of a PUT or POST request.
                StructField(
                    "sourceId", id.get_schema(recursion_depth + 1), True
                ),
                # Id of fixture used for extracting the [id],  [type], and [vid] for GET
                # requests.
                StructField(
                    "targetId", id.get_schema(recursion_depth + 1), True
                ),
                # Complete request URL.
                StructField("url", StringType(), True),
            ]
        )
        return schema
