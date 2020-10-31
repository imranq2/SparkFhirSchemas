from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CatalogEntry:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Catalog entries are wrappers that contextualize items included in a catalog.


        resourceType: This is a CatalogEntry resource

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

        identifier: Used in supporting different identifiers for the same product, e.g.
            manufacturer code and retailer code.

        type: The type of item - medication, device, service, protocol or other.

        orderable: Whether the entry represents an orderable item.

        referencedItem: The item in a catalog or definition.

        additionalIdentifier: Used in supporting related concepts, e.g. NDC to RxNorm.

        classification: Classes of devices, or ATC for medication.

        status: Used to support catalog exchange even for unsupported products, e.g. getting
            list of medications even if not prescribable.

        validityPeriod: The time period in which this catalog entry is expected to be active.

        validTo: The date until which this catalog entry is expected to be active.

        lastUpdated: Typically date of issue is different from the beginning of the validity. This
            can be used to see when an item was last updated.

        additionalCharacteristic: Used for examplefor Out of Formulary, or any specifics.

        additionalClassification: User for example for ATC classification, or.

        relatedEntry: Used for example, to point to a substance, or to a device used to administer a
            medication.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.catalogentry_relatedentry import CatalogEntry_RelatedEntry
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a CatalogEntry resource
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
                # Used in supporting different identifiers for the same product, e.g.
                # manufacturer code and retailer code.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The type of item - medication, device, service, protocol or other.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Whether the entry represents an orderable item.
                StructField("orderable", BooleanType(), True),
                # The item in a catalog or definition.
                StructField(
                    "referencedItem",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Used in supporting related concepts, e.g. NDC to RxNorm.
                StructField(
                    "additionalIdentifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Classes of devices, or ATC for medication.
                StructField(
                    "classification",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Used to support catalog exchange even for unsupported products, e.g. getting
                # list of medications even if not prescribable.
                StructField("status", StringType(), True),
                # The time period in which this catalog entry is expected to be active.
                StructField(
                    "validityPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date until which this catalog entry is expected to be active.
                StructField(
                    "validTo", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Typically date of issue is different from the beginning of the validity. This
                # can be used to see when an item was last updated.
                StructField(
                    "lastUpdated", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Used for examplefor Out of Formulary, or any specifics.
                StructField(
                    "additionalCharacteristic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # User for example for ATC classification, or.
                StructField(
                    "additionalClassification",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Used for example, to point to a substance, or to a device used to administer a
                # medication.
                StructField(
                    "relatedEntry",
                    ArrayType(
                        CatalogEntry_RelatedEntry.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
