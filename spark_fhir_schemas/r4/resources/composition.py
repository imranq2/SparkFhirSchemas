from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.composition_attester import Composition_Attester
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.composition_relatesto import Composition_RelatesTo
from spark_fhir_schemas.r4.resources.composition_event import Composition_Event
from spark_fhir_schemas.r4.resources.composition_section import Composition_Section


class Composition:
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
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("status", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("category",ArrayType(CodeableConcept.get_schema()), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField("author",ArrayType(Reference.get_schema()), True),
                StructField("title", StringType(), True),
                StructField("confidentiality", code.get_schema(), True),
                StructField("attester",ArrayType(Composition_Attester.get_schema()), True),
                StructField("custodian", Reference.get_schema(), True),
                StructField("relatesTo",ArrayType(Composition_RelatesTo.get_schema()), True),
                StructField("event",ArrayType(Composition_Event.get_schema()), True),
                StructField("section",ArrayType(Composition_Section.get_schema()), True),]
        )

        return schema
