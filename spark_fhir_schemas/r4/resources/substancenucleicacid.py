from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceNucleicAcid:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Nucleic acids are defined by three distinct elements: the base, sugar and
        linkage. Individual substance/moiety IDs will be created for each of these
        elements. The nucleotide sequence will be always entered in the 5’-3’
        direction.


        resourceType: This is a SubstanceNucleicAcid resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        sequenceType: The type of the sequence shall be specified based on a controlled vocabulary.

        numberOfSubunits: The number of linear sequences of nucleotides linked through phosphodiester
            bonds shall be described. Subunits would be strands of nucleic acids that are
            tightly associated typically through Watson-Crick base pairing. NOTE: If not
            specified in the reference source, the assumption is that there is 1 subunit.

        areaOfHybridisation: The area of hybridisation shall be described if applicable for double stranded
            RNA or DNA. The number associated with the subunit followed by the number
            associated to the residue shall be specified in increasing order. The
            underscore “” shall be used as separator as follows: “Subunitnumber Residue”.

        oligoNucleotideType: (TBC).

        subunit: Subunits are listed in order of decreasing length; sequences of the same
            length will be ordered by molecular weight; subunits that have identical
            sequences will be repeated multiple times.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.substancenucleicacid_subunit import SubstanceNucleicAcid_Subunit
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a SubstanceNucleicAcid resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The type of the sequence shall be specified based on a controlled vocabulary.
                StructField(
                    "sequenceType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The number of linear sequences of nucleotides linked through phosphodiester
                # bonds shall be described. Subunits would be strands of nucleic acids that are
                # tightly associated typically through Watson-Crick base pairing. NOTE: If not
                # specified in the reference source, the assumption is that there is 1 subunit.
                StructField(
                    "numberOfSubunits",
                    integer.get_schema(recursion_depth + 1), True
                ),
                # The area of hybridisation shall be described if applicable for double stranded
                # RNA or DNA. The number associated with the subunit followed by the number
                # associated to the residue shall be specified in increasing order. The
                # underscore “” shall be used as separator as follows: “Subunitnumber Residue”.
                StructField("areaOfHybridisation", StringType(), True),
                # (TBC).
                StructField(
                    "oligoNucleotideType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Subunits are listed in order of decreasing length; sequences of the same
                # length will be ordered by molecular weight; subunits that have identical
                # sequences will be repeated multiple times.
                StructField(
                    "subunit",
                    ArrayType(
                        SubstanceNucleicAcid_Subunit.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
