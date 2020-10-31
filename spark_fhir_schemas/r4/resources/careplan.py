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
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.careplan_activity import CarePlan_Activity
from spark_fhir_schemas.r4.resources.annotation import Annotation


class CarePlan:
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
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("instantiatesCanonical",ArrayType(canonical.get_schema()), True),
                StructField("instantiatesUri",ArrayType(uri.get_schema()), True),
                StructField("basedOn",ArrayType(Reference.get_schema()), True),
                StructField("replaces",ArrayType(Reference.get_schema()), True),
                StructField("partOf",ArrayType(Reference.get_schema()), True),
                StructField("status", code.get_schema(), True),
                StructField("intent", code.get_schema(), True),
                StructField("category",ArrayType(CodeableConcept.get_schema()), True),
                StructField("title", StringType(), True),
                StructField("description", StringType(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("period", Period.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("author", Reference.get_schema(), True),
                StructField("contributor",ArrayType(Reference.get_schema()), True),
                StructField("careTeam",ArrayType(Reference.get_schema()), True),
                StructField("addresses",ArrayType(Reference.get_schema()), True),
                StructField("supportingInfo",ArrayType(Reference.get_schema()), True),
                StructField("goal",ArrayType(Reference.get_schema()), True),
                StructField("activity",ArrayType(CarePlan_Activity.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),]
        )

        return schema
