from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DocumentReference_ContextSchema:
    """
    A reference to a document of any kind for any purpose. Provides metadata about
    the document so that the document can be discovered and managed. The scope of
    a document is any seralized object with a mime-type, so includes formal
    patient centric documents (CDA), cliical notes, scanned paper, and non-patient
    specific documents like policy text.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A reference to a document of any kind for any purpose. Provides metadata about
        the document so that the document can be discovered and managed. The scope of
        a document is any seralized object with a mime-type, so includes formal
        patient centric documents (CDA), cliical notes, scanned paper, and non-patient
        specific documents like policy text.


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

        encounter: Describes the clinical encounter or type of care that the document content is
            associated with.

        event: This list of codes represents the main clinical acts, such as a colonoscopy or
            an appendectomy, being documented. In some cases, the event is inherent in the
            type Code, such as a "History and Physical Report" in which the procedure
            being documented is necessarily a "History and Physical" act.

        period: The time period over which the service that is described by the document was
            provided.

        facilityType: The kind of facility where the patient was seen.

        practiceSetting: This property may convey specifics about the practice setting where the
            content was created, often reflecting the clinical specialty.

        sourcePatientInfo: The Patient Information as known when the document was published. May be a
            reference to a version specific, or contained.

        related: Related identifiers or resources associated with the DocumentReference.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
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
                    ArrayType(ExtensionSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # Describes the clinical encounter or type of care that the document content is
                # associated with.
                StructField(
                    "encounter",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
                # This list of codes represents the main clinical acts, such as a colonoscopy or
                # an appendectomy, being documented. In some cases, the event is inherent in the
                # type Code, such as a "History and Physical Report" in which the procedure
                # being documented is necessarily a "History and Physical" act.
                StructField(
                    "event",
                    ArrayType(
                        CodeableConceptSchema.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The time period over which the service that is described by the document was
                # provided.
                StructField(
                    "period", PeriodSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # The kind of facility where the patient was seen.
                StructField(
                    "facilityType",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # This property may convey specifics about the practice setting where the
                # content was created, often reflecting the clinical specialty.
                StructField(
                    "practiceSetting",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # The Patient Information as known when the document was published. May be a
                # reference to a version specific, or contained.
                StructField(
                    "sourcePatientInfo",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # Related identifiers or resources associated with the DocumentReference.
                StructField(
                    "related",
                    ArrayType(ReferenceSchema.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
