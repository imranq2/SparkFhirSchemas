from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Procedure:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An action that is or was performed on or for a patient. This can be a physical
        intervention like an operation, or less invasive like long term services,
        counseling, or hypnotherapy.


        resourceType: This is a Procedure resource

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

        identifier: Business identifiers assigned to this procedure by the performer or other
            systems which remain constant as the resource is updated and is propagated
            from server to server.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, order set or other
            definition that is adhered to in whole or in part by this Procedure.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, order set or
            other definition that is adhered to in whole or in part by this Procedure.

        basedOn: A reference to a resource that contains details of the request for this
            procedure.

        partOf: A larger event of which this particular procedure is a component or step.

        status: A code specifying the state of the procedure. Generally, this will be the in-
            progress or completed state.

        statusReason: Captures the reason for the current state of the procedure.

        category: A code that classifies the procedure for searching, sorting and display
            purposes (e.g. "Surgical Procedure").

        code: The specific procedure that is performed. Use text if the exact nature of the
            procedure cannot be coded (e.g. "Laparoscopic Appendectomy").

        subject: The person, animal or group on which the procedure was performed.

        encounter: The Encounter during which this Procedure was created or performed or to which
            the creation of this record is tightly associated.

        performedDateTime: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedPeriod: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedString: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedAge: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedRange: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        recorder: Individual who recorded the record and takes responsibility for its content.

        asserter: Individual who is making the procedure statement.

        performer: Limited to "real" people rather than equipment.

        location: The location where the procedure actually happened.  E.g. a newborn at home, a
            tracheostomy at a restaurant.

        reasonCode: The coded reason why the procedure was performed. This may be a coded entity
            of some type, or may simply be present as text.

        reasonReference: The justification of why the procedure was performed.

        bodySite: Detailed and structured anatomical location information. Multiple locations
            are allowed - e.g. multiple punch biopsies of a lesion.

        outcome: The outcome of the procedure - did it resolve the reasons for the procedure
            being performed?

        report: This could be a histology result, pathology report, surgical report, etc.

        complication: Any complications that occurred during the procedure, or in the immediate
            post-performance period. These are generally tracked separately from the
            notes, which will typically describe the procedure itself rather than any
            'post procedure' issues.

        complicationDetail: Any complications that occurred during the procedure, or in the immediate
            post-performance period.

        followUp: If the procedure required specific follow up - e.g. removal of sutures. The
            follow up may be represented as a simple note or could potentially be more
            complex, in which case the CarePlan resource can be used.

        note: Any other notes and comments about the procedure.

        focalDevice: A device that is implanted, removed or otherwise manipulated (calibration,
            battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a
            focal portion of the Procedure.

        usedReference: Identifies medications, devices and any other substance used as part of the
            procedure.

        usedCode: Identifies coded items that were used as part of the procedure.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.procedure_performer import Procedure_Performer
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.procedure_focaldevice import Procedure_FocalDevice
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Procedure resource
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
                # Business identifiers assigned to this procedure by the performer or other
                # systems which remain constant as the resource is updated and is propagated
                # from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, order set or other
                # definition that is adhered to in whole or in part by this Procedure.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline, order set or
                # other definition that is adhered to in whole or in part by this Procedure.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # A reference to a resource that contains details of the request for this
                # procedure.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A larger event of which this particular procedure is a component or step.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A code specifying the state of the procedure. Generally, this will be the in-
                # progress or completed state.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Captures the reason for the current state of the procedure.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A code that classifies the procedure for searching, sorting and display
                # purposes (e.g. "Surgical Procedure").
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The specific procedure that is performed. Use text if the exact nature of the
                # procedure cannot be coded (e.g. "Laparoscopic Appendectomy").
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The person, animal or group on which the procedure was performed.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Encounter during which this Procedure was created or performed or to which
                # the creation of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField("performedDateTime", StringType(), True),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField(
                    "performedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField("performedString", StringType(), True),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField(
                    "performedAge", Age.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField(
                    "performedRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                # Individual who recorded the record and takes responsibility for its content.
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                # Individual who is making the procedure statement.
                StructField(
                    "asserter", Reference.get_schema(recursion_depth + 1), True
                ),
                # Limited to "real" people rather than equipment.
                StructField(
                    "performer",
                    ArrayType(
                        Procedure_Performer.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The location where the procedure actually happened.  E.g. a newborn at home, a
                # tracheostomy at a restaurant.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # The coded reason why the procedure was performed. This may be a coded entity
                # of some type, or may simply be present as text.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The justification of why the procedure was performed.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Detailed and structured anatomical location information. Multiple locations
                # are allowed - e.g. multiple punch biopsies of a lesion.
                StructField(
                    "bodySite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The outcome of the procedure - did it resolve the reasons for the procedure
                # being performed?
                StructField(
                    "outcome", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # This could be a histology result, pathology report, surgical report, etc.
                StructField(
                    "report",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Any complications that occurred during the procedure, or in the immediate
                # post-performance period. These are generally tracked separately from the
                # notes, which will typically describe the procedure itself rather than any
                # 'post procedure' issues.
                StructField(
                    "complication",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Any complications that occurred during the procedure, or in the immediate
                # post-performance period.
                StructField(
                    "complicationDetail",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # If the procedure required specific follow up - e.g. removal of sutures. The
                # follow up may be represented as a simple note or could potentially be more
                # complex, in which case the CarePlan resource can be used.
                StructField(
                    "followUp",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Any other notes and comments about the procedure.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # A device that is implanted, removed or otherwise manipulated (calibration,
                # battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a
                # focal portion of the Procedure.
                StructField(
                    "focalDevice",
                    ArrayType(
                        Procedure_FocalDevice.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies medications, devices and any other substance used as part of the
                # procedure.
                StructField(
                    "usedReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies coded items that were used as part of the procedure.
                StructField(
                    "usedCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
