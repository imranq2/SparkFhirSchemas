from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CarePlan_Activity:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes the intention of how one or more practitioners intend to deliver
        care for a particular patient, group or community for a period of time,
        possibly limited to care for a specific condition or set of conditions.


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

        outcomeCodeableConcept: Identifies the outcome at the point when the status of the activity is
            assessed.  For example, the outcome of an education activity could be patient
            understands (or not).

        outcomeReference: Details of the outcome or action resulting from the activity.  The reference
            to an "event" resource, such as Procedure or Encounter or Observation, is the
            result/outcome of the activity itself.  The activity can be conveyed using
            CarePlan.activity.detail OR using the CarePlan.activity.reference (a reference
            to a “request” resource).

        progress: Notes about the adherence/status/progress of the activity.

        reference: The details of the proposed activity represented in a specific resource.

        detail: A simple summary of a planned activity suitable for a general care plan system
            (e.g. form driven) that doesn't know about specific resources such as
            procedure etc.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.careplan_detail import CarePlan_Detail
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
                # Identifies the outcome at the point when the status of the activity is
                # assessed.  For example, the outcome of an education activity could be patient
                # understands (or not).
                StructField(
                    "outcomeCodeableConcept",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Details of the outcome or action resulting from the activity.  The reference
                # to an "event" resource, such as Procedure or Encounter or Observation, is the
                # result/outcome of the activity itself.  The activity can be conveyed using
                # CarePlan.activity.detail OR using the CarePlan.activity.reference (a reference
                # to a “request” resource).
                StructField(
                    "outcomeReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Notes about the adherence/status/progress of the activity.
                StructField(
                    "progress",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # The details of the proposed activity represented in a specific resource.
                StructField(
                    "reference", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # A simple summary of a planned activity suitable for a general care plan system
                # (e.g. form driven) that doesn't know about specific resources such as
                # procedure etc.
                StructField(
                    "detail", CarePlan_Detail.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
