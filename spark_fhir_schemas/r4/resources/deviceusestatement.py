from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DeviceUseStatement:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A record of a device being used by a patient where the record is the result of
        a report from the patient or another clinician.


        resourceType: This is a DeviceUseStatement resource

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

        identifier: An external identifier for this statement such as an IRI.

        basedOn: A plan, proposal or order that is fulfilled in whole or in part by this
            DeviceUseStatement.

        status: A code representing the patient or other source's judgment about the state of
            the device used that this statement is about.  Generally this will be active
            or completed.

        subject: The patient who used the device.

        derivedFrom: Allows linking the DeviceUseStatement to the underlying Request, or to other
            information that supports or is used to derive the DeviceUseStatement.

        timingTiming: How often the device was used.

        timingPeriod: How often the device was used.

        timingDateTime: How often the device was used.

        recordedOn: The time at which the statement was made/recorded.

        source: Who reported the device was being used by the patient.

        device: The details of the device used.

        reasonCode: Reason or justification for the use of the device.

        reasonReference: Indicates another resource whose existence justifies this DeviceUseStatement.

        bodySite: Indicates the anotomic location on the subject's body where the device was
            used ( i.e. the target).

        note: Details about the device statement that were not represented at all or
            sufficiently in one of the attributes provided in a class. These may include
            for example a comment, an instruction, or a note associated with the
            statement.

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
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a DeviceUseStatement resource
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
                # An external identifier for this statement such as an IRI.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # A plan, proposal or order that is fulfilled in whole or in part by this
                # DeviceUseStatement.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A code representing the patient or other source's judgment about the state of
                # the device used that this statement is about.  Generally this will be active
                # or completed.
                StructField("status", StringType(), True),
                # The patient who used the device.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # Allows linking the DeviceUseStatement to the underlying Request, or to other
                # information that supports or is used to derive the DeviceUseStatement.
                StructField(
                    "derivedFrom",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # How often the device was used.
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # How often the device was used.
                StructField(
                    "timingPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # How often the device was used.
                StructField("timingDateTime", StringType(), True),
                # The time at which the statement was made/recorded.
                StructField(
                    "recordedOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Who reported the device was being used by the patient.
                StructField(
                    "source", Reference.get_schema(recursion_depth + 1), True
                ),
                # The details of the device used.
                StructField(
                    "device", Reference.get_schema(recursion_depth + 1), True
                ),
                # Reason or justification for the use of the device.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource whose existence justifies this DeviceUseStatement.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the anotomic location on the subject's body where the device was
                # used ( i.e. the target).
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Details about the device statement that were not represented at all or
                # sufficiently in one of the attributes provided in a class. These may include
                # for example a comment, an instruction, or a note associated with the
                # statement.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
