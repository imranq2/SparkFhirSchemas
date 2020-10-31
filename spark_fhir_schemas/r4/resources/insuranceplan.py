from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class InsurancePlan:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Details of a Health Insurance product/plan provided by an organization.


        resourceType: This is a InsurancePlan resource

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

        identifier: Business identifiers assigned to this health insurance product which remain
            constant as the resource is updated and propagates from server to server.

        status: The current state of the health insurance product.

        type: The kind of health insurance product.

        name: Official name of the health insurance product as designated by the owner.

        alias: A list of alternate names that the product is known as, or was known as in the
            past.

        period: The period of time that the health insurance product is available.

        ownedBy: The entity that is providing  the health insurance product and underwriting
            the risk.  This is typically an insurance carriers, other third-party payers,
            or health plan sponsors comonly referred to as 'payers'.

        administeredBy: An organization which administer other services such as underwriting, customer
            service and/or claims processing on behalf of the health insurance product
            owner.

        coverageArea: The geographic region in which a health insurance product's benefits apply.

        contact: The contact for the health insurance product for a certain purpose.

        endpoint: The technical endpoints providing access to services operated for the health
            insurance product.

        network: Reference to the network included in the health insurance product.

        coverage: Details about the coverage offered by the insurance product.

        plan: Details about an insurance plan.

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
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.insuranceplan_contact import InsurancePlan_Contact
        from spark_fhir_schemas.r4.complex_types.insuranceplan_coverage import InsurancePlan_Coverage
        from spark_fhir_schemas.r4.complex_types.insuranceplan_plan import InsurancePlan_Plan
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a InsurancePlan resource
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
                # Business identifiers assigned to this health insurance product which remain
                # constant as the resource is updated and propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The current state of the health insurance product.
                StructField("status", StringType(), True),
                # The kind of health insurance product.
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Official name of the health insurance product as designated by the owner.
                StructField("name", StringType(), True),
                # A list of alternate names that the product is known as, or was known as in the
                # past.
                StructField("alias", ArrayType(StringType()), True),
                # The period of time that the health insurance product is available.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # The entity that is providing  the health insurance product and underwriting
                # the risk.  This is typically an insurance carriers, other third-party payers,
                # or health plan sponsors comonly referred to as 'payers'.
                StructField(
                    "ownedBy", Reference.get_schema(recursion_depth + 1), True
                ),
                # An organization which administer other services such as underwriting, customer
                # service and/or claims processing on behalf of the health insurance product
                # owner.
                StructField(
                    "administeredBy",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The geographic region in which a health insurance product's benefits apply.
                StructField(
                    "coverageArea",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The contact for the health insurance product for a certain purpose.
                StructField(
                    "contact",
                    ArrayType(
                        InsurancePlan_Contact.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The technical endpoints providing access to services operated for the health
                # insurance product.
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Reference to the network included in the health insurance product.
                StructField(
                    "network",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Details about the coverage offered by the insurance product.
                StructField(
                    "coverage",
                    ArrayType(
                        InsurancePlan_Coverage.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Details about an insurance plan.
                StructField(
                    "plan",
                    ArrayType(
                        InsurancePlan_Plan.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
