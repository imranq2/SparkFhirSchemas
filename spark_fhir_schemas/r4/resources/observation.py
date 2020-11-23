from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ObservationSchema:
    """
    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
        """
        Measurements and simple assertions made about a patient, device or other
        subject.


        resourceType: This is a Observation resource

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

        identifier: A unique identifier assigned to this observation.

        basedOn: A plan, proposal or order that is fulfilled in whole or in part by this event.
            For example, a MedicationRequest may require a patient to have laboratory test
            performed before  it is dispensed.

        partOf: A larger event of which this particular Observation is a component or step.
            For example,  an observation as part of a procedure.

        status: The status of the result value.

        category: A code that classifies the general type of observation being made.

        code: Describes what was observed. Sometimes this is called the observation "name".

        subject: The patient, or group of patients, location, or device this observation is
            about and into whose record the observation is placed. If the actual focus of
            the observation is different from the subject (or a sample of, part, or region
            of the subject), the `focus` element or the `code` itself specifies the actual
            focus of the observation.

        focus: The actual focus of an observation when it is not the patient of record
            representing something or someone associated with the patient such as a
            spouse, parent, fetus, or donor. For example, fetus observations in a mother's
            record.  The focus of an observation could also be an existing condition,  an
            intervention, the subject's diet,  another observation of the subject,  or a
            body structure such as tumor or implanted device.   An example use case would
            be using the Observation resource to capture whether the mother is trained to
            change her child's tracheostomy tube. In this example, the child is the
            patient of record and the mother is the focus.

        encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
            during which this observation is made.

        effectiveDateTime: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        effectivePeriod: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        effectiveTiming: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        effectiveInstant: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        issued: The date and time this version of the observation was made available to
            providers, typically after the results have been reviewed and verified.

        performer: Who was responsible for asserting the observed value as "true".

        valueQuantity: The information determined as a result of making the observation, if the
            information has a simple value.

        valueCodeableConcept: The information determined as a result of making the observation, if the
            information has a simple value.

        valueString: The information determined as a result of making the observation, if the
            information has a simple value.

        valueBoolean: The information determined as a result of making the observation, if the
            information has a simple value.

        valueInteger: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRange: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRatio: The information determined as a result of making the observation, if the
            information has a simple value.

        valueSampledData: The information determined as a result of making the observation, if the
            information has a simple value.

        valueTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valueDateTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valuePeriod: The information determined as a result of making the observation, if the
            information has a simple value.

        dataAbsentReason: Provides a reason why the expected value in the element Observation.value[x]
            is missing.

        interpretation: A categorical assessment of an observation value.  For example, high, low,
            normal.

        note: Comments about the observation or the results.

        bodySite: Indicates the site on the subject's body where the observation was made (i.e.
            the target site).

        method: Indicates the mechanism used to perform the observation.

        specimen: The specimen that was used when this observation was made.

        device: The device used to generate the observation data.

        referenceRange: Guidance on how to interpret the value by comparison to a normal or
            recommended range.  Multiple reference ranges are interpreted as an "OR".   In
            other words, to represent two distinct target populations, two
            `referenceRange` elements would be used.

        hasMember: This observation is a group observation (e.g. a battery, a panel of tests, a
            set of vital sign measurements) that includes the target as a member of the
            group.

        derivedFrom: The target resource that represents a measurement from which this observation
            value is derived. For example, a calculated anion gap or a fetal measurement
            based on an ultrasound image.

        component: Some observations have multiple component observations.  These component
            observations are expressed as separate code value pairs that share the same
            attributes.  Examples include systolic and diastolic component observations
            for blood pressure measurement and multiple component observations for
            genetics observations.

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
        from spark_fhir_schemas.r4.complex_types.timing import TimingSchema
        from spark_fhir_schemas.r4.simple_types.instant import instantSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.ratio import RatioSchema
        from spark_fhir_schemas.r4.complex_types.sampleddata import SampledDataSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.r4.complex_types.observation_referencerange import Observation_ReferenceRangeSchema
        from spark_fhir_schemas.r4.complex_types.observation_component import Observation_ComponentSchema
        if (
            max_recursion_limit
            and nesting_list.count("Observation") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Observation"]
        schema = StructType(
            [
                # This is a Observation resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
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
                        max_recursion_limit=max_recursion_limit
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
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
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
                        max_recursion_limit=max_recursion_limit
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
                            max_recursion_limit=max_recursion_limit
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
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # A unique identifier assigned to this observation.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # A plan, proposal or order that is fulfilled in whole or in part by this event.
                # For example, a MedicationRequest may require a patient to have laboratory test
                # performed before  it is dispensed.
                StructField(
                    "basedOn",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # A larger event of which this particular Observation is a component or step.
                # For example,  an observation as part of a procedure.
                StructField(
                    "partOf",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The status of the result value.
                StructField("status", StringType(), True),
                # A code that classifies the general type of observation being made.
                StructField(
                    "category",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Describes what was observed. Sometimes this is called the observation "name".
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The patient, or group of patients, location, or device this observation is
                # about and into whose record the observation is placed. If the actual focus of
                # the observation is different from the subject (or a sample of, part, or region
                # of the subject), the `focus` element or the `code` itself specifies the actual
                # focus of the observation.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual focus of an observation when it is not the patient of record
                # representing something or someone associated with the patient such as a
                # spouse, parent, fetus, or donor. For example, fetus observations in a mother's
                # record.  The focus of an observation could also be an existing condition,  an
                # intervention, the subject's diet,  another observation of the subject,  or a
                # body structure such as tumor or implanted device.   An example use case would
                # be using the Observation resource to capture whether the mother is trained to
                # change her child's tracheostomy tube. In this example, the child is the
                # patient of record and the mother is the focus.
                StructField(
                    "focus",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The healthcare event  (e.g. a patient and healthcare provider interaction)
                # during which this observation is made.
                StructField(
                    "encounter",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField("effectiveDateTime", StringType(), True),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField(
                    "effectivePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField(
                    "effectiveTiming",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField("effectiveInstant", StringType(), True),
                # The date and time this version of the observation was made available to
                # providers, typically after the results have been reviewed and verified.
                StructField(
                    "issued",
                    instantSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Who was responsible for asserting the observed value as "true".
                StructField(
                    "performer",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueString", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueBoolean", BooleanType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueInteger", IntegerType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRatio",
                    RatioSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueSampledData",
                    SampledDataSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueDateTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valuePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Provides a reason why the expected value in the element Observation.value[x]
                # is missing.
                StructField(
                    "dataAbsentReason",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # A categorical assessment of an observation value.  For example, high, low,
                # normal.
                StructField(
                    "interpretation",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Comments about the observation or the results.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Indicates the site on the subject's body where the observation was made (i.e.
                # the target site).
                StructField(
                    "bodySite",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Indicates the mechanism used to perform the observation.
                StructField(
                    "method",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The specimen that was used when this observation was made.
                StructField(
                    "specimen",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The device used to generate the observation data.
                StructField(
                    "device",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Guidance on how to interpret the value by comparison to a normal or
                # recommended range.  Multiple reference ranges are interpreted as an "OR".   In
                # other words, to represent two distinct target populations, two
                # `referenceRange` elements would be used.
                StructField(
                    "referenceRange",
                    ArrayType(
                        Observation_ReferenceRangeSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # This observation is a group observation (e.g. a battery, a panel of tests, a
                # set of vital sign measurements) that includes the target as a member of the
                # group.
                StructField(
                    "hasMember",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # The target resource that represents a measurement from which this observation
                # value is derived. For example, a calculated anion gap or a fetal measurement
                # based on an ultrasound image.
                StructField(
                    "derivedFrom",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Some observations have multiple component observations.  These component
                # observations are expressed as separate code value pairs that share the same
                # attributes.  Examples include systolic and diastolic component observations
                # for blood pressure measurement and multiple component observations for
                # genetics observations.
                StructField(
                    "component",
                    ArrayType(
                        Observation_ComponentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
            ]
        )
        return schema
