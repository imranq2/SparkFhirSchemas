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
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.invoice_participant import Invoice_Participant
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.invoice_lineitem import Invoice_LineItem
from spark_fhir_schemas.r4.resources.invoice_pricecomponent import Invoice_PriceComponent
from spark_fhir_schemas.r4.resources.money import Money
from spark_fhir_schemas.r4.resources.money import Money
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.annotation import Annotation


class Invoice:
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
                StructField("status", StringType(), True),
                StructField("cancelledReason", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("recipient", Reference.get_schema(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField("participant",ArrayType(Invoice_Participant.get_schema()), True),
                StructField("issuer", Reference.get_schema(), True),
                StructField("account", Reference.get_schema(), True),
                StructField("lineItem",ArrayType(Invoice_LineItem.get_schema()), True),
                StructField("totalPriceComponent",ArrayType(Invoice_PriceComponent.get_schema()), True),
                StructField("totalNet", Money.get_schema(), True),
                StructField("totalGross", Money.get_schema(), True),
                StructField("paymentTerms", markdown.get_schema(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),]
        )

        return schema
