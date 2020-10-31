from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_Term:
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

        issued: When this Contract Provision was issued.

        applies: Relevant time or time-period when this Contract Provision is applicable.

        topicCodeableConcept: The entity that the term applies to.

        topicReference: The entity that the term applies to.

        type: A legal clause or condition contained within a contract that requires one or
            both parties to perform a particular requirement by some specified time or
            prevents one or both parties from performing a particular requirement by some
            specified time.

        subType: A specialized legal clause or condition based on overarching contract type.

        text: Statement of a provision in a policy or a contract.

        securityLabel: Security labels that protect the handling of information about the term and
            its elements, which may be specifically identified..

        offer: The matter of concern in the context of this provision of the agrement.

        asset: Contract Term Asset List.

        action: An actor taking a role in an activity for which it can be assigned some degree
            of responsibility for the activity taking place.

        group: Nested group of Contract Provisions.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.contract_securitylabel import Contract_SecurityLabel
        from spark_fhir_schemas.r4.complex_types.contract_offer import Contract_Offer
        from spark_fhir_schemas.r4.complex_types.contract_asset import Contract_Asset
        from spark_fhir_schemas.r4.complex_types.contract_action import Contract_Action
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Unique identifier for this particular Contract Provision.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # When this Contract Provision was issued.
                StructField(
                    "issued", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Relevant time or time-period when this Contract Provision is applicable.
                StructField(
                    "applies", Period.get_schema(recursion_depth + 1), True
                ),
                # The entity that the term applies to.
                StructField(
                    "topicCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The entity that the term applies to.
                StructField(
                    "topicReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A legal clause or condition contained within a contract that requires one or
                # both parties to perform a particular requirement by some specified time or
                # prevents one or both parties from performing a particular requirement by some
                # specified time.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A specialized legal clause or condition based on overarching contract type.
                StructField(
                    "subType", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Statement of a provision in a policy or a contract.
                StructField("text", StringType(), True),
                # Security labels that protect the handling of information about the term and
                # its elements, which may be specifically identified..
                StructField(
                    "securityLabel",
                    ArrayType(
                        Contract_SecurityLabel.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The matter of concern in the context of this provision of the agrement.
                StructField(
                    "offer", Contract_Offer.get_schema(recursion_depth + 1),
                    True
                ),
                # Contract Term Asset List.
                StructField(
                    "asset",
                    ArrayType(Contract_Asset.get_schema(recursion_depth + 1)),
                    True
                ),
                # An actor taking a role in an activity for which it can be assigned some degree
                # of responsibility for the activity taking place.
                StructField(
                    "action",
                    ArrayType(Contract_Action.get_schema(recursion_depth + 1)),
                    True
                ),
                # Nested group of Contract Provisions.
                StructField(
                    "group",
                    ArrayType(Contract_Term.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
