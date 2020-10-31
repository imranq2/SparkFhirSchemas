from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AuditEvent_Agent:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.auditevent_network import AuditEvent_Network
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
                # Specification of the participation type the user plays when performing the
                # event.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The security role that the user was acting under, that come from local codes
                # defined by the access control security system (e.g. RBAC, ABAC) used in the
                # local context.
                StructField(
                    "role",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Reference to who this agent is that was involved in the event.
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
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
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # The policy or plan that authorized the activity being recorded. Typically, a
                # single activity may have multiple applicable policies, such as patient
                # consent, guarantor funding, etc. The policy would also indicate the security
                # token used.
                StructField(
                    "policy", ArrayType(uri.get_schema(recursion_depth + 1)),
                    True
                ),
                # Type of media involved. Used when the event is about exporting/importing onto
                # media.
                StructField(
                    "media", Coding.get_schema(recursion_depth + 1), True
                ),
                # Logical network location for application activity, if the activity has a
                # network location.
                StructField(
                    "network",
                    AuditEvent_Network.get_schema(recursion_depth + 1), True
                ),
                # The reason (purpose of use), specific to this agent, that was used during the
                # event being recorded.
                StructField(
                    "purposeOfUse",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
