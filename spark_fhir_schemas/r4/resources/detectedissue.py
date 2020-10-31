from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DetectedIssue:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Indicates an actual or potential clinical issue with or between one or more
        active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
        Ineffective treatment frequency, Procedure-condition conflict, etc.


        resourceType: This is a DetectedIssue resource

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

        identifier: Business identifier associated with the detected issue record.

        status: Indicates the status of the detected issue.

        code: Identifies the general type of issue identified.

        severity: Indicates the degree of importance associated with the identified issue based
            on the potential impact on the patient.

        patient: Indicates the patient whose record the detected issue is associated with.

        identifiedDateTime: The date or period when the detected issue was initially identified.

        identifiedPeriod: The date or period when the detected issue was initially identified.

        author: Individual or device responsible for the issue being raised.  For example, a
            decision support application or a pharmacist conducting a medication review.

        implicated: Indicates the resource representing the current activity or proposed activity
            that is potentially problematic.

        evidence: Supporting evidence or manifestations that provide the basis for identifying
            the detected issue such as a GuidanceResponse or MeasureReport.

        detail: A textual explanation of the detected issue.

        reference: The literature, knowledge-base or similar reference that describes the
            propensity for the detected issue identified.

        mitigation: Indicates an action that has been taken or is committed to reduce or eliminate
            the likelihood of the risk identified by the detected issue from manifesting.
            Can also reflect an observation of known mitigating factors that may
            reduce/eliminate the need for any action.

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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.detectedissue_evidence import DetectedIssue_Evidence
        from spark_fhir_schemas.r4.complex_types.detectedissue_mitigation import DetectedIssue_Mitigation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a DetectedIssue resource
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
                # Business identifier associated with the detected issue record.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the status of the detected issue.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Identifies the general type of issue identified.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the degree of importance associated with the identified issue based
                # on the potential impact on the patient.
                StructField("severity", StringType(), True),
                # Indicates the patient whose record the detected issue is associated with.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # The date or period when the detected issue was initially identified.
                StructField("identifiedDateTime", StringType(), True),
                # The date or period when the detected issue was initially identified.
                StructField(
                    "identifiedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Individual or device responsible for the issue being raised.  For example, a
                # decision support application or a pharmacist conducting a medication review.
                StructField(
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                # Indicates the resource representing the current activity or proposed activity
                # that is potentially problematic.
                StructField(
                    "implicated",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Supporting evidence or manifestations that provide the basis for identifying
                # the detected issue such as a GuidanceResponse or MeasureReport.
                StructField(
                    "evidence",
                    ArrayType(
                        DetectedIssue_Evidence.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A textual explanation of the detected issue.
                StructField("detail", StringType(), True),
                # The literature, knowledge-base or similar reference that describes the
                # propensity for the detected issue identified.
                StructField(
                    "reference", uri.get_schema(recursion_depth + 1), True
                ),
                # Indicates an action that has been taken or is committed to reduce or eliminate
                # the likelihood of the risk identified by the detected issue from manifesting.
                # Can also reflect an observation of known mitigating factors that may
                # reduce/eliminate the need for any action.
                StructField(
                    "mitigation",
                    ArrayType(
                        DetectedIssue_Mitigation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
