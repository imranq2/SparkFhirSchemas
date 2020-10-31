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
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.medicationdispense_performer import MedicationDispense_Performer
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.dosage import Dosage
from spark_fhir_schemas.r4.resources.medicationdispense_substitution import MedicationDispense_Substitution
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference


class MedicationDispense:
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
                StructField("partOf",ArrayType(Reference.get_schema()), True),
                StructField("status", code.get_schema(), True),
                StructField("statusReasonCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("statusReasonReference", Reference.get_schema(), True),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("medicationCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("medicationReference", Reference.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("context", Reference.get_schema(), True),
                StructField("supportingInformation",ArrayType(Reference.get_schema()), True),
                StructField("performer",ArrayType(MedicationDispense_Performer.get_schema()), True),
                StructField("location", Reference.get_schema(), True),
                StructField("authorizingPrescription",ArrayType(Reference.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("daysSupply", Quantity.get_schema(), True),
                StructField("whenPrepared", dateTime.get_schema(), True),
                StructField("whenHandedOver", dateTime.get_schema(), True),
                StructField("destination", Reference.get_schema(), True),
                StructField("receiver",ArrayType(Reference.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("dosageInstruction",ArrayType(Dosage.get_schema()), True),
                StructField("substitution", MedicationDispense_Substitution.get_schema(), True),
                StructField("detectedIssue",ArrayType(Reference.get_schema()), True),
                StructField("eventHistory",ArrayType(Reference.get_schema()), True),]
        )

        return schema
