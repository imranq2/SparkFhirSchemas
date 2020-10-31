from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ClaimResponseSchema:
    """
    This resource provides the adjudication details from the processing of a Claim
    resource.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource provides the adjudication details from the processing of a Claim
        resource.


        resourceType: This is a ClaimResponse resource

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

        identifier: A unique identifier assigned to this claim response.

        status: The status of the resource instance.

        type: A finer grained suite of claim type codes which may convey additional
            information such as Inpatient vs Outpatient and/or a specialty service.

        subType: A finer grained suite of claim type codes which may convey additional
            information such as Inpatient vs Outpatient and/or a specialty service.

        use: A code to indicate whether the nature of the request is: to request
            adjudication of products and services previously rendered; or requesting
            authorization and adjudication for provision in the future; or requesting the
            non-binding adjudication of the listed products and services which could be
            provided in the future.

        patient: The party to whom the professional services and/or products have been supplied
            or are being considered and for whom actual for facast reimbursement is
            sought.

        created: The date this resource was created.

        insurer: The party responsible for authorization, adjudication and reimbursement.

        requestor: The provider which is responsible for the claim, predetermination or
            preauthorization.

        request: Original request resource reference.

        outcome: The outcome of the claim, predetermination, or preauthorization processing.

        disposition: A human readable description of the status of the adjudication.

        preAuthRef: Reference from the Insurer which is used in later communications which refers
            to this adjudication.

        preAuthPeriod: The time frame during which this authorization is effective.

        payeeType: Type of Party to be reimbursed: subscriber, provider, other.

        item: A claim line. Either a simple (a product or service) or a 'group' of details
            which can also be a simple items or groups of sub-details.

        addItem: The first-tier service adjudications for payor added product or service lines.

        adjudication: The adjudication results which are presented at the header level rather than
            at the line-item or add-item levels.

        total: Categorized monetary totals for the adjudication.

        payment: Payment details for the adjudication of the claim.

        fundsReserve: A code, used only on a response to a preauthorization, to indicate whether the
            benefits payable have been reserved and for whom.

        formCode: A code for the form to be used for printing the content.

        form: The actual form, by reference or inclusion, for printing the content or an
            EOB.

        processNote: A note that describes or explains adjudication results in a human readable
            form.

        communicationRequest: Request for additional supporting or authorizing information.

        insurance: Financial instruments for reimbursement for the health care products and
            services specified on the claim.

        error: Errors encountered during the processing of the adjudication.

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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_item import ClaimResponse_ItemSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_additem import ClaimResponse_AddItemSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_AdjudicationSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_total import ClaimResponse_TotalSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_payment import ClaimResponse_PaymentSchema
        from spark_fhir_schemas.r4.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_processnote import ClaimResponse_ProcessNoteSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_insurance import ClaimResponse_InsuranceSchema
        from spark_fhir_schemas.r4.complex_types.claimresponse_error import ClaimResponse_ErrorSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ClaimResponse resource
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
                # A unique identifier assigned to this claim response.
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
                # A finer grained suite of claim type codes which may convey additional
                # information such as Inpatient vs Outpatient and/or a specialty service.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # A finer grained suite of claim type codes which may convey additional
                # information such as Inpatient vs Outpatient and/or a specialty service.
                StructField(
                    "subType",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # A code to indicate whether the nature of the request is: to request
                # adjudication of products and services previously rendered; or requesting
                # authorization and adjudication for provision in the future; or requesting the
                # non-binding adjudication of the listed products and services which could be
                # provided in the future.
                StructField(
                    "use", codeSchema.get_schema(recursion_depth + 1), True
                ),
                # The party to whom the professional services and/or products have been supplied
                # or are being considered and for whom actual for facast reimbursement is
                # sought.
                StructField(
                    "patient", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The date this resource was created.
                StructField(
                    "created", dateTimeSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The party responsible for authorization, adjudication and reimbursement.
                StructField(
                    "insurer", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The provider which is responsible for the claim, predetermination or
                # preauthorization.
                StructField(
                    "requestor",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # Original request resource reference.
                StructField(
                    "request", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The outcome of the claim, predetermination, or preauthorization processing.
                StructField(
                    "outcome", codeSchema.get_schema(recursion_depth + 1), True
                ),
                # A human readable description of the status of the adjudication.
                StructField("disposition", StringType(), True),
                # Reference from the Insurer which is used in later communications which refers
                # to this adjudication.
                StructField("preAuthRef", StringType(), True),
                # The time frame during which this authorization is effective.
                StructField(
                    "preAuthPeriod",
                    PeriodSchema.get_schema(recursion_depth + 1), True
                ),
                # Type of Party to be reimbursed: subscriber, provider, other.
                StructField(
                    "payeeType",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # A claim line. Either a simple (a product or service) or a 'group' of details
                # which can also be a simple items or groups of sub-details.
                StructField(
                    "item",
                    ArrayType(
                        ClaimResponse_ItemSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The first-tier service adjudications for payor added product or service lines.
                StructField(
                    "addItem",
                    ArrayType(
                        ClaimResponse_AddItemSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The adjudication results which are presented at the header level rather than
                # at the line-item or add-item levels.
                StructField(
                    "adjudication",
                    ArrayType(
                        ClaimResponse_AdjudicationSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Categorized monetary totals for the adjudication.
                StructField(
                    "total",
                    ArrayType(
                        ClaimResponse_TotalSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Payment details for the adjudication of the claim.
                StructField(
                    "payment",
                    ClaimResponse_PaymentSchema.
                    get_schema(recursion_depth + 1), True
                ),
                # A code, used only on a response to a preauthorization, to indicate whether the
                # benefits payable have been reserved and for whom.
                StructField(
                    "fundsReserve",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # A code for the form to be used for printing the content.
                StructField(
                    "formCode",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The actual form, by reference or inclusion, for printing the content or an
                # EOB.
                StructField(
                    "form", AttachmentSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A note that describes or explains adjudication results in a human readable
                # form.
                StructField(
                    "processNote",
                    ArrayType(
                        ClaimResponse_ProcessNoteSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Request for additional supporting or authorizing information.
                StructField(
                    "communicationRequest",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Financial instruments for reimbursement for the health care products and
                # services specified on the claim.
                StructField(
                    "insurance",
                    ArrayType(
                        ClaimResponse_InsuranceSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Errors encountered during the processing of the adjudication.
                StructField(
                    "error",
                    ArrayType(
                        ClaimResponse_ErrorSchema.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
