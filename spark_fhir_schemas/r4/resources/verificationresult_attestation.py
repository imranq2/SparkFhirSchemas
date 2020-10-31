from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.signature import Signature
from spark_fhir_schemas.r4.resources.signature import Signature


class VerificationResult_Attestation:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("who", Reference.get_schema(), True),
                StructField("onBehalfOf", Reference.get_schema(), True),
                StructField("communicationMethod", CodeableConcept.get_schema(), True),
                StructField("date", DateType(), True),
                StructField("sourceIdentityCertificate", StringType(), True),
                StructField("proxyIdentityCertificate", StringType(), True),
                StructField("proxySignature", Signature.get_schema(), True),
                StructField("sourceSignature", Signature.get_schema(), True),]
        )

        return schema
