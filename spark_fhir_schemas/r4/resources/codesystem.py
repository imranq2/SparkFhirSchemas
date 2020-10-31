from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class CodeSystem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.complex_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.codesystem_filter import CodeSystem_Filter
        from spark_fhir_schemas.r4.complex_types.codesystem_property import CodeSystem_Property
        from spark_fhir_schemas.r4.complex_types.codesystem_concept import CodeSystem_Concept
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("version", StringType(), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("status", StringType(), True),
                StructField("experimental", BooleanType(), True),
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField("publisher", StringType(), True),
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField("caseSensitive", BooleanType(), True),
                StructField(
                    "valueSet", canonical.get_schema(recursion_depth + 1), True
                ),
                StructField("hierarchyMeaning", StringType(), True),
                StructField("compositional", BooleanType(), True),
                StructField("versionNeeded", BooleanType(), True),
                StructField("content", StringType(), True),
                StructField(
                    "supplements", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "count", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "filter",
                    ArrayType(
                        CodeSystem_Filter.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "property",
                    ArrayType(
                        CodeSystem_Property.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "concept",
                    ArrayType(
                        CodeSystem_Concept.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
