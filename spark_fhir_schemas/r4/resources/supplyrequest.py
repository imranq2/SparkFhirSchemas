from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SupplyRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A record of a request for a medication, substance or device used in the
        healthcare setting.


        resourceType: This is a SupplyRequest resource

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

        identifier: Business identifiers assigned to this SupplyRequest by the author and/or other
            systems. These identifiers remain constant as the resource is updated and
            propagates from server to server.

        status: Status of the supply request.

        category: Category of supply, e.g.  central, non-stock, etc. This is used to support
            work flows associated with the supply process.

        priority: Indicates how quickly this SupplyRequest should be addressed with respect to
            other requests.

        itemCodeableConcept: The item that is requested to be supplied. This is either a link to a resource
            representing the details of the item or a code that identifies the item from a
            known list.

        itemReference: The item that is requested to be supplied. This is either a link to a resource
            representing the details of the item or a code that identifies the item from a
            known list.

        quantity: The amount that is being ordered of the indicated item.

        parameter: Specific parameters for the ordered item.  For example, the size of the
            indicated item.

        occurrenceDateTime: When the request should be fulfilled.

        occurrencePeriod: When the request should be fulfilled.

        occurrenceTiming: When the request should be fulfilled.

        authoredOn: When the request was made.

        requester: The device, practitioner, etc. who initiated the request.

        supplier: Who is intended to fulfill the request.

        reasonCode: The reason why the supply item was requested.

        reasonReference: The reason why the supply item was requested.

        deliverFrom: Where the supply is expected to come from.

        deliverTo: Where the supply is destined to go.

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
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.supplyrequest_parameter import SupplyRequest_Parameter
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a SupplyRequest resource
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
                # Business identifiers assigned to this SupplyRequest by the author and/or other
                # systems. These identifiers remain constant as the resource is updated and
                # propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Status of the supply request.
                StructField("status", StringType(), True),
                # Category of supply, e.g.  central, non-stock, etc. This is used to support
                # work flows associated with the supply process.
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates how quickly this SupplyRequest should be addressed with respect to
                # other requests.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # The item that is requested to be supplied. This is either a link to a resource
                # representing the details of the item or a code that identifies the item from a
                # known list.
                StructField(
                    "itemCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The item that is requested to be supplied. This is either a link to a resource
                # representing the details of the item or a code that identifies the item from a
                # known list.
                StructField(
                    "itemReference", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The amount that is being ordered of the indicated item.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Specific parameters for the ordered item.  For example, the size of the
                # indicated item.
                StructField(
                    "parameter",
                    ArrayType(
                        SupplyRequest_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # When the request should be fulfilled.
                StructField("occurrenceDateTime", StringType(), True),
                # When the request should be fulfilled.
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # When the request should be fulfilled.
                StructField(
                    "occurrenceTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # When the request was made.
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The device, practitioner, etc. who initiated the request.
                StructField(
                    "requester", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Who is intended to fulfill the request.
                StructField(
                    "supplier",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The reason why the supply item was requested.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The reason why the supply item was requested.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Where the supply is expected to come from.
                StructField(
                    "deliverFrom", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Where the supply is destined to go.
                StructField(
                    "deliverTo", Reference.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
