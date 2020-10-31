from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class AuditEvent_AgentSchema:
    """
    A record of an event made for purposes of maintaining a security log. Typical
    uses include detection of intrusion attempts and monitoring for inappropriate
    usage.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        A record of an event made for purposes of maintaining a security log. Typical
        uses include detection of intrusion attempts and monitoring for inappropriate
        usage.


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

        type: Specification of the participation type the user plays when performing the
            event.

        role: The security role that the user was acting under, that come from local codes
            defined by the access control security system (e.g. RBAC, ABAC) used in the
            local context.

        who: Reference to who this agent is that was involved in the event.

        altId: Alternative agent Identifier. For a human, this should be a user identifier
            text string from authentication system. This identifier would be one known to
            a common authentication system (e.g. single sign-on), if available.

        name: Human-meaningful name for the agent.

        requestor: Indicator that the user is or is not the requestor, or initiator, for the
            event being audited.

        location: Where the event occurred.

        policy: The policy or plan that authorized the activity being recorded. Typically, a
            single activity may have multiple applicable policies, such as patient
            consent, guarantor funding, etc. The policy would also indicate the security
            token used.

        media: Type of media involved. Used when the event is about exporting/importing onto
            media.

        network: Logical network location for application activity, if the activity has a
            network location.

        purposeOfUse: The reason (purpose of use), specific to this agent, that was used during the
            event being recorded.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4.complex_types.auditevent_network import AuditEvent_NetworkSchema
        if recursion_list.count(
            "AuditEvent_Agent"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["AuditEvent_Agent"]
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
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
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
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Specification of the participation type the user plays when performing the
                # event.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The security role that the user was acting under, that come from local codes
                # defined by the access control security system (e.g. RBAC, ABAC) used in the
                # local context.
                StructField(
                    "role",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Reference to who this agent is that was involved in the event.
                StructField(
                    "who",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Alternative agent Identifier. For a human, this should be a user identifier
                # text string from authentication system. This identifier would be one known to
                # a common authentication system (e.g. single sign-on), if available.
                StructField("altId", StringType(), True),
                # Human-meaningful name for the agent.
                StructField("name", StringType(), True),
                # Indicator that the user is or is not the requestor, or initiator, for the
                # event being audited.
                StructField("requestor", BooleanType(), True),
                # Where the event occurred.
                StructField(
                    "location",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The policy or plan that authorized the activity being recorded. Typically, a
                # single activity may have multiple applicable policies, such as patient
                # consent, guarantor funding, etc. The policy would also indicate the security
                # token used.
                StructField(
                    "policy",
                    ArrayType(
                        uriSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Type of media involved. Used when the event is about exporting/importing onto
                # media.
                StructField(
                    "media",
                    CodingSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Logical network location for application activity, if the activity has a
                # network location.
                StructField(
                    "network",
                    AuditEvent_NetworkSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The reason (purpose of use), specific to this agent, that was used during the
                # event being recorded.
                StructField(
                    "purposeOfUse",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
            ]
        )
        return schema
