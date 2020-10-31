from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationKnowledge:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Information about a medication that is used to support knowledge.


        resourceType: This is a MedicationKnowledge resource

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

        code: A code that specifies this medication, or a textual description if no code is
            available. Usage note: This could be a standard medication code such as a code
            from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local
            formulary code, optionally with translations to other code systems.

        status: A code to indicate if the medication is in active use.  The status refers to
            the validity about the information of the medication and not to its medicinal
            properties.

        manufacturer: Describes the details of the manufacturer of the medication product.  This is
            not intended to represent the distributor of a medication product.

        doseForm: Describes the form of the item.  Powder; tablets; capsule.

        amount: Specific amount of the drug in the packaged product.  For example, when
            specifying a product that has the same strength (For example, Insulin glargine
            100 unit per mL solution for injection), this attribute provides additional
            clarification of the package amount (For example, 3 mL, 10mL, etc.).

        synonym: Additional names for a medication, for example, the name(s) given to a
            medication in different countries.  For example, acetaminophen and paracetamol
            or salbutamol and albuterol.

        relatedMedicationKnowledge: Associated or related knowledge about a medication.

        associatedMedication: Associated or related medications.  For example, if the medication is a
            branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g.
            Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this
            would link to a branded product (e.g. Crestor).

        productType: Category of the medication or product (e.g. branded product, therapeutic
            moeity, generic product, innovator product, etc.).

        monograph: Associated documentation about the medication.

        ingredient: Identifies a particular constituent of interest in the product.

        preparationInstruction: The instructions for preparing the medication.

        intendedRoute: The intended or approved route of administration.

        cost: The price of the medication.

        monitoringProgram: The program under which the medication is reviewed.

        administrationGuidelines: Guidelines for the administration of the medication.

        medicineClassification: Categorization of the medication within a formulary or classification system.

        packaging: Information that only applies to packages (not products).

        drugCharacteristic: Specifies descriptive properties of the medicine, such as color, shape,
            imprints, etc.

        contraindication: Potential clinical issue with or between medication(s) (for example, drug-drug
            interaction, drug-disease contraindication, drug-allergy interaction, etc.).

        regulatory: Regulatory information about a medication.

        kinetics: The time course of drug absorption, distribution, metabolism and excretion of
            a medication from the body.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_relatedmedicationknowledge import MedicationKnowledge_RelatedMedicationKnowledge
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_monograph import MedicationKnowledge_Monograph
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_ingredient import MedicationKnowledge_Ingredient
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_cost import MedicationKnowledge_Cost
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_monitoringprogram import MedicationKnowledge_MonitoringProgram
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_administrationguidelines import MedicationKnowledge_AdministrationGuidelines
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_medicineclassification import MedicationKnowledge_MedicineClassification
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_packaging import MedicationKnowledge_Packaging
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_drugcharacteristic import MedicationKnowledge_DrugCharacteristic
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_regulatory import MedicationKnowledge_Regulatory
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_kinetics import MedicationKnowledge_Kinetics
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MedicationKnowledge resource
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
                # A code that specifies this medication, or a textual description if no code is
                # available. Usage note: This could be a standard medication code such as a code
                # from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local
                # formulary code, optionally with translations to other code systems.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A code to indicate if the medication is in active use.  The status refers to
                # the validity about the information of the medication and not to its medicinal
                # properties.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Describes the details of the manufacturer of the medication product.  This is
                # not intended to represent the distributor of a medication product.
                StructField(
                    "manufacturer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Describes the form of the item.  Powder; tablets; capsule.
                StructField(
                    "doseForm",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Specific amount of the drug in the packaged product.  For example, when
                # specifying a product that has the same strength (For example, Insulin glargine
                # 100 unit per mL solution for injection), this attribute provides additional
                # clarification of the package amount (For example, 3 mL, 10mL, etc.).
                StructField(
                    "amount", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Additional names for a medication, for example, the name(s) given to a
                # medication in different countries.  For example, acetaminophen and paracetamol
                # or salbutamol and albuterol.
                StructField("synonym", ArrayType(StringType()), True),
                # Associated or related knowledge about a medication.
                StructField(
                    "relatedMedicationKnowledge",
                    ArrayType(
                        MedicationKnowledge_RelatedMedicationKnowledge.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Associated or related medications.  For example, if the medication is a
                # branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g.
                # Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this
                # would link to a branded product (e.g. Crestor).
                StructField(
                    "associatedMedication",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Category of the medication or product (e.g. branded product, therapeutic
                # moeity, generic product, innovator product, etc.).
                StructField(
                    "productType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Associated documentation about the medication.
                StructField(
                    "monograph",
                    ArrayType(
                        MedicationKnowledge_Monograph.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies a particular constituent of interest in the product.
                StructField(
                    "ingredient",
                    ArrayType(
                        MedicationKnowledge_Ingredient.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The instructions for preparing the medication.
                StructField(
                    "preparationInstruction",
                    markdown.get_schema(recursion_depth + 1), True
                ),
                # The intended or approved route of administration.
                StructField(
                    "intendedRoute",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The price of the medication.
                StructField(
                    "cost",
                    ArrayType(
                        MedicationKnowledge_Cost.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The program under which the medication is reviewed.
                StructField(
                    "monitoringProgram",
                    ArrayType(
                        MedicationKnowledge_MonitoringProgram.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Guidelines for the administration of the medication.
                StructField(
                    "administrationGuidelines",
                    ArrayType(
                        MedicationKnowledge_AdministrationGuidelines.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Categorization of the medication within a formulary or classification system.
                StructField(
                    "medicineClassification",
                    ArrayType(
                        MedicationKnowledge_MedicineClassification.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Information that only applies to packages (not products).
                StructField(
                    "packaging",
                    MedicationKnowledge_Packaging.
                    get_schema(recursion_depth + 1), True
                ),
                # Specifies descriptive properties of the medicine, such as color, shape,
                # imprints, etc.
                StructField(
                    "drugCharacteristic",
                    ArrayType(
                        MedicationKnowledge_DrugCharacteristic.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Potential clinical issue with or between medication(s) (for example, drug-drug
                # interaction, drug-disease contraindication, drug-allergy interaction, etc.).
                StructField(
                    "contraindication",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Regulatory information about a medication.
                StructField(
                    "regulatory",
                    ArrayType(
                        MedicationKnowledge_Regulatory.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The time course of drug absorption, distribution, metabolism and excretion of
                # a medication from the body.
                StructField(
                    "kinetics",
                    ArrayType(
                        MedicationKnowledge_Kinetics.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
