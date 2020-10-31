from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Goal:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes the intended objective(s) for a patient, group or organization care,
        for example, weight loss, restoring an activity of daily living, obtaining
        herd immunity via immunization, meeting a process improvement objective, etc.


        resourceType: This is a Goal resource

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

        identifier: Business identifiers assigned to this goal by the performer or other systems
            which remain constant as the resource is updated and propagates from server to
            server.

        lifecycleStatus: The state of the goal throughout its lifecycle.

        achievementStatus: Describes the progression, or lack thereof, towards the goal against the
            target.

        category: Indicates a category the goal falls within.

        priority: Identifies the mutually agreed level of importance associated with
            reaching/sustaining the goal.

        description: Human-readable and/or coded description of a specific desired objective of
            care, such as "control blood pressure" or "negotiate an obstacle course" or
            "dance with child at wedding".

        subject: Identifies the patient, group or organization for whom the goal is being
            established.

        startDate: The date or event after which the goal should begin being pursued.

        startCodeableConcept: The date or event after which the goal should begin being pursued.

        target: Indicates what should be done by when.

        statusDate: Identifies when the current status.  I.e. When initially created, when
            achieved, when cancelled, etc.

        statusReason: Captures the reason for the current status.

        expressedBy: Indicates whose goal this is - patient goal, practitioner goal, etc.

        addresses: The identified conditions and other health record elements that are intended
            to be addressed by the goal.

        note: Any comments related to the goal.

        outcomeCode: Identifies the change (or lack of change) at the point when the status of the
            goal is assessed.

        outcomeReference: Details of what's changed (or not changed).

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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.goal_target import Goal_Target
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Goal resource
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
                # Business identifiers assigned to this goal by the performer or other systems
                # which remain constant as the resource is updated and propagates from server to
                # server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The state of the goal throughout its lifecycle.
                StructField("lifecycleStatus", StringType(), True),
                # Describes the progression, or lack thereof, towards the goal against the
                # target.
                StructField(
                    "achievementStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates a category the goal falls within.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Identifies the mutually agreed level of importance associated with
                # reaching/sustaining the goal.
                StructField(
                    "priority",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Human-readable and/or coded description of a specific desired objective of
                # care, such as "control blood pressure" or "negotiate an obstacle course" or
                # "dance with child at wedding".
                StructField(
                    "description",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identifies the patient, group or organization for whom the goal is being
                # established.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The date or event after which the goal should begin being pursued.
                StructField("startDate", StringType(), True),
                # The date or event after which the goal should begin being pursued.
                StructField(
                    "startCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates what should be done by when.
                StructField(
                    "target",
                    ArrayType(Goal_Target.get_schema(recursion_depth + 1)),
                    True
                ),
                # Identifies when the current status.  I.e. When initially created, when
                # achieved, when cancelled, etc.
                StructField("statusDate", DateType(), True),
                # Captures the reason for the current status.
                StructField("statusReason", StringType(), True),
                # Indicates whose goal this is - patient goal, practitioner goal, etc.
                StructField(
                    "expressedBy", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The identified conditions and other health record elements that are intended
                # to be addressed by the goal.
                StructField(
                    "addresses",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Any comments related to the goal.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the change (or lack of change) at the point when the status of the
                # goal is assessed.
                StructField(
                    "outcomeCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Details of what's changed (or not changed).
                StructField(
                    "outcomeReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
