from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ProvenanceSchema:
    """
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that resource.
    Provenance provides a critical foundation for assessing authenticity, enabling
    trust, and allowing reproducibility. Provenance assertions are a form of
    contextual metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in terms of
    confidence in authenticity, reliability, and trustworthiness, integrity, and
    stage in lifecycle (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust policies.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Provenance of a resource is a record that describes entities and processes
        involved in producing and delivering or otherwise influencing that resource.
        Provenance provides a critical foundation for assessing authenticity, enabling
        trust, and allowing reproducibility. Provenance assertions are a form of
        contextual metadata and can themselves become important records with their own
        provenance. Provenance statement indicates clinical significance in terms of
        confidence in authenticity, reliability, and trustworthiness, integrity, and
        stage in lifecycle (e.g. Document Completion - has the artifact been legally
        authenticated), all of which may impact security, privacy, and trust policies.


        resourceType: This is a Provenance resource

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

        target: The Reference(s) that were generated or updated by  the activity described in
            this resource. A provenance can point to more than one target if multiple
            resources were created/updated by the same activity.

        occurredPeriod: The period during which the activity occurred.

        occurredDateTime: The period during which the activity occurred.

        recorded: The instant of time at which the activity was recorded.

        policy: Policy or plan the activity was defined by. Typically, a single activity may
            have multiple applicable policy documents, such as patient consent, guarantor
            funding, etc.

        location: Where the activity occurred, if relevant.

        reason: The reason that the activity was taking place.

        activity: An activity is something that occurs over a period of time and acts upon or
            with entities; it may include consuming, processing, transforming, modifying,
            relocating, using, or generating entities.

        agent: An actor taking a role in an activity  for which it can be assigned some
            degree of responsibility for the activity taking place.

        entity: An entity used in this activity.

        signature: A digital signature on the target Reference(s). The signer should match a
            Provenance.agent. The purpose of the signature is indicated.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.simple_types.instant import instantSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.provenance_agent import Provenance_AgentSchema
        from spark_fhir_schemas.r4.complex_types.provenance_entity import Provenance_EntitySchema
        from spark_fhir_schemas.r4.complex_types.signature import SignatureSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Provenance resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id", idSchema.get_schema(recursion_depth + 1), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", MetaSchema.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uriSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", codeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", NarrativeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The Reference(s) that were generated or updated by  the activity described in
                # this resource. A provenance can point to more than one target if multiple
                # resources were created/updated by the same activity.
                StructField(
                    "target",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # The period during which the activity occurred.
                StructField(
                    "occurredPeriod",
                    PeriodSchema.get_schema(recursion_depth + 1), True
                ),
                # The period during which the activity occurred.
                StructField("occurredDateTime", StringType(), True),
                # The instant of time at which the activity was recorded.
                StructField(
                    "recorded", instantSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # Policy or plan the activity was defined by. Typically, a single activity may
                # have multiple applicable policy documents, such as patient consent, guarantor
                # funding, etc.
                StructField(
                    "policy",
                    ArrayType(uriSchema.get_schema(recursion_depth + 1)), True
                ),
                # Where the activity occurred, if relevant.
                StructField(
                    "location",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # The reason that the activity was taking place.
                StructField(
                    "reason",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An activity is something that occurs over a period of time and acts upon or
                # with entities; it may include consuming, processing, transforming, modifying,
                # relocating, using, or generating entities.
                StructField(
                    "activity",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # An actor taking a role in an activity  for which it can be assigned some
                # degree of responsibility for the activity taking place.
                StructField(
                    "agent",
                    ArrayType(
                        Provenance_AgentSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An entity used in this activity.
                StructField(
                    "entity",
                    ArrayType(
                        Provenance_EntitySchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A digital signature on the target Reference(s). The signer should match a
                # Provenance.agent. The purpose of the signature is indicated.
                StructField(
                    "signature",
                    ArrayType(SignatureSchema.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
