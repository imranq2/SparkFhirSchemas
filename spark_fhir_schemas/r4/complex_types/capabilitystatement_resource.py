from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatement_ResourceSchema:
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR
    Server for a particular version of FHIR that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
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

        type: A type of resource exposed via the restful interface.

        profile: A specification of the profile that describes the solution's overall support
            for the resource, including any constraints on cardinality, bindings, lengths
            or other limitations. See further discussion in [Using
            Profiles](profiling.html#profile-uses).

        supportedProfile: A list of profiles that represent different use cases supported by the system.
            For a server, "supported by the system" means the system hosts/produces a set
            of resources that are conformant to a particular profile, and allows clients
            that use its services to search using this profile and to find appropriate
            data. For a client, it means the system will search by this profile and
            process data according to the guidance implicit in the profile. See further
            discussion in [Using Profiles](profiling.html#profile-uses).

        documentation: Additional information about the resource type used by the system.

        interaction: Identifies a restful operation supported by the solution.

        versioning: This field is set to no-version to specify that the system does not support
            (server) or use (client) versioning for this resource type. If this has some
            other value, the server must at least correctly track and populate the
            versionId meta-property on resources. If the value is 'versioned-update', then
            the server supports all the versioning features, including using e-tags for
            version integrity in the API.

        readHistory: A flag for whether the server is able to return past versions as part of the
            vRead operation.

        updateCreate: A flag to indicate that the server allows or needs to allow the client to
            create new identities on the server (that is, the client PUTs to a location
            where there is no existing resource). Allowing this operation means that the
            server allows the client to create new identities on the server.

        conditionalCreate: A flag that indicates that the server supports conditional create.

        conditionalRead: A code that indicates how the server supports conditional read.

        conditionalUpdate: A flag that indicates that the server supports conditional update.

        conditionalDelete: A code that indicates how the server supports conditional delete.

        referencePolicy: A set of flags that defines how references are supported.

        searchInclude: A list of _include values supported by the server.

        searchRevInclude: A list of _revinclude (reverse include) values supported by the server.

        searchParam: Search parameters for implementations to support and/or make use of - either
            references to ones defined in the specification, or additional ones defined
            for/by the implementation.

        operation: Definition of an operation or a named query together with its parameters and
            their meaning and type. Consult the definition of the operation for details
            about how to invoke the operation, and the parameters.

        """
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.simple_types.markdown import markdownSchema
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_interaction import CapabilityStatement_InteractionSchema
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_searchparam import CapabilityStatement_SearchParamSchema
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_operation import CapabilityStatement_OperationSchema
        if (
            max_recursion_limit
            and nesting_list.count("CapabilityStatement_Resource") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "CapabilityStatement_Resource"
        ]
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

                # >>> Hiding extension Extension

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

                # >>> Hiding modifierExtension Extension

                # A type of resource exposed via the restful interface.
                StructField(
                    "type",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A specification of the profile that describes the solution's overall support
                # for the resource, including any constraints on cardinality, bindings, lengths
                # or other limitations. See further discussion in [Using
                # Profiles](profiling.html#profile-uses).
                StructField(
                    "profile",
                    canonicalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A list of profiles that represent different use cases supported by the system.
                # For a server, "supported by the system" means the system hosts/produces a set
                # of resources that are conformant to a particular profile, and allows clients
                # that use its services to search using this profile and to find appropriate
                # data. For a client, it means the system will search by this profile and
                # process data according to the guidance implicit in the profile. See further
                # discussion in [Using Profiles](profiling.html#profile-uses).
                StructField(
                    "supportedProfile",
                    ArrayType(
                        canonicalSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Additional information about the resource type used by the system.
                StructField(
                    "documentation",
                    markdownSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Identifies a restful operation supported by the solution.
                StructField(
                    "interaction",
                    ArrayType(
                        CapabilityStatement_InteractionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # This field is set to no-version to specify that the system does not support
                # (server) or use (client) versioning for this resource type. If this has some
                # other value, the server must at least correctly track and populate the
                # versionId meta-property on resources. If the value is 'versioned-update', then
                # the server supports all the versioning features, including using e-tags for
                # version integrity in the API.
                StructField("versioning", StringType(), True),
                # A flag for whether the server is able to return past versions as part of the
                # vRead operation.
                StructField("readHistory", BooleanType(), True),
                # A flag to indicate that the server allows or needs to allow the client to
                # create new identities on the server (that is, the client PUTs to a location
                # where there is no existing resource). Allowing this operation means that the
                # server allows the client to create new identities on the server.
                StructField("updateCreate", BooleanType(), True),
                # A flag that indicates that the server supports conditional create.
                StructField("conditionalCreate", BooleanType(), True),
                # A code that indicates how the server supports conditional read.
                StructField("conditionalRead", StringType(), True),
                # A flag that indicates that the server supports conditional update.
                StructField("conditionalUpdate", BooleanType(), True),
                # A code that indicates how the server supports conditional delete.
                StructField("conditionalDelete", StringType(), True),
                # A set of flags that defines how references are supported.
                # A list of _include values supported by the server.
                StructField("searchInclude", ArrayType(StringType()), True),
                # A list of _revinclude (reverse include) values supported by the server.
                StructField("searchRevInclude", ArrayType(StringType()), True),
                # Search parameters for implementations to support and/or make use of - either
                # references to ones defined in the specification, or additional ones defined
                # for/by the implementation.
                StructField(
                    "searchParam",
                    ArrayType(
                        CapabilityStatement_SearchParamSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Definition of an operation or a named query together with its parameters and
                # their meaning and type. Consult the definition of the operation for details
                # about how to invoke the operation, and the parameters.
                StructField(
                    "operation",
                    ArrayType(
                        CapabilityStatement_OperationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
