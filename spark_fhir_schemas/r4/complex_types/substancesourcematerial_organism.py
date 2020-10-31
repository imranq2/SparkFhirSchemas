from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceSourceMaterial_Organism:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Source material shall capture information on the taxonomic and anatomical
        origins as well as the fraction of a material that can result in or can be
        modified to form a substance. This set of data elements shall be used to
        define polymer substances isolated from biological matrices. Taxonomic and
        anatomical origins shall be described using a controlled vocabulary as
        required. This information is captured for naturally derived polymers ( .
        starch) and structurally diverse substances. For Organisms belonging to the
        Kingdom Plantae the Substance level defines the fresh material of a single
        species or infraspecies, the Herbal Drug and the Herbal preparation. For
        Herbal preparations, the fraction information will be captured at the
        Substance information level and additional information for herbal extracts
        will be captured at the Specified Substance Group 1 information level. See for
        further explanation the Substance Class: Structurally Diverse and the herbal
        annex.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        family: The family of an organism shall be specified.

        genus: The genus of an organism shall be specified; refers to the Latin epithet of
            the genus element of the plant/animal scientific name; it is present in names
            for genera, species and infraspecies.

        species: The species of an organism shall be specified; refers to the Latin epithet of
            the species of the plant/animal; it is present in names for species and
            infraspecies.

        intraspecificType: The Intraspecific type of an organism shall be specified.

        intraspecificDescription: The intraspecific description of an organism shall be specified based on a
            controlled vocabulary. For Influenza Vaccine, the intraspecific description
            shall contain the syntax of the antigen in line with the WHO convention.

        author: 4.9.13.6.1 Author type (Conditional).

        hybrid: 4.9.13.8.1 Hybrid species maternal organism ID (Optional).

        organismGeneral: 4.9.13.7.1 Kingdom (Conditional).

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_author import SubstanceSourceMaterial_Author
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_hybrid import SubstanceSourceMaterial_Hybrid
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_organismgeneral import SubstanceSourceMaterial_OrganismGeneral
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The family of an organism shall be specified.
                StructField(
                    "family", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The genus of an organism shall be specified; refers to the Latin epithet of
                # the genus element of the plant/animal scientific name; it is present in names
                # for genera, species and infraspecies.
                StructField(
                    "genus", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The species of an organism shall be specified; refers to the Latin epithet of
                # the species of the plant/animal; it is present in names for species and
                # infraspecies.
                StructField(
                    "species", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The Intraspecific type of an organism shall be specified.
                StructField(
                    "intraspecificType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The intraspecific description of an organism shall be specified based on a
                # controlled vocabulary. For Influenza Vaccine, the intraspecific description
                # shall contain the syntax of the antigen in line with the WHO convention.
                StructField("intraspecificDescription", StringType(), True),
                # 4.9.13.6.1 Author type (Conditional).
                StructField(
                    "author",
                    ArrayType(
                        SubstanceSourceMaterial_Author.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
                StructField(
                    "hybrid",
                    SubstanceSourceMaterial_Hybrid.
                    get_schema(recursion_depth + 1), True
                ),
                # 4.9.13.7.1 Kingdom (Conditional).
                StructField(
                    "organismGeneral",
                    SubstanceSourceMaterial_OrganismGeneral.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
