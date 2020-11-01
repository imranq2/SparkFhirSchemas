from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ImmunizationSchema:
    """
    Describes the event of a patient being administered a vaccine or a record of
    an immunization as reported by a patient, a clinician or another party.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        Describes the event of a patient being administered a vaccine or a record of
        an immunization as reported by a patient, a clinician or another party.


        resourceType: This is a Immunization resource

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

        identifier: A unique identifier assigned to this immunization record.

        status: Indicates the current status of the immunization event.

        statusReason: Indicates the reason the immunization event was not performed.

        vaccineCode: Vaccine that was administered or was to be administered.

        patient: The patient who either received or did not receive the immunization.

        encounter: The visit or admission or other contact between patient and health care
            provider the immunization was performed as part of.

        occurrenceDateTime: Date vaccine administered or was to be administered.

        occurrenceString: Date vaccine administered or was to be administered.

        recorded: The date the occurrence of the immunization was first captured in the record -
            potentially significantly after the occurrence of the event.

        primarySource: An indication that the content of the record is based on information from the
            person who administered the vaccine. This reflects the context under which the
            data was originally recorded.

        reportOrigin: The source of the data when the report of the immunization event is not based
            on information from the person who administered the vaccine.

        location: The service delivery location where the vaccine administration occurred.

        manufacturer: Name of vaccine manufacturer.

        lotNumber: Lot number of the  vaccine product.

        expirationDate: Date vaccine batch expires.

        site: Body site where vaccine was administered.

        route: The path by which the vaccine product is taken into the body.

        doseQuantity: The quantity of vaccine product that was administered.

        performer: Indicates who performed the immunization event.

        note: Extra information about the immunization that is not conveyed by the other
            attributes.

        reasonCode: Reasons why the vaccine was administered.

        reasonReference: Condition, Observation or DiagnosticReport that supports why the immunization
            was administered.

        isSubpotent: Indication if a dose is considered to be subpotent. By default, a dose should
            be considered to be potent.

        subpotentReason: Reason why a dose is considered to be subpotent.

        education: Educational material presented to the patient (or guardian) at the time of
            vaccine administration.

        programEligibility: Indicates a patient's eligibility for a funding program.

        fundingSource: Indicates the source of the vaccine actually administered. This may be
            different than the patient eligibility (e.g. the patient may be eligible for a
            publically purchased vaccine but due to inventory issues, vaccine purchased
            with private funds was actually administered).

        reaction: Categorical data indicating that an adverse event is associated in time to an
            immunization.

        protocolApplied: The protocol (set of recommendations) being followed by the provider who
            administered the dose.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.immunization_performer import Immunization_PerformerSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.r4.complex_types.immunization_education import Immunization_EducationSchema
        from spark_fhir_schemas.r4.complex_types.immunization_reaction import Immunization_ReactionSchema
        from spark_fhir_schemas.r4.complex_types.immunization_protocolapplied import Immunization_ProtocolAppliedSchema
        if recursion_list.count(
            "Immunization"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + ["Immunization"]
        schema = StructType(
            [
                # This is a Immunization resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
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
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.

                # >>> Hiding extension Extension

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

                # >>> Hiding modifierExtension Extension

                # A unique identifier assigned to this immunization record.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Indicates the current status of the immunization event.
                StructField(
                    "status",
                    codeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates the reason the immunization event was not performed.
                StructField(
                    "statusReason",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Vaccine that was administered or was to be administered.
                StructField(
                    "vaccineCode",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The patient who either received or did not receive the immunization.
                StructField(
                    "patient",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The visit or admission or other contact between patient and health care
                # provider the immunization was performed as part of.
                StructField(
                    "encounter",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Date vaccine administered or was to be administered.
                StructField("occurrenceDateTime", StringType(), True),
                # Date vaccine administered or was to be administered.
                StructField("occurrenceString", StringType(), True),
                # The date the occurrence of the immunization was first captured in the record -
                # potentially significantly after the occurrence of the event.
                StructField(
                    "recorded",
                    dateTimeSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # An indication that the content of the record is based on information from the
                # person who administered the vaccine. This reflects the context under which the
                # data was originally recorded.
                StructField("primarySource", BooleanType(), True),
                # The source of the data when the report of the immunization event is not based
                # on information from the person who administered the vaccine.
                StructField(
                    "reportOrigin",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The service delivery location where the vaccine administration occurred.
                StructField(
                    "location",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Name of vaccine manufacturer.
                StructField(
                    "manufacturer",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Lot number of the  vaccine product.
                StructField("lotNumber", StringType(), True),
                # Date vaccine batch expires.
                StructField("expirationDate", DateType(), True),
                # Body site where vaccine was administered.
                StructField(
                    "site",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The path by which the vaccine product is taken into the body.
                StructField(
                    "route",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # The quantity of vaccine product that was administered.
                StructField(
                    "doseQuantity",
                    QuantitySchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates who performed the immunization event.
                StructField(
                    "performer",
                    ArrayType(
                        Immunization_PerformerSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Extra information about the immunization that is not conveyed by the other
                # attributes.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Reasons why the vaccine was administered.
                StructField(
                    "reasonCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Condition, Observation or DiagnosticReport that supports why the immunization
                # was administered.
                StructField(
                    "reasonReference",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Indication if a dose is considered to be subpotent. By default, a dose should
                # be considered to be potent.
                StructField("isSubpotent", BooleanType(), True),
                # Reason why a dose is considered to be subpotent.
                StructField(
                    "subpotentReason",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Educational material presented to the patient (or guardian) at the time of
                # vaccine administration.
                StructField(
                    "education",
                    ArrayType(
                        Immunization_EducationSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Indicates a patient's eligibility for a funding program.
                StructField(
                    "programEligibility",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # Indicates the source of the vaccine actually administered. This may be
                # different than the patient eligibility (e.g. the patient may be eligible for a
                # publically purchased vaccine but due to inventory issues, vaccine purchased
                # with private funds was actually administered).
                StructField(
                    "fundingSource",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Categorical data indicating that an adverse event is associated in time to an
                # immunization.
                StructField(
                    "reaction",
                    ArrayType(
                        Immunization_ReactionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # The protocol (set of recommendations) being followed by the provider who
                # administered the dose.
                StructField(
                    "protocolApplied",
                    ArrayType(
                        Immunization_ProtocolAppliedSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
            ]
        )
        return schema
