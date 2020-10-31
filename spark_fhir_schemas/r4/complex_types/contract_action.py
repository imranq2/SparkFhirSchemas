from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_Action:
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

        doNotPerform: True if the term prohibits the  action.

        type: Activity or service obligation to be done or not done, performed or not
            performed, effectuated or not by this Contract term.

        subject: Entity of the action.

        intent: Reason or purpose for the action stipulated by this Contract Provision.

        linkId: Id [identifier??] of the clause or question text related to this action in the
            referenced form or QuestionnaireResponse.

        status: Current state of the term action.

        context: Encounter or Episode with primary association to specified term activity.

        contextLinkId: Id [identifier??] of the clause or question text related to the requester of
            this action in the referenced form or QuestionnaireResponse.

        occurrenceDateTime: When action happens.

        occurrencePeriod: When action happens.

        occurrenceTiming: When action happens.

        requester: Who or what initiated the action and has responsibility for its activation.

        requesterLinkId: Id [identifier??] of the clause or question text related to the requester of
            this action in the referenced form or QuestionnaireResponse.

        performerType: The type of individual that is desired or required to perform or not perform
            the action.

        performerRole: The type of role or competency of an individual desired or required to perform
            or not perform the action.

        performer: Indicates who or what is being asked to perform (or not perform) the ction.

        performerLinkId: Id [identifier??] of the clause or question text related to the reason type or
            reference of this  action in the referenced form or QuestionnaireResponse.

        reasonCode: Rationale for the action to be performed or not performed. Describes why the
            action is permitted or prohibited.

        reasonReference: Indicates another resource whose existence justifies permitting or not
            permitting this action.

        reason: Describes why the action is to be performed or not performed in textual form.

        reasonLinkId: Id [identifier??] of the clause or question text related to the reason type or
            reference of this  action in the referenced form or QuestionnaireResponse.

        note: Comments made about the term action made by the requester, performer, subject
            or other participants.

        securityLabelNumber: Security labels that protects the action.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.contract_subject import Contract_Subject
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
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
                # True if the term prohibits the  action.
                StructField("doNotPerform", BooleanType(), True),
                # Activity or service obligation to be done or not done, performed or not
                # performed, effectuated or not by this Contract term.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Entity of the action.
                StructField(
                    "subject",
                    ArrayType(
                        Contract_Subject.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Reason or purpose for the action stipulated by this Contract Provision.
                StructField(
                    "intent", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Id [identifier??] of the clause or question text related to this action in the
                # referenced form or QuestionnaireResponse.
                StructField("linkId", ArrayType(StringType()), True),
                # Current state of the term action.
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Encounter or Episode with primary association to specified term activity.
                StructField(
                    "context", Reference.get_schema(recursion_depth + 1), True
                ),
                # Id [identifier??] of the clause or question text related to the requester of
                # this action in the referenced form or QuestionnaireResponse.
                StructField("contextLinkId", ArrayType(StringType()), True),
                # When action happens.
                StructField("occurrenceDateTime", StringType(), True),
                # When action happens.
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # When action happens.
                StructField(
                    "occurrenceTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # Who or what initiated the action and has responsibility for its activation.
                StructField(
                    "requester",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Id [identifier??] of the clause or question text related to the requester of
                # this action in the referenced form or QuestionnaireResponse.
                StructField("requesterLinkId", ArrayType(StringType()), True),
                # The type of individual that is desired or required to perform or not perform
                # the action.
                StructField(
                    "performerType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The type of role or competency of an individual desired or required to perform
                # or not perform the action.
                StructField(
                    "performerRole",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates who or what is being asked to perform (or not perform) the ction.
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Id [identifier??] of the clause or question text related to the reason type or
                # reference of this  action in the referenced form or QuestionnaireResponse.
                StructField("performerLinkId", ArrayType(StringType()), True),
                # Rationale for the action to be performed or not performed. Describes why the
                # action is permitted or prohibited.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource whose existence justifies permitting or not
                # permitting this action.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Describes why the action is to be performed or not performed in textual form.
                StructField("reason", ArrayType(StringType()), True),
                # Id [identifier??] of the clause or question text related to the reason type or
                # reference of this  action in the referenced form or QuestionnaireResponse.
                StructField("reasonLinkId", ArrayType(StringType()), True),
                # Comments made about the term action made by the requester, performer, subject
                # or other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Security labels that protects the action.
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
