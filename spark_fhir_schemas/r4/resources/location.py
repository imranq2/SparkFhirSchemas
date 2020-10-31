from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
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


# noinspection PyPep8Naming
class Location:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("status", StringType(), True),
                StructField("operationalStatus", Coding.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("alias", ArrayType(StringType()), True),
                StructField("description", StringType(), True),
                StructField("mode", StringType(), True),
                StructField(
                    "type", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "telecom", ArrayType(ContactPoint.get_schema()), True
                ),
                StructField("address", Address.get_schema(), True),
                StructField(
                    "physicalType", CodeableConcept.get_schema(), True
                ),
                StructField("position", Location_Position.get_schema(), True),
                StructField(
                    "managingOrganization", Reference.get_schema(), True
                ),
                StructField("partOf", Reference.get_schema(), True),
                StructField(
                    "hoursOfOperation",
                    ArrayType(Location_HoursOfOperation.get_schema()), True
                ),
                StructField("availabilityExceptions", StringType(), True),
                StructField(
                    "endpoint", ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
