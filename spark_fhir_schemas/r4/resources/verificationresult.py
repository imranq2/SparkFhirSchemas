from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class VerificationResult:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes validation requirements, source(s), status and dates for one or more
        elements.


        resourceType: This is a VerificationResult resource

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

        target: A resource that was validated.

        targetLocation: The fhirpath location(s) within the resource that was validated.

        need: The frequency with which the target must be validated (none; initial;
            periodic).

        status: The validation status of the target (attested; validated; in process; requires
            revalidation; validation failed; revalidation failed).

        statusDate: When the validation status was updated.

        validationType: What the target is validated against (nothing; primary source; multiple
            sources).

        validationProcess: The primary process by which the target is validated (edit check; value set;
            primary source; multiple sources; standalone; in context).

        frequency: Frequency of revalidation.

        lastPerformed: The date/time validation was last completed (including failed validations).

        nextScheduled: The date when target is next validated, if appropriate.

        failureAction: The result if validation fails (fatal; warning; record only; none).

        primarySource: Information about the primary source(s) involved in validation.

        attestation: Information about the entity attesting to information.

        validator: Information about the entity validating information.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.verificationresult_primarysource import VerificationResult_PrimarySource
        from spark_fhir_schemas.r4.complex_types.verificationresult_attestation import VerificationResult_Attestation
        from spark_fhir_schemas.r4.complex_types.verificationresult_validator import VerificationResult_Validator
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a VerificationResult resource
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
                # A resource that was validated.
                StructField(
                    "target",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The fhirpath location(s) within the resource that was validated.
                StructField("targetLocation", ArrayType(StringType()), True),
                # The frequency with which the target must be validated (none; initial;
                # periodic).
                StructField(
                    "need", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The validation status of the target (attested; validated; in process; requires
                # revalidation; validation failed; revalidation failed).
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # When the validation status was updated.
                StructField(
                    "statusDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # What the target is validated against (nothing; primary source; multiple
                # sources).
                StructField(
                    "validationType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The primary process by which the target is validated (edit check; value set;
                # primary source; multiple sources; standalone; in context).
                StructField(
                    "validationProcess",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Frequency of revalidation.
                StructField(
                    "frequency", Timing.get_schema(recursion_depth + 1), True
                ),
                # The date/time validation was last completed (including failed validations).
                StructField(
                    "lastPerformed", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The date when target is next validated, if appropriate.
                StructField("nextScheduled", DateType(), True),
                # The result if validation fails (fatal; warning; record only; none).
                StructField(
                    "failureAction",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Information about the primary source(s) involved in validation.
                StructField(
                    "primarySource",
                    ArrayType(
                        VerificationResult_PrimarySource.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Information about the entity attesting to information.
                StructField(
                    "attestation",
                    VerificationResult_Attestation.
                    get_schema(recursion_depth + 1), True
                ),
                # Information about the entity validating information.
                StructField(
                    "validator",
                    ArrayType(
                        VerificationResult_Validator.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
