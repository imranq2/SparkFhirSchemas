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
class StructureMap_SourceSchema:
    """
    A Map of relationships between 2 structures that can be used to transform
    data.
    """
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A Map of relationships between 2 structures that can be used to transform
        data.


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

        context: Type or variable this rule applies to.

        min: Specified minimum cardinality for the element. This is optional; if present,
            it acts an implicit check on the input content.

        max: Specified maximum cardinality for the element - a number or a "*". This is
            optional; if present, it acts an implicit check on the input content (* just
            serves as documentation; it's the default value).

        type: Specified type for the element. This works as a condition on the mapping - use
            for polymorphic elements.

        defaultValueBase64Binary: A value to use if there is no existing value in the source object.

        defaultValueBoolean: A value to use if there is no existing value in the source object.

        defaultValueCanonical: A value to use if there is no existing value in the source object.

        defaultValueCode: A value to use if there is no existing value in the source object.

        defaultValueDate: A value to use if there is no existing value in the source object.

        defaultValueDateTime: A value to use if there is no existing value in the source object.

        defaultValueDecimal: A value to use if there is no existing value in the source object.

        defaultValueId: A value to use if there is no existing value in the source object.

        defaultValueInstant: A value to use if there is no existing value in the source object.

        defaultValueInteger: A value to use if there is no existing value in the source object.

        defaultValueMarkdown: A value to use if there is no existing value in the source object.

        defaultValueOid: A value to use if there is no existing value in the source object.

        defaultValuePositiveInt: A value to use if there is no existing value in the source object.

        defaultValueString: A value to use if there is no existing value in the source object.

        defaultValueTime: A value to use if there is no existing value in the source object.

        defaultValueUnsignedInt: A value to use if there is no existing value in the source object.

        defaultValueUri: A value to use if there is no existing value in the source object.

        defaultValueUrl: A value to use if there is no existing value in the source object.

        defaultValueUuid: A value to use if there is no existing value in the source object.

        defaultValueAddress: A value to use if there is no existing value in the source object.

        defaultValueAge: A value to use if there is no existing value in the source object.

        defaultValueAnnotation: A value to use if there is no existing value in the source object.

        defaultValueAttachment: A value to use if there is no existing value in the source object.

        defaultValueCodeableConcept: A value to use if there is no existing value in the source object.

        defaultValueCoding: A value to use if there is no existing value in the source object.

        defaultValueContactPoint: A value to use if there is no existing value in the source object.

        defaultValueCount: A value to use if there is no existing value in the source object.

        defaultValueDistance: A value to use if there is no existing value in the source object.

        defaultValueDuration: A value to use if there is no existing value in the source object.

        defaultValueHumanName: A value to use if there is no existing value in the source object.

        defaultValueIdentifier: A value to use if there is no existing value in the source object.

        defaultValueMoney: A value to use if there is no existing value in the source object.

        defaultValuePeriod: A value to use if there is no existing value in the source object.

        defaultValueQuantity: A value to use if there is no existing value in the source object.

        defaultValueRange: A value to use if there is no existing value in the source object.

        defaultValueRatio: A value to use if there is no existing value in the source object.

        defaultValueReference: A value to use if there is no existing value in the source object.

        defaultValueSampledData: A value to use if there is no existing value in the source object.

        defaultValueSignature: A value to use if there is no existing value in the source object.

        defaultValueTiming: A value to use if there is no existing value in the source object.

        defaultValueContactDetail: A value to use if there is no existing value in the source object.

        defaultValueContributor: A value to use if there is no existing value in the source object.

        defaultValueDataRequirement: A value to use if there is no existing value in the source object.

        defaultValueExpression: A value to use if there is no existing value in the source object.

        defaultValueParameterDefinition: A value to use if there is no existing value in the source object.

        defaultValueRelatedArtifact: A value to use if there is no existing value in the source object.

        defaultValueTriggerDefinition: A value to use if there is no existing value in the source object.

        defaultValueUsageContext: A value to use if there is no existing value in the source object.

        defaultValueDosage: A value to use if there is no existing value in the source object.

        defaultValueMeta: A value to use if there is no existing value in the source object.

        element: Optional field for this source.

        listMode: How to handle the list mode for this element.

        variable: Named context for field, if a field is specified.

        condition: FHIRPath expression  - must be true or the rule does not apply.

        check: FHIRPath expression  - must be true or the mapping engine throws an error
            instead of completing.

        logMessage: A FHIRPath expression which specifies a message to put in the transform log
            when content matching the source rule is found.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.id import idSchema
        from spark_fhir_schemas.r4.simple_types.integer import integerSchema
        from spark_fhir_schemas.r4.complex_types.address import AddressSchema
        from spark_fhir_schemas.r4.complex_types.age import AgeSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.r4.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPointSchema
        from spark_fhir_schemas.r4.complex_types.count import CountSchema
        from spark_fhir_schemas.r4.complex_types.distance import DistanceSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        from spark_fhir_schemas.r4.complex_types.humanname import HumanNameSchema
        from spark_fhir_schemas.r4.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.r4.complex_types.money import MoneySchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.complex_types.range import RangeSchema
        from spark_fhir_schemas.r4.complex_types.ratio import RatioSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.sampleddata import SampledDataSchema
        from spark_fhir_schemas.r4.complex_types.signature import SignatureSchema
        from spark_fhir_schemas.r4.complex_types.timing import TimingSchema
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.r4.complex_types.contributor import ContributorSchema
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirementSchema
        from spark_fhir_schemas.r4.complex_types.expression import ExpressionSchema
        from spark_fhir_schemas.r4.complex_types.parameterdefinition import ParameterDefinitionSchema
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifactSchema
        from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinitionSchema
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.r4.complex_types.dosage import DosageSchema
        from spark_fhir_schemas.r4.complex_types.meta import MetaSchema
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
                # Type or variable this rule applies to.
                StructField(
                    "context", idSchema.get_schema(recursion_depth + 1), True
                ),
                # Specified minimum cardinality for the element. This is optional; if present,
                # it acts an implicit check on the input content.
                StructField(
                    "min", integerSchema.get_schema(recursion_depth + 1), True
                ),
                # Specified maximum cardinality for the element - a number or a "*". This is
                # optional; if present, it acts an implicit check on the input content (* just
                # serves as documentation; it's the default value).
                StructField("max", StringType(), True),
                # Specified type for the element. This works as a condition on the mapping - use
                # for polymorphic elements.
                StructField("type", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueBase64Binary", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueBoolean", BooleanType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueCanonical", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueCode", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDate", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDateTime", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDecimal", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueId", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueInstant", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueInteger", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueMarkdown", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueOid", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValuePositiveInt", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueString", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueTime", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUnsignedInt", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUri", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUrl", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUuid", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAddress",
                    AddressSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAge",
                    AgeSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAnnotation",
                    AnnotationSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAttachment",
                    AttachmentSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCodeableConcept",
                    CodeableConceptSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCoding",
                    CodingSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContactPoint",
                    ContactPointSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCount",
                    CountSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDistance",
                    DistanceSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDuration",
                    DurationSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueHumanName",
                    HumanNameSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueIdentifier",
                    IdentifierSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueMoney",
                    MoneySchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValuePeriod",
                    PeriodSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueQuantity",
                    QuantitySchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRange",
                    RangeSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRatio",
                    RatioSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueReference",
                    ReferenceSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueSampledData",
                    SampledDataSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueSignature",
                    SignatureSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueTiming",
                    TimingSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContactDetail",
                    ContactDetailSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContributor",
                    ContributorSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDataRequirement",
                    DataRequirementSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueExpression",
                    ExpressionSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueParameterDefinition",
                    ParameterDefinitionSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRelatedArtifact",
                    RelatedArtifactSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueTriggerDefinition",
                    TriggerDefinitionSchema.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueUsageContext",
                    UsageContextSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDosage",
                    DosageSchema.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueMeta",
                    MetaSchema.get_schema(recursion_depth + 1), True
                ),
                # Optional field for this source.
                StructField("element", StringType(), True),
                # How to handle the list mode for this element.
                StructField("listMode", StringType(), True),
                # Named context for field, if a field is specified.
                StructField(
                    "variable", idSchema.get_schema(recursion_depth + 1), True
                ),
                # FHIRPath expression  - must be true or the rule does not apply.
                StructField("condition", StringType(), True),
                # FHIRPath expression  - must be true or the mapping engine throws an error
                # instead of completing.
                StructField("check", StringType(), True),
                # A FHIRPath expression which specifies a message to put in the transform log
                # when content matching the source rule is found.
                StructField("logMessage", StringType(), True),
            ]
        )
        return schema
