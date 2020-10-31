from typing import List
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class EvidenceVariable_CharacteristicSchema:
    """
    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_recursion_depth: int = 4,
        recursion_depth: int = 0,
        recursion_list: List[str] = []
    ) -> Union[StructType, DataType]:
        """
        The EvidenceVariable resource describes a "PICO" element that knowledge
        (evidence, assertion, recommendation) is about.


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

        description: A short, natural language description of the characteristic that could be used
            to communicate the criteria to an end-user.

        definitionReference: Define members of the evidence element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionCanonical: Define members of the evidence element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionCodeableConcept: Define members of the evidence element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionExpression: Define members of the evidence element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionDataRequirement: Define members of the evidence element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionTriggerDefinition: Define members of the evidence element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        usageContext: Use UsageContext to define the members of the population, such as Age Ranges,
            Genders, Settings.

        exclude: When true, members with this characteristic are excluded from the element.

        participantEffectiveDateTime: Indicates what effective period the study covers.

        participantEffectivePeriod: Indicates what effective period the study covers.

        participantEffectiveDuration: Indicates what effective period the study covers.

        participantEffectiveTiming: Indicates what effective period the study covers.

        timeFromStart: Indicates duration from the participant's study entry.

        groupMeasure: Indicates how elements are aggregated within the study effective period.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.expression import ExpressionSchema
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirementSchema
        from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinitionSchema
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        from spark_fhir_schemas.r4.complex_types.timing import TimingSchema
        if recursion_list.count(
            "EvidenceVariable_Characteristic"
        ) >= 2 or recursion_depth >= max_recursion_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_recursion_list: List[str] = recursion_list + [
            "EvidenceVariable_Characteristic"
        ]
        schema = StructType(
            [
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # A short, natural language description of the characteristic that could be used
                # to communicate the criteria to an end-user.
                StructField("description", StringType(), True),
                # Define members of the evidence element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionReference",
                    ReferenceSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Define members of the evidence element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField("definitionCanonical", StringType(), True),
                # Define members of the evidence element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Define members of the evidence element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionExpression",
                    ExpressionSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Define members of the evidence element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionDataRequirement",
                    DataRequirementSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Define members of the evidence element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionTriggerDefinition",
                    TriggerDefinitionSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Use UsageContext to define the members of the population, such as Age Ranges,
                # Genders, Settings.
                StructField(
                    "usageContext",
                    ArrayType(
                        UsageContextSchema.get_schema(
                            max_recursion_depth=max_recursion_depth,
                            recursion_depth=recursion_depth + 1,
                            recursion_list=my_recursion_list
                        )
                    ), True
                ),
                # When true, members with this characteristic are excluded from the element.
                StructField("exclude", BooleanType(), True),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveDateTime", StringType(), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectivePeriod",
                    PeriodSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveDuration",
                    DurationSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveTiming",
                    TimingSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates duration from the participant's study entry.
                StructField(
                    "timeFromStart",
                    DurationSchema.get_schema(
                        max_recursion_depth=max_recursion_depth,
                        recursion_depth=recursion_depth + 1,
                        recursion_list=my_recursion_list
                    ), True
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField("groupMeasure", StringType(), True),
            ]
        )
        return schema
