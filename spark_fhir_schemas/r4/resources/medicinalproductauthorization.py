from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicinalProductAuthorization:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The regulatory authorization of a medicinal product.


        resourceType: This is a MedicinalProductAuthorization resource

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

        identifier: Business identifier for the marketing authorization, as assigned by a
            regulator.

        subject: The medicinal product that is being authorized.

        country: The country in which the marketing authorization has been granted.

        jurisdiction: Jurisdiction within a country.

        status: The status of the marketing authorization.

        statusDate: The date at which the given status has become applicable.

        restoreDate: The date when a suspended the marketing or the marketing authorization of the
            product is anticipated to be restored.

        validityPeriod: The beginning of the time period in which the marketing authorization is in
            the specific status shall be specified A complete date consisting of day,
            month and year shall be specified using the ISO 8601 date format.

        dataExclusivityPeriod: A period of time after authorization before generic product applicatiosn can
            be submitted.

        dateOfFirstAuthorization: The date when the first authorization was granted by a Medicines Regulatory
            Agency.

        internationalBirthDate: Date of first marketing authorization for a company's new medicinal product in
            any country in the World.

        legalBasis: The legal framework against which this authorization is granted.

        jurisdictionalAuthorization: Authorization in areas within a country.

        holder: Marketing Authorization Holder.

        regulator: Medicines Regulatory Agency.

        procedure: The regulatory procedure for granting or amending a marketing authorization.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.medicinalproductauthorization_jurisdictionalauthorization import MedicinalProductAuthorization_JurisdictionalAuthorization
        from spark_fhir_schemas.r4.complex_types.medicinalproductauthorization_procedure import MedicinalProductAuthorization_Procedure
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MedicinalProductAuthorization resource
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
                # Business identifier for the marketing authorization, as assigned by a
                # regulator.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The medicinal product that is being authorized.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The country in which the marketing authorization has been granted.
                StructField(
                    "country",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Jurisdiction within a country.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The status of the marketing authorization.
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The date at which the given status has become applicable.
                StructField(
                    "statusDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The date when a suspended the marketing or the marketing authorization of the
                # product is anticipated to be restored.
                StructField(
                    "restoreDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The beginning of the time period in which the marketing authorization is in
                # the specific status shall be specified A complete date consisting of day,
                # month and year shall be specified using the ISO 8601 date format.
                StructField(
                    "validityPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # A period of time after authorization before generic product applicatiosn can
                # be submitted.
                StructField(
                    "dataExclusivityPeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                # The date when the first authorization was granted by a Medicines Regulatory
                # Agency.
                StructField(
                    "dateOfFirstAuthorization",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                # Date of first marketing authorization for a company's new medicinal product in
                # any country in the World.
                StructField(
                    "internationalBirthDate",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                # The legal framework against which this authorization is granted.
                StructField(
                    "legalBasis",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Authorization in areas within a country.
                StructField(
                    "jurisdictionalAuthorization",
                    ArrayType(
                        MedicinalProductAuthorization_JurisdictionalAuthorization
                        .get_schema(recursion_depth + 1)
                    ), True
                ),
                # Marketing Authorization Holder.
                StructField(
                    "holder", Reference.get_schema(recursion_depth + 1), True
                ),
                # Medicines Regulatory Agency.
                StructField(
                    "regulator", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The regulatory procedure for granting or amending a marketing authorization.
                StructField(
                    "procedure",
                    MedicinalProductAuthorization_Procedure.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
