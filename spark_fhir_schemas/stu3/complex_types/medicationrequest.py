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
class MedicationRequestSchema:
    """
    An order or request for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
    to generalize the use across inpatient and outpatient settings, including care
    plans, etc., and to harmonize with workflow patterns.
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
        An order or request for both supply of the medication and the instructions for
        administration of the medication to a patient. The resource is called
        "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
        to generalize the use across inpatient and outpatient settings, including care
        plans, etc., and to harmonize with workflow patterns.


        resourceType: This is a MedicationRequest resource

        identifier: This records identifiers associated with this medication request that are
            defined by business processes and/or used to refer to it when a direct URL
            reference to the resource itself is not appropriate. For example a re-
            imbursement system might issue its own id for each prescription that is
            created.  This is particularly important where FHIR only provides part of an
            entire workflow process where records must be tracked through an entire
            system.

        definition: Protocol or definition followed by this request.

        basedOn: A plan or request that is fulfilled in whole or in part by this medication
            request.

        groupIdentifier: A shared identifier common to all requests that were authorized more or less
            simultaneously by a single author, representing the identifier of the
            requisition or prescription.

        status: A code specifying the current state of the order.  Generally this will be
            active or completed state.

        intent: Whether the request is a proposal, plan, or an original order.

        category: Indicates the type of medication order and where the medication is expected to
            be consumed or administered.

        priority: Indicates how quickly the Medication Request should be addressed with respect
            to other requests.

        medicationCodeableConcept: Identifies the medication being requested. This is a link to a resource that
            represents the medication which may be the details of the medication or simply
            an attribute carrying a code that identifies the medication from a known list
            of medications.

        medicationReference: Identifies the medication being requested. This is a link to a resource that
            represents the medication which may be the details of the medication or simply
            an attribute carrying a code that identifies the medication from a known list
            of medications.

        subject: A link to a resource representing the person or set of individuals to whom the
            medication will be given.

        context: A link to an encounter, or episode of care, that identifies the particular
            occurrence or set occurrences of contact between patient and health care
            provider.

        supportingInformation: Include additional information (for example, patient height and weight) that
            supports the ordering of the medication.

        authoredOn: The date (and perhaps time) when the prescription was initially written or
            authored on.

        requester: The individual, organization or device that initiated the request and has
            responsibility for its activation.

        recorder: The person who entered the order on behalf of another individual for example
            in the case of a verbal or a telephone order.

        reasonCode: The reason or the indication for ordering the medication.

        reasonReference: Condition or observation that supports why the medication was ordered.

        note: Extra information about the prescription that could not be conveyed by the
            other attributes.

        dosageInstruction: Indicates how the medication is to be used by the patient.

        dispenseRequest: Indicates the specific details for the dispense or medication supply part of a
            medication request (also known as a Medication Prescription or Medication
            Order).  Note that this information is not always sent with the order.  There
            may be in some settings (e.g. hospitals) institutional or system support for
            completing the dispense details in the pharmacy department.

        substitution: Indicates whether or not substitution can or should be part of the dispense.
            In some cases substitution must happen, in other cases substitution must not
            happen. This block explains the prescriber's intent. If nothing is specified
            substitution may be done.

        priorPrescription: A link to a resource representing an earlier order related order or
            prescription.

        detectedIssue: Indicates an actual or potential clinical issue with or between one or more
            active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
            duplicate therapy, dosage alert etc.

        eventHistory: Links to Provenance records for past versions of this resource or fulfilling
            request or event resources that identify key state transitions or updates that
            are likely to be relevant to a user looking at the current version of the
            resource.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.medicationrequest_requester import MedicationRequest_RequesterSchema
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.stu3.complex_types.dosage import DosageSchema
        from spark_fhir_schemas.stu3.complex_types.medicationrequest_dispenserequest import MedicationRequest_DispenseRequestSchema
        from spark_fhir_schemas.stu3.complex_types.medicationrequest_substitution import MedicationRequest_SubstitutionSchema
        if (
            max_recursion_limit
            and nesting_list.count("MedicationRequest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationRequest"]
        schema = StructType(
            [
                # This is a MedicationRequest resource
                StructField("resourceType", StringType(), True),
                # This records identifiers associated with this medication request that are
                # defined by business processes and/or used to refer to it when a direct URL
                # reference to the resource itself is not appropriate. For example a re-
                # imbursement system might issue its own id for each prescription that is
                # created.  This is particularly important where FHIR only provides part of an
                # entire workflow process where records must be tracked through an entire
                # system.
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
                # Protocol or definition followed by this request.
                StructField(
                    "definition",
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
                # A plan or request that is fulfilled in whole or in part by this medication
                # request.
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
                # A shared identifier common to all requests that were authorized more or less
                # simultaneously by a single author, representing the identifier of the
                # requisition or prescription.
                StructField(
                    "groupIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A code specifying the current state of the order.  Generally this will be
                # active or completed state.
                StructField("status", StringType(), True),
                # Whether the request is a proposal, plan, or an original order.
                StructField("intent", StringType(), True),
                # Indicates the type of medication order and where the medication is expected to
                # be consumed or administered.
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
                # Indicates how quickly the Medication Request should be addressed with respect
                # to other requests.
                StructField("priority", StringType(), True),
                # Identifies the medication being requested. This is a link to a resource that
                # represents the medication which may be the details of the medication or simply
                # an attribute carrying a code that identifies the medication from a known list
                # of medications.
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
                # Identifies the medication being requested. This is a link to a resource that
                # represents the medication which may be the details of the medication or simply
                # an attribute carrying a code that identifies the medication from a known list
                # of medications.
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
                # A link to a resource representing the person or set of individuals to whom the
                # medication will be given.
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
                # A link to an encounter, or episode of care, that identifies the particular
                # occurrence or set occurrences of contact between patient and health care
                # provider.
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
                # Include additional information (for example, patient height and weight) that
                # supports the ordering of the medication.
                StructField(
                    "supportingInformation",
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
                # The date (and perhaps time) when the prescription was initially written or
                # authored on.
                StructField("authoredOn", StringType(), True),
                # The individual, organization or device that initiated the request and has
                # responsibility for its activation.
                StructField(
                    "requester",
                    MedicationRequest_RequesterSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The person who entered the order on behalf of another individual for example
                # in the case of a verbal or a telephone order.
                StructField(
                    "recorder",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The reason or the indication for ordering the medication.
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
                # Condition or observation that supports why the medication was ordered.
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
                # Extra information about the prescription that could not be conveyed by the
                # other attributes.
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
                # Indicates how the medication is to be used by the patient.
                StructField(
                    "dosageInstruction",
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
                # Indicates the specific details for the dispense or medication supply part of a
                # medication request (also known as a Medication Prescription or Medication
                # Order).  Note that this information is not always sent with the order.  There
                # may be in some settings (e.g. hospitals) institutional or system support for
                # completing the dispense details in the pharmacy department.
                StructField(
                    "dispenseRequest",
                    MedicationRequest_DispenseRequestSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates whether or not substitution can or should be part of the dispense.
                # In some cases substitution must happen, in other cases substitution must not
                # happen. This block explains the prescriber's intent. If nothing is specified
                # substitution may be done.
                StructField(
                    "substitution",
                    MedicationRequest_SubstitutionSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A link to a resource representing an earlier order related order or
                # prescription.
                StructField(
                    "priorPrescription",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates an actual or potential clinical issue with or between one or more
                # active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
                # duplicate therapy, dosage alert etc.
                StructField(
                    "detectedIssue",
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
                # Links to Provenance records for past versions of this resource or fulfilling
                # request or event resources that identify key state transitions or updates that
                # are likely to be relevant to a user looking at the current version of the
                # resource.
                StructField(
                    "eventHistory",
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
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema