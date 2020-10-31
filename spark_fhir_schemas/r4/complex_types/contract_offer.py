from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Contract_OfferSchema:
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: Unique identifier for this particular Contract Provision.

        party: Offer Recipient.

        topic: The owner of an asset has the residual control rights over the asset: the
            right to decide all usages of the asset in any way not inconsistent with a
            prior contract, custom, or law (Hart, 1995, p. 30).

        type: Type of Contract Provision such as specific requirements, purposes for
            actions, obligations, prohibitions, e.g. life time maximum benefit.

        decision: Type of choice made by accepting party with respect to an offer made by an
            offeror/ grantee.

        decisionMode: How the decision about a Contract was conveyed.

        answer: Response to offer text.

        text: Human readable form of this Contract Offer.

        linkId: The id of the clause or question text of the offer in the referenced
            questionnaire/response.

        securityLabelNumber: Security labels that protects the offer.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.contract_party import Contract_PartySchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.contract_answer import Contract_AnswerSchema
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedIntSchema
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Unique identifier for this particular Contract Provision.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Offer Recipient.
                StructField(
                    "party",
                    ArrayType(
                        Contract_PartySchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The owner of an asset has the residual control rights over the asset: the
                # right to decide all usages of the asset in any way not inconsistent with a
                # prior contract, custom, or law (Hart, 1995, p. 30).
                StructField(
                    "topic", ReferenceSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # Type of Contract Provision such as specific requirements, purposes for
                # actions, obligations, prohibitions, e.g. life time maximum benefit.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # Type of choice made by accepting party with respect to an offer made by an
                # offeror/ grantee.
                StructField(
                    "decision",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # How the decision about a Contract was conveyed.
                StructField(
                    "decisionMode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Response to offer text.
                StructField(
                    "answer",
                    ArrayType(
                        Contract_AnswerSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Human readable form of this Contract Offer.
                StructField("text", StringType(), True),
                # The id of the clause or question text of the offer in the referenced
                # questionnaire/response.
                StructField("linkId", ArrayType(StringType()), True),
                # Security labels that protects the offer.
                StructField(
                    "securityLabelNumber",
                    ArrayType(
                        unsignedIntSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
