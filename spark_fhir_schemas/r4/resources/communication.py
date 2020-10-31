from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.communication_payload import Communication_Payload
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class Communication:
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
                StructField(
                    "instantiatesCanonical", ArrayType(canonical.get_schema()),
                    True
                ),
                StructField(
                    "instantiatesUri", ArrayType(uri.get_schema()), True
                ),
                StructField(
                    "basedOn", ArrayType(Reference.get_schema()), True
                ),
                StructField("partOf", ArrayType(Reference.get_schema()), True),
                StructField(
                    "inResponseTo", ArrayType(Reference.get_schema()), True
                ),
                StructField("status", code.get_schema(), True),
                StructField(
                    "statusReason", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("priority", code.get_schema(), True),
                StructField(
                    "medium", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("subject", Reference.get_schema(), True),
                StructField("topic", CodeableConcept.get_schema(), True),
                StructField("about", ArrayType(Reference.get_schema()), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("sent", dateTime.get_schema(), True),
                StructField("received", dateTime.get_schema(), True),
                StructField(
                    "recipient", ArrayType(Reference.get_schema()), True
                ),
                StructField("sender", Reference.get_schema(), True),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reasonReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "payload", ArrayType(Communication_Payload.get_schema()),
                    True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
            ]
        )

        return schema