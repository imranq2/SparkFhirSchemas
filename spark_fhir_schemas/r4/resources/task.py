from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Task:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A task to be performed.


        resourceType: This is a Task resource

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

        identifier: The business identifier for this task.

        instantiatesCanonical: The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this Task.

        instantiatesUri: The URL pointing to an *externally* maintained  protocol, guideline, orderset
            or other definition that is adhered to in whole or in part by this Task.

        basedOn: BasedOn refers to a higher-level authorization that triggered the creation of
            the task.  It references a "request" resource such as a ServiceRequest,
            MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the
            "request" resource the task is seeking to fulfill.  This latter resource is
            referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a
            task is created to fulfill a procedureRequest ( = FocusOn ) to collect a
            specimen from a patient.

        groupIdentifier: An identifier that links together multiple tasks and other requests that were
            created in the same context.

        partOf: Task that this particular task is part of.

        status: The current status of the task.

        statusReason: An explanation as to why this task is held, failed, was refused, etc.

        businessStatus: Contains business-specific nuances of the business state.

        intent: Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs
            this a proposed task, a planned task, an actionable task, etc.

        priority: Indicates how quickly the Task should be addressed with respect to other
            requests.

        code: A name or code (or both) briefly describing what the task involves.

        description: A free-text description of what is to be performed.

        focus: The request being actioned or the resource being manipulated by this task.

        for: The entity who benefits from the performance of the service specified in the
            task (e.g., the patient).

        encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
            during which this task was created.

        executionPeriod: Identifies the time action was first taken against the task (start) and/or the
            time final action was taken against the task prior to marking it as completed
            (end).

        authoredOn: The date and time this task was created.

        lastModified: The date and time of last modification to this task.

        requester: The creator of the task.

        performerType: The kind of participant that should perform the task.

        owner: Individual organization or Device currently responsible for task execution.

        location: Principal physical location where the this task is performed.

        reasonCode: A description or code indicating why this task needs to be performed.

        reasonReference: A resource reference indicating why this task needs to be performed.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be relevant to the Task.

        note: Free-text information captured about the task as it progresses.

        relevantHistory: Links to Provenance records for past versions of this Task that identify key
            state transitions or updates that are likely to be relevant to a user looking
            at the current version of the task.

        restriction: If the Task.focus is a request resource and the task is seeking fulfillment
            (i.e. is asking for the request to be actioned), this element identifies any
            limitations on what parts of the referenced request should be actioned.

        input: Additional information that may be needed in the execution of the task.

        output: Outputs produced by the Task.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.task_restriction import Task_Restriction
        from spark_fhir_schemas.r4.complex_types.task_input import Task_Input
        from spark_fhir_schemas.r4.complex_types.task_output import Task_Output
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Task resource
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
                # The business identifier for this task.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this Task.
                StructField(
                    "instantiatesCanonical",
                    canonical.get_schema(recursion_depth + 1), True
                ),
                # The URL pointing to an *externally* maintained  protocol, guideline, orderset
                # or other definition that is adhered to in whole or in part by this Task.
                StructField(
                    "instantiatesUri", uri.get_schema(recursion_depth + 1),
                    True
                ),
                # BasedOn refers to a higher-level authorization that triggered the creation of
                # the task.  It references a "request" resource such as a ServiceRequest,
                # MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the
                # "request" resource the task is seeking to fulfill.  This latter resource is
                # referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a
                # task is created to fulfill a procedureRequest ( = FocusOn ) to collect a
                # specimen from a patient.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # An identifier that links together multiple tasks and other requests that were
                # created in the same context.
                StructField(
                    "groupIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # Task that this particular task is part of.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The current status of the task.
                StructField("status", StringType(), True),
                # An explanation as to why this task is held, failed, was refused, etc.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Contains business-specific nuances of the business state.
                StructField(
                    "businessStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs
                # this a proposed task, a planned task, an actionable task, etc.
                StructField("intent", StringType(), True),
                # Indicates how quickly the Task should be addressed with respect to other
                # requests.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # A name or code (or both) briefly describing what the task involves.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A free-text description of what is to be performed.
                StructField("description", StringType(), True),
                # The request being actioned or the resource being manipulated by this task.
                StructField(
                    "focus", Reference.get_schema(recursion_depth + 1), True
                ),
                # The entity who benefits from the performance of the service specified in the
                # task (e.g., the patient).
                StructField(
                    "for", Reference.get_schema(recursion_depth + 1), True
                ),
                # The healthcare event  (e.g. a patient and healthcare provider interaction)
                # during which this task was created.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Identifies the time action was first taken against the task (start) and/or the
                # time final action was taken against the task prior to marking it as completed
                # (end).
                StructField(
                    "executionPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date and time this task was created.
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The date and time of last modification to this task.
                StructField(
                    "lastModified", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The creator of the task.
                StructField(
                    "requester", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The kind of participant that should perform the task.
                StructField(
                    "performerType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Individual organization or Device currently responsible for task execution.
                StructField(
                    "owner", Reference.get_schema(recursion_depth + 1), True
                ),
                # Principal physical location where the this task is performed.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # A description or code indicating why this task needs to be performed.
                StructField(
                    "reasonCode",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A resource reference indicating why this task needs to be performed.
                StructField(
                    "reasonReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be relevant to the Task.
                StructField(
                    "insurance",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Free-text information captured about the task as it progresses.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Links to Provenance records for past versions of this Task that identify key
                # state transitions or updates that are likely to be relevant to a user looking
                # at the current version of the task.
                StructField(
                    "relevantHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # If the Task.focus is a request resource and the task is seeking fulfillment
                # (i.e. is asking for the request to be actioned), this element identifies any
                # limitations on what parts of the referenced request should be actioned.
                StructField(
                    "restriction",
                    Task_Restriction.get_schema(recursion_depth + 1), True
                ),
                # Additional information that may be needed in the execution of the task.
                StructField(
                    "input",
                    ArrayType(Task_Input.get_schema(recursion_depth + 1)), True
                ),
                # Outputs produced by the Task.
                StructField(
                    "output",
                    ArrayType(Task_Output.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
