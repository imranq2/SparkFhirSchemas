from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Location:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Details and position information for a physical place where services are
        provided and resources and participants may be stored, found, contained, or
        accommodated.


        resourceType: This is a Location resource

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

        identifier: Unique code or number identifying the location to its users.

        status: The status property covers the general availability of the resource, not the
            current value which may be covered by the operationStatus, or by a
            schedule/slots if they are configured for the location.

        operationalStatus: The operational status covers operation values most relevant to beds (but can
            also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis
            chair). This typically covers concepts such as contamination, housekeeping,
            and other activities like maintenance.

        name: Name of the location as used by humans. Does not need to be unique.

        alias: A list of alternate names that the location is known as, or was known as, in
            the past.

        description: Description of the Location, which helps in finding or referencing the place.

        mode: Indicates whether a resource instance represents a specific location or a
            class of locations.

        type: Indicates the type of function performed at the location.

        telecom: The contact details of communication devices available at the location. This
            can include phone numbers, fax numbers, mobile numbers, email addresses and
            web sites.

        address: Physical location.

        physicalType: Physical form of the location, e.g. building, room, vehicle, road.

        position: The absolute geographic location of the Location, expressed using the WGS84
            datum (This is the same co-ordinate system used in KML).

        managingOrganization: The organization responsible for the provisioning and upkeep of the location.

        partOf: Another Location of which this Location is physically a part of.

        hoursOfOperation: What days/times during a week is this location usually open.

        availabilityExceptions: A description of when the locations opening ours are different to normal, e.g.
            public holiday availability. Succinctly describing all possible exceptions to
            normal site availability as detailed in the opening hours Times.

        endpoint: Technical endpoints providing access to services operated for the location.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.location_position import Location_Position
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.location_hoursofoperation import Location_HoursOfOperation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Location resource
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
                # Unique code or number identifying the location to its users.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The status property covers the general availability of the resource, not the
                # current value which may be covered by the operationStatus, or by a
                # schedule/slots if they are configured for the location.
                StructField("status", StringType(), True),
                # The operational status covers operation values most relevant to beds (but can
                # also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis
                # chair). This typically covers concepts such as contamination, housekeeping,
                # and other activities like maintenance.
                StructField(
                    "operationalStatus",
                    Coding.get_schema(recursion_depth + 1), True
                ),
                # Name of the location as used by humans. Does not need to be unique.
                StructField("name", StringType(), True),
                # A list of alternate names that the location is known as, or was known as, in
                # the past.
                StructField("alias", ArrayType(StringType()), True),
                # Description of the Location, which helps in finding or referencing the place.
                StructField("description", StringType(), True),
                # Indicates whether a resource instance represents a specific location or a
                # class of locations.
                StructField("mode", StringType(), True),
                # Indicates the type of function performed at the location.
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The contact details of communication devices available at the location. This
                # can include phone numbers, fax numbers, mobile numbers, email addresses and
                # web sites.
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                # Physical location.
                StructField(
                    "address", Address.get_schema(recursion_depth + 1), True
                ),
                # Physical form of the location, e.g. building, room, vehicle, road.
                StructField(
                    "physicalType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The absolute geographic location of the Location, expressed using the WGS84
                # datum (This is the same co-ordinate system used in KML).
                StructField(
                    "position",
                    Location_Position.get_schema(recursion_depth + 1), True
                ),
                # The organization responsible for the provisioning and upkeep of the location.
                StructField(
                    "managingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Another Location of which this Location is physically a part of.
                StructField(
                    "partOf", Reference.get_schema(recursion_depth + 1), True
                ),
                # What days/times during a week is this location usually open.
                StructField(
                    "hoursOfOperation",
                    ArrayType(
                        Location_HoursOfOperation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A description of when the locations opening ours are different to normal, e.g.
                # public holiday availability. Succinctly describing all possible exceptions to
                # normal site availability as detailed in the opening hours Times.
                StructField("availabilityExceptions", StringType(), True),
                # Technical endpoints providing access to services operated for the location.
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
