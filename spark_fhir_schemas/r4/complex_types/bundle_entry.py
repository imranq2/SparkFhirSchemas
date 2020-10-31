from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Bundle_Entry:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A container for a collection of resources.


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

        link: A series of links that provide context to this entry.

        fullUrl: The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id
            in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be
            version-independent URL consistent with the Resource.id. The fullUrl is a
            version independent reference to the resource. The fullUrl element SHALL have
            a value except that:
            * fullUrl can be empty on a POST (although it does not need to when specifying
            a temporary id for reference in the bundle)
            * Results from operations might involve resources that are not identified.

        resource: The Resource for the entry. The purpose/meaning of the resource is determined
            by the Bundle.type.

        search: Information about the search process that lead to the creation of this entry.

        request: Additional information about how this entry should be processed as part of a
            transaction or batch.  For history, it shows how the entry was processed to
            create the version contained in the entry.

        response: Indicates the results of processing the corresponding 'request' entry in the
            batch or transaction being responded to or what the results of an operation
            where when returning history.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.bundle_link import Bundle_Link
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.bundle_search import Bundle_Search
        from spark_fhir_schemas.r4.complex_types.bundle_request import Bundle_Request
        from spark_fhir_schemas.r4.complex_types.bundle_response import Bundle_Response
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
                # A series of links that provide context to this entry.
                StructField(
                    "link",
                    ArrayType(Bundle_Link.get_schema(recursion_depth + 1)),
                    True
                ),
                # The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id
                # in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be
                # version-independent URL consistent with the Resource.id. The fullUrl is a
                # version independent reference to the resource. The fullUrl element SHALL have
                # a value except that:
                # * fullUrl can be empty on a POST (although it does not need to when specifying
                # a temporary id for reference in the bundle)
                # * Results from operations might involve resources that are not identified.
                StructField(
                    "fullUrl", uri.get_schema(recursion_depth + 1), True
                ),
                # The Resource for the entry. The purpose/meaning of the resource is determined
                # by the Bundle.type.
                StructField(
                    "resource", ResourceList.get_schema(recursion_depth + 1),
                    True
                ),
                # Information about the search process that lead to the creation of this entry.
                StructField(
                    "search", Bundle_Search.get_schema(recursion_depth + 1),
                    True
                ),
                # Additional information about how this entry should be processed as part of a
                # transaction or batch.  For history, it shows how the entry was processed to
                # create the version contained in the entry.
                StructField(
                    "request", Bundle_Request.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the results of processing the corresponding 'request' entry in the
                # batch or transaction being responded to or what the results of an operation
                # where when returning history.
                StructField(
                    "response",
                    Bundle_Response.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
