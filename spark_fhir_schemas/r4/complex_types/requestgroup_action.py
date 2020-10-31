from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class RequestGroup_ActionSchema:
    """
    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A group of related requests that can be used to capture intended activities
        that have inter-dependencies such as "give this medication after that one".


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

        prefix: A user-visible prefix for the action.

        title: The title of the action displayed to a user.

        description: A short description of the action used to provide a summary to display to the
            user.

        textEquivalent: A text equivalent of the action to be performed. This provides a human-
            interpretable description of the action when the definition is consumed by a
            system that might not be capable of interpreting it dynamically.

        priority: Indicates how quickly the action should be addressed with respect to other
            actions.

        code: A code that provides meaning for the action or action group. For example, a
            section may have a LOINC code for a section of a documentation template.

        documentation: Didactic or other informational resources associated with the action that can
            be provided to the CDS recipient. Information resources can include inline
            text commentary and links to web resources.

        condition: An expression that describes applicability criteria, or start/stop conditions
            for the action.

        relatedAction: A relationship to another action such as "before" or "30-60 minutes after
            start of".

        timingDateTime: An optional value describing when the action should be performed.

        timingAge: An optional value describing when the action should be performed.

        timingPeriod: An optional value describing when the action should be performed.

        timingDuration: An optional value describing when the action should be performed.

        timingRange: An optional value describing when the action should be performed.

        timingTiming: An optional value describing when the action should be performed.

        participant: The participant that should perform or be responsible for this action.

        type: The type of action to perform (create, update, remove).

        groupingBehavior: Defines the grouping behavior for the action and its children.

        selectionBehavior: Defines the selection behavior for the action and its children.

        requiredBehavior: Defines expectations around whether an action is required.

        precheckBehavior: Defines whether the action should usually be preselected.

        cardinalityBehavior: Defines whether the action can be selected multiple times.

        resource: The resource that is the target of the action (e.g. CommunicationRequest).

        action: Sub actions.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifactSchema
        from spark_fhir_schemas.r4.complex_types.requestgroup_condition import RequestGroup_ConditionSchema
        from spark_fhir_schemas.r4.complex_types.requestgroup_relatedaction import RequestGroup_RelatedActionSchema
        from spark_fhir_schemas.r4.complex_types.age import AgeSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.timing import TimingSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # A user-visible prefix for the action.
                StructField("prefix", StringType(), True),
                # The title of the action displayed to a user.
                StructField("title", StringType(), True),
                # A short description of the action used to provide a summary to display to the
                # user.
                StructField("description", StringType(), True),
                # A text equivalent of the action to be performed. This provides a human-
                # interpretable description of the action when the definition is consumed by a
                # system that might not be capable of interpreting it dynamically.
                StructField("textEquivalent", StringType(), True),
                # Indicates how quickly the action should be addressed with respect to other
                # actions.
                StructField(
                    "priority", codeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A code that provides meaning for the action or action group. For example, a
                # section may have a LOINC code for a section of a documentation template.
                StructField(
                    "code",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Didactic or other informational resources associated with the action that can
                # be provided to the CDS recipient. Information resources can include inline
                # text commentary and links to web resources.
                StructField(
                    "documentation",
                    ArrayType(
                        RelatedArtifactSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An expression that describes applicability criteria, or start/stop conditions
                # for the action.
                StructField(
                    "condition",
                    ArrayType(
                        RequestGroup_ConditionSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A relationship to another action such as "before" or "30-60 minutes after
                # start of".
                StructField(
                    "relatedAction",
                    ArrayType(
                        RequestGroup_RelatedActionSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # An optional value describing when the action should be performed.
                StructField("timingDateTime", StringType(), True),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingAge", AgeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingPeriod",
                    PeriodSchema.get_schema(recursion_depth + 1), True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingDuration",
                    DurationSchema.get_schema(recursion_depth + 1), True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingRange", RangeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingTiming",
                    TimingSchema.get_schema(recursion_depth + 1), True
                ),
                # The participant that should perform or be responsible for this action.
                StructField(
                    "participant",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The type of action to perform (create, update, remove).
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Defines the grouping behavior for the action and its children.
                StructField(
                    "groupingBehavior",
                    codeSchema.get_schema(recursion_depth + 1), True
                ),
                # Defines the selection behavior for the action and its children.
                StructField(
                    "selectionBehavior",
                    codeSchema.get_schema(recursion_depth + 1), True
                ),
                # Defines expectations around whether an action is required.
                StructField(
                    "requiredBehavior",
                    codeSchema.get_schema(recursion_depth + 1), True
                ),
                # Defines whether the action should usually be preselected.
                StructField(
                    "precheckBehavior",
                    codeSchema.get_schema(recursion_depth + 1), True
                ),
                # Defines whether the action can be selected multiple times.
                StructField(
                    "cardinalityBehavior",
                    codeSchema.get_schema(recursion_depth + 1), True
                ),
                # The resource that is the target of the action (e.g. CommunicationRequest).
                StructField(
                    "resource",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # Sub actions.
                StructField(
                    "action",
                    ArrayType(
                        RequestGroup_ActionSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
