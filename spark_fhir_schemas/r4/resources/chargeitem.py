from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ChargeItem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The resource ChargeItem describes the provision of healthcare provider
        products for a certain patient, therefore referring not only to the product,
        but containing in addition details of the provision, like date, time, amounts
        and participating organizations and persons. Main Usage of the ChargeItem is
        to enable the billing process and internal cost allocation.


        resourceType: This is a ChargeItem resource

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

        identifier: Identifiers assigned to this event performer or other systems.

        definitionUri: References the (external) source of pricing information, rules of application
            for the code this ChargeItem uses.

        definitionCanonical: References the source of pricing information, rules of application for the
            code this ChargeItem uses.

        status: The current state of the ChargeItem.

        partOf: ChargeItems can be grouped to larger ChargeItems covering the whole set.

        code: A code that identifies the charge, like a billing code.

        subject: The individual or set of individuals the action is being or was performed on.

        context: The encounter or episode of care that establishes the context for this event.

        occurrenceDateTime: Date/time(s) or duration when the charged service was applied.

        occurrencePeriod: Date/time(s) or duration when the charged service was applied.

        occurrenceTiming: Date/time(s) or duration when the charged service was applied.

        performer: Indicates who or what performed or participated in the charged service.

        performingOrganization: The organization requesting the service.

        requestingOrganization: The organization performing the service.

        costCenter: The financial cost center permits the tracking of charge attribution.

        quantity: Quantity of which the charge item has been serviced.

        bodysite: The anatomical location where the related service has been applied.

        factorOverride: Factor overriding the factor determined by the rules associated with the code.

        priceOverride: Total price of the charge overriding the list price associated with the code.

        overrideReason: If the list price or the rule-based factor associated with the code is
            overridden, this attribute can capture a text to indicate the  reason for this
            action.

        enterer: The device, practitioner, etc. who entered the charge item.

        enteredDate: Date the charge item was entered.

        reason: Describes why the event occurred in coded or textual form.

        service: Indicated the rendered service that caused this charge.

        productReference: Identifies the device, food, drug or other product being charged either by
            type code or reference to an instance.

        productCodeableConcept: Identifies the device, food, drug or other product being charged either by
            type code or reference to an instance.

        account: Account into which this ChargeItems belongs.

        note: Comments made about the event by the performer, subject or other participants.

        supportingInformation: Further information supporting this charge.

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
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.chargeitem_performer import ChargeItem_Performer
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ChargeItem resource
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
                # Identifiers assigned to this event performer or other systems.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # References the (external) source of pricing information, rules of application
                # for the code this ChargeItem uses.
                StructField(
                    "definitionUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # References the source of pricing information, rules of application for the
                # code this ChargeItem uses.
                StructField(
                    "definitionCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The current state of the ChargeItem.
                StructField("status", StringType(), True),
                # ChargeItems can be grouped to larger ChargeItems covering the whole set.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A code that identifies the charge, like a billing code.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The individual or set of individuals the action is being or was performed on.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The encounter or episode of care that establishes the context for this event.
                StructField(
                    "context", Reference.get_schema(recursion_depth + 1), True
                ),
                # Date/time(s) or duration when the charged service was applied.
                StructField("occurrenceDateTime", StringType(), True),
                # Date/time(s) or duration when the charged service was applied.
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Date/time(s) or duration when the charged service was applied.
                StructField(
                    "occurrenceTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates who or what performed or participated in the charged service.
                StructField(
                    "performer",
                    ArrayType(
                        ChargeItem_Performer.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The organization requesting the service.
                StructField(
                    "performingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The organization performing the service.
                StructField(
                    "requestingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The financial cost center permits the tracking of charge attribution.
                StructField(
                    "costCenter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Quantity of which the charge item has been serviced.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # The anatomical location where the related service has been applied.
                StructField(
                    "bodysite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Factor overriding the factor determined by the rules associated with the code.
                StructField(
                    "factorOverride", decimal.get_schema(recursion_depth + 1),
                    True
                ),
                # Total price of the charge overriding the list price associated with the code.
                StructField(
                    "priceOverride", Money.get_schema(recursion_depth + 1),
                    True
                ),
                # If the list price or the rule-based factor associated with the code is
                # overridden, this attribute can capture a text to indicate the  reason for this
                # action.
                StructField("overrideReason", StringType(), True),
                # The device, practitioner, etc. who entered the charge item.
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                # Date the charge item was entered.
                StructField(
                    "enteredDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Describes why the event occurred in coded or textual form.
                StructField(
                    "reason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicated the rendered service that caused this charge.
                StructField(
                    "service",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the device, food, drug or other product being charged either by
                # type code or reference to an instance.
                StructField(
                    "productReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies the device, food, drug or other product being charged either by
                # type code or reference to an instance.
                StructField(
                    "productCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Account into which this ChargeItems belongs.
                StructField(
                    "account",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Comments made about the event by the performer, subject or other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Further information supporting this charge.
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
