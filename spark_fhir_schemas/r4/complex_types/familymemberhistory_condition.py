from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class FamilyMemberHistory_Condition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Significant health conditions for a person related to the patient relevant in
        the context of care for the patient.


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

        code: The actual condition specified. Could be a coded condition (like MI or
            Diabetes) or a less specific string like 'cancer' depending on how much is
            known about the condition and the capabilities of the creating system.

        outcome: Indicates what happened following the condition.  If the condition resulted in
            death, deceased date is captured on the relation.

        contributedToDeath: This condition contributed to the cause of death of the related person. If
            contributedToDeath is not populated, then it is unknown.

        onsetAge: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        onsetRange: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        onsetPeriod: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        onsetString: Either the age of onset, range of approximate age or descriptive string can be
            recorded.  For conditions with multiple occurrences, this describes the first
            known occurrence.

        note: An area where general notes can be placed about this specific condition.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The actual condition specified. Could be a coded condition (like MI or
                # Diabetes) or a less specific string like 'cancer' depending on how much is
                # known about the condition and the capabilities of the creating system.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates what happened following the condition.  If the condition resulted in
                # death, deceased date is captured on the relation.
                StructField(
                    "outcome", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # This condition contributed to the cause of death of the related person. If
                # contributedToDeath is not populated, then it is unknown.
                StructField("contributedToDeath", BooleanType(), True),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField(
                    "onsetAge", Age.get_schema(recursion_depth + 1), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField(
                    "onsetRange", Range.get_schema(recursion_depth + 1), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField(
                    "onsetPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # Either the age of onset, range of approximate age or descriptive string can be
                # recorded.  For conditions with multiple occurrences, this describes the first
                # known occurrence.
                StructField("onsetString", StringType(), True),
                # An area where general notes can be placed about this specific condition.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
