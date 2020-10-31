from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Group:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Represents a defined collection of entities that may be discussed or acted
        upon collectively but which are not expected to act collectively, and are not
        formally or legally recognized; i.e. a collection of entities that isn't an
        Organization.


        resourceType: This is a Group resource

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

        identifier: A unique business identifier for this group.

        active: Indicates whether the record for the group is available for use or is merely
            being retained for historical purposes.

        type: Identifies the broad classification of the kind of resources the group
            includes.

        actual: If true, indicates that the resource refers to a specific group of real
            individuals.  If false, the group defines a set of intended individuals.

        code: Provides a specific type of resource the group includes; e.g. "cow",
            "syringe", etc.

        name: A label assigned to the group for human identification and communication.

        quantity: A count of the number of resource instances that are part of the group.

        managingEntity: Entity responsible for defining and maintaining Group characteristics and/or
            registered members.

        characteristic: Identifies traits whose presence r absence is shared by members of the group.

        member: Identifies the resource instances that are members of the group.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.group_characteristic import Group_Characteristic
        from spark_fhir_schemas.r4.complex_types.group_member import Group_Member
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Group resource
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
                # A unique business identifier for this group.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Indicates whether the record for the group is available for use or is merely
                # being retained for historical purposes.
                StructField("active", BooleanType(), True),
                # Identifies the broad classification of the kind of resources the group
                # includes.
                StructField("type", StringType(), True),
                # If true, indicates that the resource refers to a specific group of real
                # individuals.  If false, the group defines a set of intended individuals.
                StructField("actual", BooleanType(), True),
                # Provides a specific type of resource the group includes; e.g. "cow",
                # "syringe", etc.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A label assigned to the group for human identification and communication.
                StructField("name", StringType(), True),
                # A count of the number of resource instances that are part of the group.
                StructField(
                    "quantity", unsignedInt.get_schema(recursion_depth + 1),
                    True
                ),
                # Entity responsible for defining and maintaining Group characteristics and/or
                # registered members.
                StructField(
                    "managingEntity",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies traits whose presence r absence is shared by members of the group.
                StructField(
                    "characteristic",
                    ArrayType(
                        Group_Characteristic.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies the resource instances that are members of the group.
                StructField(
                    "member",
                    ArrayType(Group_Member.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
