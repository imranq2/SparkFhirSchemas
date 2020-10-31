from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ActivityDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource allows for the definition of some activity to be performed,
        independent of a particular patient, practitioner, or other performance
        context.


        resourceType: This is a ActivityDefinition resource

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

        url: An absolute URI that is used to identify this activity definition when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this activity
            definition is (or will be) published. This URL can be the target of a
            canonical reference. It SHALL remain the same when the activity definition is
            stored on different servers.

        identifier: A formal identifier that is used to identify this activity definition when it
            is represented in other formats, or referenced in a specification, model,
            design or an instance.

        version: The identifier that is used to identify this version of the activity
            definition when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the activity definition author
            and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
            no expectation that versions can be placed in a lexicographical sequence. To
            provide a version consistent with the Decision Support Service specification,
            use the format Major.Minor.Revision (e.g. 1.0.0). For more information on
            versioning knowledge assets, refer to the Decision Support Service
            specification. Note that a version is required for non-experimental active
            assets.

        name: A natural language name identifying the activity definition. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the activity definition.

        subtitle: An explanatory or alternate title for the activity definition giving
            additional information about its content.

        status: The status of this activity definition. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this activity definition is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        subjectCodeableConcept: A code or group definition that describes the intended subject of the activity
            being defined.

        subjectReference: A code or group definition that describes the intended subject of the activity
            being defined.

        date: The date  (and optionally time) when the activity definition was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the activity definition changes.

        publisher: The name of the organization or individual that published the activity
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the activity definition from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate activity
            definition instances.

        jurisdiction: A legal or geographic region in which the activity definition is intended to
            be used.

        purpose: Explanation of why this activity definition is needed and why it has been
            designed as it has.

        usage: A detailed description of how the activity definition is used from a clinical
            perspective.

        copyright: A copyright statement relating to the activity definition and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the activity definition.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the activity definition content was or is planned to
            be in active use.

        topic: Descriptive topics related to the content of the activity. Topics provide a
            high-level categorization of the activity that can be useful for filtering and
            searching.

        author: An individiual or organization primarily involved in the creation and
            maintenance of the content.

        editor: An individual or organization primarily responsible for internal coherence of
            the content.

        reviewer: An individual or organization primarily responsible for review of some aspect
            of the content.

        endorser: An individual or organization responsible for officially endorsing the content
            for use in some setting.

        relatedArtifact: Related artifacts such as additional documentation, justification, or
            bibliographic references.

        library: A reference to a Library resource containing any formal logic used by the
            activity definition.

        kind: A description of the kind of resource the activity definition is representing.
            For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest.
            Typically, but not always, this is a Request resource.

        profile: A profile to which the target of the activity definition is expected to
            conform.

        code: Detailed description of the type of activity; e.g. What lab test, what
            procedure, what kind of encounter.

        intent: Indicates the level of authority/intentionality associated with the activity
            and where the request should fit into the workflow chain.

        priority: Indicates how quickly the activity  should be addressed with respect to other
            requests.

        doNotPerform: Set this to true if the definition is to indicate that a particular activity
            should NOT be performed. If true, this element should be interpreted to
            reinforce a negative coding. For example NPO as a code with a doNotPerform of
            true would still indicate to NOT perform the action.

        timingTiming: The period, timing or frequency upon which the described activity is to occur.

        timingDateTime: The period, timing or frequency upon which the described activity is to occur.

        timingAge: The period, timing or frequency upon which the described activity is to occur.

        timingPeriod: The period, timing or frequency upon which the described activity is to occur.

        timingRange: The period, timing or frequency upon which the described activity is to occur.

        timingDuration: The period, timing or frequency upon which the described activity is to occur.

        location: Identifies the facility where the activity will occur; e.g. home, hospital,
            specific clinic, etc.

        participant: Indicates who should participate in performing the action described.

        productReference: Identifies the food, drug or other product being consumed or supplied in the
            activity.

        productCodeableConcept: Identifies the food, drug or other product being consumed or supplied in the
            activity.

        quantity: Identifies the quantity expected to be consumed at once (per dose, per meal,
            etc.).

        dosage: Provides detailed dosage instructions in the same way that they are described
            for MedicationRequest resources.

        bodySite: Indicates the sites on the subject's body where the procedure should be
            performed (I.e. the target sites).

        specimenRequirement: Defines specimen requirements for the action to be performed, such as required
            specimens for a lab test.

        observationRequirement: Defines observation requirements for the action to be performed, such as body
            weight or surface area.

        observationResultRequirement: Defines the observations that are expected to be produced by the action.

        transform: A reference to a StructureMap resource that defines a transform that can be
            executed to produce the intent resource using the ActivityDefinition instance
            as the input.

        dynamicValue: Dynamic values that will be evaluated to produce values for elements of the
            resulting resource. For example, if the dosage of a medication must be
            computed based on the patient's weight, a dynamic value would be used to
            specify an expression that calculated the weight, and the path on the request
            resource that would contain the result.

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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.activitydefinition_participant import ActivityDefinition_Participant
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.dosage import Dosage
        from spark_fhir_schemas.r4.complex_types.activitydefinition_dynamicvalue import ActivityDefinition_DynamicValue
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ActivityDefinition resource
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
                # An absolute URI that is used to identify this activity definition when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this activity
                # definition is (or will be) published. This URL can be the target of a
                # canonical reference. It SHALL remain the same when the activity definition is
                # stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # A formal identifier that is used to identify this activity definition when it
                # is represented in other formats, or referenced in a specification, model,
                # design or an instance.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The identifier that is used to identify this version of the activity
                # definition when it is referenced in a specification, model, design or
                # instance. This is an arbitrary value managed by the activity definition author
                # and is not expected to be globally unique. For example, it might be a
                # timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
                # no expectation that versions can be placed in a lexicographical sequence. To
                # provide a version consistent with the Decision Support Service specification,
                # use the format Major.Minor.Revision (e.g. 1.0.0). For more information on
                # versioning knowledge assets, refer to the Decision Support Service
                # specification. Note that a version is required for non-experimental active
                # assets.
                StructField("version", StringType(), True),
                # A natural language name identifying the activity definition. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the activity definition.
                StructField("title", StringType(), True),
                # An explanatory or alternate title for the activity definition giving
                # additional information about its content.
                StructField("subtitle", StringType(), True),
                # The status of this activity definition. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this activity definition is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # A code or group definition that describes the intended subject of the activity
                # being defined.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A code or group definition that describes the intended subject of the activity
                # being defined.
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The date  (and optionally time) when the activity definition was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the activity definition changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the activity
                # definition.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the activity definition from a
                # consumer's perspective.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate activity
                # definition instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the activity definition is intended to
                # be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Explanation of why this activity definition is needed and why it has been
                # designed as it has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # A detailed description of how the activity definition is used from a clinical
                # perspective.
                StructField("usage", StringType(), True),
                # A copyright statement relating to the activity definition and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the activity definition.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", DateType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval but does not change the original approval date.
                StructField("lastReviewDate", DateType(), True),
                # The period during which the activity definition content was or is planned to
                # be in active use.
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Descriptive topics related to the content of the activity. Topics provide a
                # high-level categorization of the activity that can be useful for filtering and
                # searching.
                StructField(
                    "topic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individiual or organization primarily involved in the creation and
                # maintenance of the content.
                StructField(
                    "author",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individual or organization primarily responsible for internal coherence of
                # the content.
                StructField(
                    "editor",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individual or organization primarily responsible for review of some aspect
                # of the content.
                StructField(
                    "reviewer",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # An individual or organization responsible for officially endorsing the content
                # for use in some setting.
                StructField(
                    "endorser",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # Related artifacts such as additional documentation, justification, or
                # bibliographic references.
                StructField(
                    "relatedArtifact",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                # A reference to a Library resource containing any formal logic used by the
                # activity definition.
                StructField(
                    "library",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # A description of the kind of resource the activity definition is representing.
                # For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest.
                # Typically, but not always, this is a Request resource.
                StructField(
                    "kind", code.get_schema(recursion_depth + 1), True
                ),
                # A profile to which the target of the activity definition is expected to
                # conform.
                StructField(
                    "profile", canonical.get_schema(recursion_depth + 1), True
                ),
                # Detailed description of the type of activity; e.g. What lab test, what
                # procedure, what kind of encounter.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the level of authority/intentionality associated with the activity
                # and where the request should fit into the workflow chain.
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates how quickly the activity  should be addressed with respect to other
                # requests.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # Set this to true if the definition is to indicate that a particular activity
                # should NOT be performed. If true, this element should be interpreted to
                # reinforce a negative coding. For example NPO as a code with a doNotPerform of
                # true would still indicate to NOT perform the action.
                StructField("doNotPerform", BooleanType(), True),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField("timingDateTime", StringType(), True),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingAge", Age.get_schema(recursion_depth + 1), True
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingRange", Range.get_schema(recursion_depth + 1), True
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # Identifies the facility where the activity will occur; e.g. home, hospital,
                # specific clinic, etc.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # Indicates who should participate in performing the action described.
                StructField(
                    "participant",
                    ArrayType(
                        ActivityDefinition_Participant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies the food, drug or other product being consumed or supplied in the
                # activity.
                StructField(
                    "productReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies the food, drug or other product being consumed or supplied in the
                # activity.
                StructField(
                    "productCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identifies the quantity expected to be consumed at once (per dose, per meal,
                # etc.).
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Provides detailed dosage instructions in the same way that they are described
                # for MedicationRequest resources.
                StructField(
                    "dosage",
                    ArrayType(Dosage.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the sites on the subject's body where the procedure should be
                # performed (I.e. the target sites).
                StructField(
                    "bodySite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Defines specimen requirements for the action to be performed, such as required
                # specimens for a lab test.
                StructField(
                    "specimenRequirement",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Defines observation requirements for the action to be performed, such as body
                # weight or surface area.
                StructField(
                    "observationRequirement",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Defines the observations that are expected to be produced by the action.
                StructField(
                    "observationResultRequirement",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A reference to a StructureMap resource that defines a transform that can be
                # executed to produce the intent resource using the ActivityDefinition instance
                # as the input.
                StructField(
                    "transform", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                # Dynamic values that will be evaluated to produce values for elements of the
                # resulting resource. For example, if the dosage of a medication must be
                # computed based on the patient's weight, a dynamic value would be used to
                # specify an expression that calculated the weight, and the path on the request
                # resource that would contain the result.
                StructField(
                    "dynamicValue",
                    ArrayType(
                        ActivityDefinition_DynamicValue.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
