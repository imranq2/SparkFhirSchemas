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
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.appointment_participant import Appointment_Participant
from spark_fhir_schemas.r4.resources.period import Period


class Appointment:
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
                StructField("cancelationReason", CodeableConcept.get_schema(), True),
                StructField("serviceCategory",ArrayType(CodeableConcept.get_schema()), True),
                StructField("serviceType",ArrayType(CodeableConcept.get_schema()), True),
                StructField("specialty",ArrayType(CodeableConcept.get_schema()), True),
                StructField("appointmentType", CodeableConcept.get_schema(), True),
                StructField("reasonCode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("reasonReference",ArrayType(Reference.get_schema()), True),
                StructField("priority", unsignedInt.get_schema(), True),
                StructField("description", StringType(), True),
                StructField("supportingInformation",ArrayType(Reference.get_schema()), True),
                StructField("start", instant.get_schema(), True),
                StructField("end", instant.get_schema(), True),
                StructField("minutesDuration", positiveInt.get_schema(), True),
                StructField("slot",ArrayType(Reference.get_schema()), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("comment", StringType(), True),
                StructField("patientInstruction", StringType(), True),
                StructField("basedOn",ArrayType(Reference.get_schema()), True),
                StructField("participant",ArrayType(Appointment_Participant.get_schema()), True),
                StructField("requestedPeriod",ArrayType(Period.get_schema()), True),]
        )

        return schema
