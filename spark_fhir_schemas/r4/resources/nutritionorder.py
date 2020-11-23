from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NutritionOrderSchema:
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
        """
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


        resourceType: This is a NutritionOrder resource

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

        identifier: Identifiers assigned to this order by the order sender or by the order
            receiver.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this NutritionOrder.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            NutritionOrder.

        instantiates: The URL pointing to a protocol, guideline, orderset or other definition that
            is adhered to in whole or in part by this NutritionOrder.

        status: The workflow status of the nutrition order/request.

        intent: Indicates the level of authority/intentionality associated with the
            NutrionOrder and where the request fits into the workflow chain.

        patient: The person (patient) who needs the nutrition order for an oral diet,
            nutritional supplement and/or enteral or formula feeding.

        encounter: An encounter that provides additional information about the healthcare context
            in which this request is made.

        dateTime: The date and time that this nutrition order was requested.

        orderer: The practitioner that holds legal responsibility for ordering the diet,
            nutritional supplement, or formula feedings.

        allergyIntolerance: A link to a record of allergies or intolerances  which should be included in
            the nutrition order.

        foodPreferenceModifier: This modifier is used to convey order-specific modifiers about the type of
            food that should be given. These can be derived from patient allergies,
            intolerances, or preferences such as Halal, Vegan or Kosher. This modifier
            applies to the entire nutrition order inclusive of the oral diet, nutritional
            supplements and enteral formula feedings.

        excludeFoodModifier: This modifier is used to convey Order-specific modifier about the type of oral
            food or oral fluids that should not be given. These can be derived from
            patient allergies, intolerances, or preferences such as No Red Meat, No Soy or
            No Wheat or  Gluten-Free.  While it should not be necessary to repeat allergy
            or intolerance information captured in the referenced AllergyIntolerance
            resource in the excludeFoodModifier, this element may be used to convey
            additional specificity related to foods that should be eliminated from the
            patient’s diet for any reason.  This modifier applies to the entire nutrition
            order inclusive of the oral diet, nutritional supplements and enteral formula
            feedings.

        oralDiet: Diet given orally in contrast to enteral (tube) feeding.

        supplement: Oral nutritional products given in order to add further nutritional value to
            the patient's diet.

        enteralFormula: Feeding provided through the gastrointestinal tract via a tube, catheter, or
            stoma that delivers nutrition distal to the oral cavity.

        note: Comments made about the {{title}} by the requester, performer, subject or
            other participants.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.nutritionorder_oraldiet import NutritionOrder_OralDietSchema
        from spark_fhir_schemas.r4.complex_types.nutritionorder_supplement import NutritionOrder_SupplementSchema
        from spark_fhir_schemas.r4.complex_types.nutritionorder_enteralformula import NutritionOrder_EnteralFormulaSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        if (
            max_recursion_limit
            and nesting_list.count("NutritionOrder") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["NutritionOrder"]
        schema = StructType(
            [
                # This is a NutritionOrder resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Identifiers assigned to this order by the order sender or by the order
                # receiver.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this NutritionOrder.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(
                        canonicalSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # NutritionOrder.
                StructField(
                    "instantiatesUri",
                    ArrayType(
                        uriSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The URL pointing to a protocol, guideline, orderset or other definition that
                # is adhered to in whole or in part by this NutritionOrder.
                StructField(
                    "instantiates",
                    ArrayType(
                        uriSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The workflow status of the nutrition order/request.
                StructField(
                    "status",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Indicates the level of authority/intentionality associated with the
                # NutrionOrder and where the request fits into the workflow chain.
                StructField(
                    "intent",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The person (patient) who needs the nutrition order for an oral diet,
                # nutritional supplement and/or enteral or formula feeding.
                StructField(
                    "patient",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # An encounter that provides additional information about the healthcare context
                # in which this request is made.
                StructField(
                    "encounter",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The date and time that this nutrition order was requested.
                StructField(
                    "dateTime",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The practitioner that holds legal responsibility for ordering the diet,
                # nutritional supplement, or formula feedings.
                StructField(
                    "orderer",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A link to a record of allergies or intolerances  which should be included in
                # the nutrition order.
                StructField(
                    "allergyIntolerance",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # This modifier is used to convey order-specific modifiers about the type of
                # food that should be given. These can be derived from patient allergies,
                # intolerances, or preferences such as Halal, Vegan or Kosher. This modifier
                # applies to the entire nutrition order inclusive of the oral diet, nutritional
                # supplements and enteral formula feedings.
                StructField(
                    "foodPreferenceModifier",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # This modifier is used to convey Order-specific modifier about the type of oral
                # food or oral fluids that should not be given. These can be derived from
                # patient allergies, intolerances, or preferences such as No Red Meat, No Soy or
                # No Wheat or  Gluten-Free.  While it should not be necessary to repeat allergy
                # or intolerance information captured in the referenced AllergyIntolerance
                # resource in the excludeFoodModifier, this element may be used to convey
                # additional specificity related to foods that should be eliminated from the
                # patient’s diet for any reason.  This modifier applies to the entire nutrition
                # order inclusive of the oral diet, nutritional supplements and enteral formula
                # feedings.
                StructField(
                    "excludeFoodModifier",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Diet given orally in contrast to enteral (tube) feeding.
                StructField(
                    "oralDiet",
                    NutritionOrder_OralDietSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Oral nutritional products given in order to add further nutritional value to
                # the patient's diet.
                StructField(
                    "supplement",
                    ArrayType(
                        NutritionOrder_SupplementSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Feeding provided through the gastrointestinal tract via a tube, catheter, or
                # stoma that delivers nutrition distal to the oral cavity.
                StructField(
                    "enteralFormula",
                    NutritionOrder_EnteralFormulaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Comments made about the {{title}} by the requester, performer, subject or
                # other participants.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
