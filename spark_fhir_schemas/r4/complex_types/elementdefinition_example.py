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
class ElementDefinition_ExampleSchema:
    """
    Captures constraints on each element within the resource, profile, or
    extension.
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
        Captures constraints on each element within the resource, profile, or
        extension.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        label: Describes the purpose of this example amoung the set of examples.

        valueBase64Binary: The actual value for the element, which must be one of the types allowed for
            this element.

        valueBoolean: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCanonical: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCode: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDate: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDateTime: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDecimal: The actual value for the element, which must be one of the types allowed for
            this element.

        valueId: The actual value for the element, which must be one of the types allowed for
            this element.

        valueInstant: The actual value for the element, which must be one of the types allowed for
            this element.

        valueInteger: The actual value for the element, which must be one of the types allowed for
            this element.

        valueMarkdown: The actual value for the element, which must be one of the types allowed for
            this element.

        valueOid: The actual value for the element, which must be one of the types allowed for
            this element.

        valuePositiveInt: The actual value for the element, which must be one of the types allowed for
            this element.

        valueString: The actual value for the element, which must be one of the types allowed for
            this element.

        valueTime: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUnsignedInt: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUri: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUrl: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUuid: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAddress: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAge: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAnnotation: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAttachment: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCodeableConcept: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCoding: The actual value for the element, which must be one of the types allowed for
            this element.

        valueContactPoint: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCount: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDistance: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDuration: The actual value for the element, which must be one of the types allowed for
            this element.

        valueHumanName: The actual value for the element, which must be one of the types allowed for
            this element.

        valueIdentifier: The actual value for the element, which must be one of the types allowed for
            this element.

        valueMoney: The actual value for the element, which must be one of the types allowed for
            this element.

        valuePeriod: The actual value for the element, which must be one of the types allowed for
            this element.

        valueQuantity: The actual value for the element, which must be one of the types allowed for
            this element.

        valueRange: The actual value for the element, which must be one of the types allowed for
            this element.

        valueRatio: The actual value for the element, which must be one of the types allowed for
            this element.

        valueReference: The actual value for the element, which must be one of the types allowed for
            this element.

        valueSampledData: The actual value for the element, which must be one of the types allowed for
            this element.

        valueSignature: The actual value for the element, which must be one of the types allowed for
            this element.

        valueTiming: The actual value for the element, which must be one of the types allowed for
            this element.

        valueContactDetail: The actual value for the element, which must be one of the types allowed for
            this element.

        valueContributor: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDataRequirement: The actual value for the element, which must be one of the types allowed for
            this element.

        valueExpression: The actual value for the element, which must be one of the types allowed for
            this element.

        valueParameterDefinition: The actual value for the element, which must be one of the types allowed for
            this element.

        valueRelatedArtifact: The actual value for the element, which must be one of the types allowed for
            this element.

        valueTriggerDefinition: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUsageContext: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDosage: The actual value for the element, which must be one of the types allowed for
            this element.

        valueMeta: The actual value for the element, which must be one of the types allowed for
            this element.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
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
        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition_Example") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ElementDefinition_Example"
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
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit
                        )
                    ), True
                ),
                # Describes the purpose of this example amoung the set of examples.
                StructField("label", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueBase64Binary", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueBoolean", BooleanType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueCanonical", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueCode", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueDate", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueDateTime", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueDecimal", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueId", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueInstant", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueInteger", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueMarkdown", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueOid", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valuePositiveInt", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueString", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueTime", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUnsignedInt", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUri", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUrl", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUuid", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAddress",
                    AddressSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAge",
                    AgeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAnnotation",
                    AnnotationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueCoding",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueContactPoint",
                    ContactPointSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueCount",
                    CountSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDistance",
                    DistanceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDuration",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueHumanName",
                    HumanNameSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueMoney",
                    MoneySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valuePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueRatio",
                    RatioSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueSampledData",
                    SampledDataSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueSignature",
                    SignatureSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueTiming",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueContactDetail",
                    ContactDetailSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueContributor",
                    ContributorSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDataRequirement",
                    DataRequirementSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueExpression",
                    ExpressionSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinitionSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifactSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinitionSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueUsageContext",
                    UsageContextSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDosage",
                    DosageSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueMeta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
            ]
        )
        return schema
