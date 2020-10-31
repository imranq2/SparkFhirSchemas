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
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.documentreference_relatesto import DocumentReference_RelatesTo
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.documentreference_content import DocumentReference_Content
from spark_fhir_schemas.r4.resources.documentreference_context import DocumentReference_Context


class DocumentReference:
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
                StructField("masterIdentifier", Identifier.get_schema(), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("docStatus", code.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("category",ArrayType(CodeableConcept.get_schema()), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("date", instant.get_schema(), True),
                StructField("author",ArrayType(Reference.get_schema()), True),
                StructField("authenticator", Reference.get_schema(), True),
                StructField("custodian", Reference.get_schema(), True),
                StructField("relatesTo",ArrayType(DocumentReference_RelatesTo.get_schema()), True),
                StructField("description", StringType(), True),
                StructField("securityLabel",ArrayType(CodeableConcept.get_schema()), True),
                StructField("content",ArrayType(DocumentReference_Content.get_schema()), True),
                StructField("context", DocumentReference_Context.get_schema(), True),]
        )

        return schema
