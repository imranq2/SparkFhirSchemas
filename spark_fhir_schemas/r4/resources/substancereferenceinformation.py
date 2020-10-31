from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.substancereferenceinformation_gene import SubstanceReferenceInformation_Gene
from spark_fhir_schemas.r4.resources.substancereferenceinformation_geneelement import SubstanceReferenceInformation_GeneElement
from spark_fhir_schemas.r4.resources.substancereferenceinformation_classification import SubstanceReferenceInformation_Classification
from spark_fhir_schemas.r4.resources.substancereferenceinformation_target import SubstanceReferenceInformation_Target


class SubstanceReferenceInformation:
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
                StructField("comment", StringType(), True),
                StructField("gene",ArrayType(SubstanceReferenceInformation_Gene.get_schema()), True),
                StructField("geneElement",ArrayType(SubstanceReferenceInformation_GeneElement.get_schema()), True),
                StructField("classification",ArrayType(SubstanceReferenceInformation_Classification.get_schema()), True),
                StructField("target",ArrayType(SubstanceReferenceInformation_Target.get_schema()), True),]
        )

        return schema
