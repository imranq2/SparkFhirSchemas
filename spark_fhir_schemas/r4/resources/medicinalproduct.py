from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicinalProduct:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Detailed definition of a medicinal product, typically for uses other than
        direct patient care (e.g. regulatory use).


        resourceType: This is a MedicinalProduct resource

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

        identifier: Business identifier for this product. Could be an MPID.

        type: Regulatory type, e.g. Investigational or Authorized.

        domain: If this medicine applies to human or veterinary uses.

        combinedPharmaceuticalDoseForm: The dose form for a single part product, or combined form of a multiple part
            product.

        legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the
            regulator.

        additionalMonitoringIndicator: Whether the Medicinal Product is subject to additional monitoring for
            regulatory reasons.

        specialMeasures: Whether the Medicinal Product is subject to special measures for regulatory
            reasons.

        paediatricUseIndicator: If authorised for use in children.

        productClassification: Allows the product to be classified by various systems.

        marketingStatus: Marketing status of the medicinal product, in contrast to marketing
            authorizaton.

        pharmaceuticalProduct: Pharmaceutical aspects of product.

        packagedMedicinalProduct: Package representation for the product.

        attachedDocument: Supporting documentation, typically for regulatory submission.

        masterFile: A master file for to the medicinal product (e.g. Pharmacovigilance System
            Master File).

        contact: A product specific contact, person (in a role), or an organization.

        clinicalTrial: Clinical trials or studies that this product is involved in.

        name: The product's name, including full name and possibly coded parts.

        crossReference: Reference to another product, e.g. for linking authorised to investigational
            product.

        manufacturingBusinessOperation: An operation applied to the product, for manufacturing or adminsitrative
            purpose.

        specialDesignation: Indicates if the medicinal product has an orphan designation for the treatment
            of a rare disease.

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
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.marketingstatus import MarketingStatus
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.medicinalproduct_name import MedicinalProduct_Name
        from spark_fhir_schemas.r4.complex_types.medicinalproduct_manufacturingbusinessoperation import MedicinalProduct_ManufacturingBusinessOperation
        from spark_fhir_schemas.r4.complex_types.medicinalproduct_specialdesignation import MedicinalProduct_SpecialDesignation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MedicinalProduct resource
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
                # Business identifier for this product. Could be an MPID.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Regulatory type, e.g. Investigational or Authorized.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # If this medicine applies to human or veterinary uses.
                StructField(
                    "domain", Coding.get_schema(recursion_depth + 1), True
                ),
                # The dose form for a single part product, or combined form of a multiple part
                # product.
                StructField(
                    "combinedPharmaceuticalDoseForm",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The legal status of supply of the medicinal product as classified by the
                # regulator.
                StructField(
                    "legalStatusOfSupply",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Whether the Medicinal Product is subject to additional monitoring for
                # regulatory reasons.
                StructField(
                    "additionalMonitoringIndicator",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Whether the Medicinal Product is subject to special measures for regulatory
                # reasons.
                StructField("specialMeasures", ArrayType(StringType()), True),
                # If authorised for use in children.
                StructField(
                    "paediatricUseIndicator",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Allows the product to be classified by various systems.
                StructField(
                    "productClassification",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Marketing status of the medicinal product, in contrast to marketing
                # authorizaton.
                StructField(
                    "marketingStatus",
                    ArrayType(MarketingStatus.get_schema(recursion_depth + 1)),
                    True
                ),
                # Pharmaceutical aspects of product.
                StructField(
                    "pharmaceuticalProduct",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Package representation for the product.
                StructField(
                    "packagedMedicinalProduct",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Supporting documentation, typically for regulatory submission.
                StructField(
                    "attachedDocument",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A master file for to the medicinal product (e.g. Pharmacovigilance System
                # Master File).
                StructField(
                    "masterFile",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A product specific contact, person (in a role), or an organization.
                StructField(
                    "contact",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Clinical trials or studies that this product is involved in.
                StructField(
                    "clinicalTrial",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The product's name, including full name and possibly coded parts.
                StructField(
                    "name",
                    ArrayType(
                        MedicinalProduct_Name.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Reference to another product, e.g. for linking authorised to investigational
                # product.
                StructField(
                    "crossReference",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # An operation applied to the product, for manufacturing or adminsitrative
                # purpose.
                StructField(
                    "manufacturingBusinessOperation",
                    ArrayType(
                        MedicinalProduct_ManufacturingBusinessOperation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Indicates if the medicinal product has an orphan designation for the treatment
                # of a rare disease.
                StructField(
                    "specialDesignation",
                    ArrayType(
                        MedicinalProduct_SpecialDesignation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
