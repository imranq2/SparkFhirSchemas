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
class MedicationStatementSchema:
    """
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the medication
    now or has taken the medication in the past or will be taking the medication
    in the future.  The source of this information can be the patient, significant
    other (such as a family member or spouse), or a clinician.  A common scenario
    where this information is captured is during the history taking process during
    a patient visit or stay.   The medication information may come from sources
    such as the patient's memory, from a prescription bottle,  or from a list of
    medications the patient, clinician or other party maintains.

    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration information
    from the person who administered the medication.  A medication statement is
    often, if not always, less specific.  There is no required date/time when the
    medication was administered, in fact we only know that a source has reported
    the patient is taking this medication, where details such as time, quantity,
    or rate or even medication product may be incomplete or missing or less
    precise.  As stated earlier, the medication statement information may come
    from the patient's memory, from a prescription bottle or from a list of
    medications the patient, clinician or other party maintains.  Medication
    administration is more formal and is not missing detailed information.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A record of a medication that is being consumed by a patient.   A
        MedicationStatement may indicate that the patient may be taking the medication
        now or has taken the medication in the past or will be taking the medication
        in the future.  The source of this information can be the patient, significant
        other (such as a family member or spouse), or a clinician.  A common scenario
        where this information is captured is during the history taking process during
        a patient visit or stay.   The medication information may come from sources
        such as the patient's memory, from a prescription bottle,  or from a list of
        medications the patient, clinician or other party maintains.

        The primary difference between a medication statement and a medication
        administration is that the medication administration has complete
        administration information and is based on actual administration information
        from the person who administered the medication.  A medication statement is
        often, if not always, less specific.  There is no required date/time when the
        medication was administered, in fact we only know that a source has reported
        the patient is taking this medication, where details such as time, quantity,
        or rate or even medication product may be incomplete or missing or less
        precise.  As stated earlier, the medication statement information may come
        from the patient's memory, from a prescription bottle or from a list of
        medications the patient, clinician or other party maintains.  Medication
        administration is more formal and is not missing detailed information.


        resourceType: This is a MedicationStatement resource

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

        identifier: Identifiers associated with this Medication Statement that are defined by
            business processes and/or used to refer to it when a direct URL reference to
            the resource itself is not appropriate. They are business identifiers assigned
            to this resource by the performer or other systems and remain constant as the
            resource is updated and propagates from server to server.

        basedOn: A plan, proposal or order that is fulfilled in whole or in part by this event.

        partOf: A larger event of which this particular event is a component or step.

        status: A code representing the patient or other source's judgment about the state of
            the medication used that this statement is about.  Generally, this will be
            active or completed.

        statusReason: Captures the reason for the current state of the MedicationStatement.

        category: Indicates where the medication is expected to be consumed or administered.

        medicationCodeableConcept: Identifies the medication being administered. This is either a link to a
            resource representing the details of the medication or a simple attribute
            carrying a code that identifies the medication from a known list of
            medications.

        medicationReference: Identifies the medication being administered. This is either a link to a
            resource representing the details of the medication or a simple attribute
            carrying a code that identifies the medication from a known list of
            medications.

        subject: The person, animal or group who is/was taking the medication.

        context: The encounter or episode of care that establishes the context for this
            MedicationStatement.

        effectiveDateTime: The interval of time during which it is being asserted that the patient
            is/was/will be taking the medication (or was not taking, when the
            MedicationStatement.taken element is No).

        effectivePeriod: The interval of time during which it is being asserted that the patient
            is/was/will be taking the medication (or was not taking, when the
            MedicationStatement.taken element is No).

        dateAsserted: The date when the medication statement was asserted by the information source.

        informationSource: The person or organization that provided the information about the taking of
            this medication. Note: Use derivedFrom when a MedicationStatement is derived
            from other resources, e.g. Claim or MedicationRequest.

        derivedFrom: Allows linking the MedicationStatement to the underlying MedicationRequest, or
            to other information that supports or is used to derive the
            MedicationStatement.

        reasonCode: A reason for why the medication is being/was taken.

        reasonReference: Condition or observation that supports why the medication is being/was taken.

        note: Provides extra information about the medication statement that is not conveyed
            by the other attributes.

        dosage: Indicates how the medication is/was or should be taken by the patient.

        """
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
        from spark_fhir_schemas.r4.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4.simple_types.code import codeSchema
        from spark_fhir_schemas.r4.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.r4.complex_types.dosage import DosageSchema
        if (
            max_recursion_limit and
            nesting_list.count("MedicationStatement") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationStatement"]
        schema = StructType(
            [
                # This is a MedicationStatement resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
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
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
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
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
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
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
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
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
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
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Identifiers associated with this Medication Statement that are defined by
                # business processes and/or used to refer to it when a direct URL reference to
                # the resource itself is not appropriate. They are business identifiers assigned
                # to this resource by the performer or other systems and remain constant as the
                # resource is updated and propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A plan, proposal or order that is fulfilled in whole or in part by this event.
                StructField(
                    "basedOn",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A larger event of which this particular event is a component or step.
                StructField(
                    "partOf",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A code representing the patient or other source's judgment about the state of
                # the medication used that this statement is about.  Generally, this will be
                # active or completed.
                StructField(
                    "status",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Captures the reason for the current state of the MedicationStatement.
                StructField(
                    "statusReason",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Indicates where the medication is expected to be consumed or administered.
                StructField(
                    "category",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Identifies the medication being administered. This is either a link to a
                # resource representing the details of the medication or a simple attribute
                # carrying a code that identifies the medication from a known list of
                # medications.
                StructField(
                    "medicationCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Identifies the medication being administered. This is either a link to a
                # resource representing the details of the medication or a simple attribute
                # carrying a code that identifies the medication from a known list of
                # medications.
                StructField(
                    "medicationReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The person, animal or group who is/was taking the medication.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The encounter or episode of care that establishes the context for this
                # MedicationStatement.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The interval of time during which it is being asserted that the patient
                # is/was/will be taking the medication (or was not taking, when the
                # MedicationStatement.taken element is No).
                StructField("effectiveDateTime", StringType(), True),
                # The interval of time during which it is being asserted that the patient
                # is/was/will be taking the medication (or was not taking, when the
                # MedicationStatement.taken element is No).
                StructField(
                    "effectivePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The date when the medication statement was asserted by the information source.
                StructField(
                    "dateAsserted",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The person or organization that provided the information about the taking of
                # this medication. Note: Use derivedFrom when a MedicationStatement is derived
                # from other resources, e.g. Claim or MedicationRequest.
                StructField(
                    "informationSource",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Allows linking the MedicationStatement to the underlying MedicationRequest, or
                # to other information that supports or is used to derive the
                # MedicationStatement.
                StructField(
                    "derivedFrom",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A reason for why the medication is being/was taken.
                StructField(
                    "reasonCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Condition or observation that supports why the medication is being/was taken.
                StructField(
                    "reasonReference",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Provides extra information about the medication statement that is not conveyed
                # by the other attributes.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Indicates how the medication is/was or should be taken by the patient.
                StructField(
                    "dosage",
                    ArrayType(
                        DosageSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
