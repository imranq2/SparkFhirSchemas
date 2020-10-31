from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CoverageSchema:
    """
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Financial instrument which may be used to reimburse or pay for health care
        products and services. Includes both insurance and self-payment.


        resourceType: This is a Coverage resource

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

        identifier: A unique identifier assigned to this coverage.

        status: The status of the resource instance.

        type: The type of coverage: social program, medical plan, accident coverage (workers
            compensation, auto), group health or payment by an individual or organization.

        policyHolder: The party who 'owns' the insurance policy.

        subscriber: The party who has signed-up for or 'owns' the contractual relationship to the
            policy or to whom the benefit of the policy for services rendered to them or
            their family is due.

        subscriberId: The insurer assigned ID for the Subscriber.

        beneficiary: The party who benefits from the insurance coverage; the patient when products
            and/or services are provided.

        dependent: A unique identifier for a dependent under the coverage.

        relationship: The relationship of beneficiary (patient) to the subscriber.

        period: Time period during which the coverage is in force. A missing start date
            indicates the start date isn't known, a missing end date means the coverage is
            continuing to be in force.

        payor: The program or plan underwriter or payor including both insurance and non-
            insurance agreements, such as patient-pay agreements.

        class: A suite of underwriter specific classifiers.

        order: The order of applicability of this coverage relative to other coverages which
            are currently in force. Note, there may be gaps in the numbering and this does
            not imply primary, secondary etc. as the specific positioning of coverages
            depends upon the episode of care.

        network: The insurer-specific identifier for the insurer-defined network of providers
            to which the beneficiary may seek treatment which will be covered at the 'in-
            network' rate, otherwise 'out of network' terms and conditions apply.

        costToBeneficiary: A suite of codes indicating the cost category and associated amount which have
            been detailed in the policy and may have been  included on the health card.

        subrogation: When 'subrogation=true' this insurance instance has been included not for
            adjudication but to provide insurers with the details to recover costs.

        contract: The policy(s) which constitute this insurance coverage.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.coverage_class import Coverage_ClassSchema
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveIntSchema
        from spark_fhir_schemas.r4.complex_types.coverage_costtobeneficiary import Coverage_CostToBeneficiarySchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                # This is a Coverage resource
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
                # A unique identifier assigned to this coverage.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The status of the resource instance.
                StructField(
                    "status", codeSchema.get_schema(recursion_depth + 1), True
                ),
                # The type of coverage: social program, medical plan, accident coverage (workers
                # compensation, auto), group health or payment by an individual or organization.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The party who 'owns' the insurance policy.
                StructField(
                    "policyHolder",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # The party who has signed-up for or 'owns' the contractual relationship to the
                # policy or to whom the benefit of the policy for services rendered to them or
                # their family is due.
                StructField(
                    "subscriber",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # The insurer assigned ID for the Subscriber.
                StructField("subscriberId", StringType(), True),
                # The party who benefits from the insurance coverage; the patient when products
                # and/or services are provided.
                StructField(
                    "beneficiary",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # A unique identifier for a dependent under the coverage.
                StructField("dependent", StringType(), True),
                # The relationship of beneficiary (patient) to the subscriber.
                StructField(
                    "relationship",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Time period during which the coverage is in force. A missing start date
                # indicates the start date isn't known, a missing end date means the coverage is
                # continuing to be in force.
                StructField(
                    "period", PeriodSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The program or plan underwriter or payor including both insurance and non-
                # insurance agreements, such as patient-pay agreements.
                StructField(
                    "payor",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # A suite of underwriter specific classifiers.
                StructField(
                    "class",
                    ArrayType(
                        Coverage_ClassSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The order of applicability of this coverage relative to other coverages which
                # are currently in force. Note, there may be gaps in the numbering and this does
                # not imply primary, secondary etc. as the specific positioning of coverages
                # depends upon the episode of care.
                StructField(
                    "order", positiveIntSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The insurer-specific identifier for the insurer-defined network of providers
                # to which the beneficiary may seek treatment which will be covered at the 'in-
                # network' rate, otherwise 'out of network' terms and conditions apply.
                StructField("network", StringType(), True),
                # A suite of codes indicating the cost category and associated amount which have
                # been detailed in the policy and may have been  included on the health card.
                StructField(
                    "costToBeneficiary",
                    ArrayType(
                        Coverage_CostToBeneficiarySchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # When 'subrogation=true' this insurance instance has been included not for
                # adjudication but to provide insurers with the details to recover costs.
                StructField("subrogation", BooleanType(), True),
                # The policy(s) which constitute this insurance coverage.
                StructField(
                    "contract",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
