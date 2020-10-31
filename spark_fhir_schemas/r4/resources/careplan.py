from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CarePlan:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes the intention of how one or more practitioners intend to deliver
        care for a particular patient, group or community for a period of time,
        possibly limited to care for a specific condition or set of conditions.


        resourceType: This is a CarePlan resource

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

        identifier: Business identifiers assigned to this care plan by the performer or other
            systems which remain constant as the resource is updated and propagates from
            server to server.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other
            definition that is adhered to in whole or in part by this CarePlan.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline,
            questionnaire or other definition that is adhered to in whole or in part by
            this CarePlan.

        basedOn: A care plan that is fulfilled in whole or in part by this care plan.

        replaces: Completed or terminated care plan whose function is taken by this new care
            plan.

        partOf: A larger care plan of which this particular care plan is a component or step.

        status: Indicates whether the plan is currently being acted upon, represents future
            intentions or is now a historical record.

        intent: Indicates the level of authority/intentionality associated with the care plan
            and where the care plan fits into the workflow chain.

        category: Identifies what "kind" of plan this is to support differentiation between
            multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma",
            "disease management", "wellness plan", etc.

        title: Human-friendly name for the care plan.

        description: A description of the scope and nature of the plan.

        subject: Identifies the patient or group whose intended care is described by the plan.

        encounter: The Encounter during which this CarePlan was created or to which the creation
            of this record is tightly associated.

        period: Indicates when the plan did (or is intended to) come into effect and end.

        created: Represents when this particular CarePlan record was created in the system,
            which is often a system-generated date.

        author: When populated, the author is responsible for the care plan.  The care plan is
            attributed to the author.

        contributor: Identifies the individual(s) or organization who provided the contents of the
            care plan.

        careTeam: Identifies all people and organizations who are expected to be involved in the
            care envisioned by this plan.

        addresses: Identifies the conditions/problems/concerns/diagnoses/etc. whose management
            and/or mitigation are handled by this plan.

        supportingInfo: Identifies portions of the patient's record that specifically influenced the
            formation of the plan.  These might include comorbidities, recent procedures,
            limitations, recent assessments, etc.

        goal: Describes the intended objective(s) of carrying out the care plan.

        activity: Identifies a planned action to occur as part of the plan.  For example, a
            medication to be used, lab tests to perform, self-monitoring, education, etc.

        note: General notes about the care plan not covered elsewhere.

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
        from spark_fhir_schemas.r4.complex_types.careplan_activity import CarePlan_Activity
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a CarePlan resource
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
                # Business identifiers assigned to this care plan by the performer or other
                # systems which remain constant as the resource is updated and propagates from
                # server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other
                # definition that is adhered to in whole or in part by this CarePlan.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline,
                # questionnaire or other definition that is adhered to in whole or in part by
                # this CarePlan.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # A care plan that is fulfilled in whole or in part by this care plan.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Completed or terminated care plan whose function is taken by this new care
                # plan.
                StructField(
                    "replaces",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A larger care plan of which this particular care plan is a component or step.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Indicates whether the plan is currently being acted upon, represents future
                # intentions or is now a historical record.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates the level of authority/intentionality associated with the care plan
                # and where the care plan fits into the workflow chain.
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                # Identifies what "kind" of plan this is to support differentiation between
                # multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma",
                # "disease management", "wellness plan", etc.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Human-friendly name for the care plan.
                StructField("title", StringType(), True),
                # A description of the scope and nature of the plan.
                StructField("description", StringType(), True),
                # Identifies the patient or group whose intended care is described by the plan.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Encounter during which this CarePlan was created or to which the creation
                # of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates when the plan did (or is intended to) come into effect and end.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # Represents when this particular CarePlan record was created in the system,
                # which is often a system-generated date.
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                # When populated, the author is responsible for the care plan.  The care plan is
                # attributed to the author.
                StructField(
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies the individual(s) or organization who provided the contents of the
                # care plan.
                StructField(
                    "contributor",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies all people and organizations who are expected to be involved in the
                # care envisioned by this plan.
                StructField(
                    "careTeam",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the conditions/problems/concerns/diagnoses/etc. whose management
                # and/or mitigation are handled by this plan.
                StructField(
                    "addresses",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies portions of the patient's record that specifically influenced the
                # formation of the plan.  These might include comorbidities, recent procedures,
                # limitations, recent assessments, etc.
                StructField(
                    "supportingInfo",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Describes the intended objective(s) of carrying out the care plan.
                StructField(
                    "goal",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies a planned action to occur as part of the plan.  For example, a
                # medication to be used, lab tests to perform, self-monitoring, education, etc.
                StructField(
                    "activity",
                    ArrayType(
                        CarePlan_Activity.get_schema(recursion_depth + 1)
                    ), True
                ),
                # General notes about the care plan not covered elsewhere.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
