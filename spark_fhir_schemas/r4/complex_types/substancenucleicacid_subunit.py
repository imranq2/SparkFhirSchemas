from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceNucleicAcid_Subunit:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Nucleic acids are defined by three distinct elements: the base, sugar and
        linkage. Individual substance/moiety IDs will be created for each of these
        elements. The nucleotide sequence will be always entered in the 5’-3’
        direction.


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

        subunit: Index of linear sequences of nucleic acids in order of decreasing length.
            Sequences of the same length will be ordered by molecular weight. Subunits
            that have identical sequences will be repeated and have sequential subscripts.

        sequence: Actual nucleotide sequence notation from 5' to 3' end using standard single
            letter codes. In addition to the base sequence, sugar and type of phosphate or
            non-phosphate linkage should also be captured.

        length: The length of the sequence shall be captured.

        sequenceAttachment: (TBC).

        fivePrime: The nucleotide present at the 5’ terminal shall be specified based on a
            controlled vocabulary. Since the sequence is represented from the 5' to the 3'
            end, the 5’ prime nucleotide is the letter at the first position in the
            sequence. A separate representation would be redundant.

        threePrime: The nucleotide present at the 3’ terminal shall be specified based on a
            controlled vocabulary. Since the sequence is represented from the 5' to the 3'
            end, the 5’ prime nucleotide is the letter at the last position in the
            sequence. A separate representation would be redundant.

        linkage: The linkages between sugar residues will also be captured.

        sugar: 5.3.6.8.1 Sugar ID (Mandatory).

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substancenucleicacid_linkage import SubstanceNucleicAcid_Linkage
        from spark_fhir_schemas.r4.complex_types.substancenucleicacid_sugar import SubstanceNucleicAcid_Sugar
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
                # Index of linear sequences of nucleic acids in order of decreasing length.
                # Sequences of the same length will be ordered by molecular weight. Subunits
                # that have identical sequences will be repeated and have sequential subscripts.
                StructField(
                    "subunit", integer.get_schema(recursion_depth + 1), True
                ),
                # Actual nucleotide sequence notation from 5' to 3' end using standard single
                # letter codes. In addition to the base sequence, sugar and type of phosphate or
                # non-phosphate linkage should also be captured.
                StructField("sequence", StringType(), True),
                # The length of the sequence shall be captured.
                StructField(
                    "length", integer.get_schema(recursion_depth + 1), True
                ),
                # (TBC).
                StructField(
                    "sequenceAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # The nucleotide present at the 5’ terminal shall be specified based on a
                # controlled vocabulary. Since the sequence is represented from the 5' to the 3'
                # end, the 5’ prime nucleotide is the letter at the first position in the
                # sequence. A separate representation would be redundant.
                StructField(
                    "fivePrime",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The nucleotide present at the 3’ terminal shall be specified based on a
                # controlled vocabulary. Since the sequence is represented from the 5' to the 3'
                # end, the 5’ prime nucleotide is the letter at the last position in the
                # sequence. A separate representation would be redundant.
                StructField(
                    "threePrime",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The linkages between sugar residues will also be captured.
                StructField(
                    "linkage",
                    ArrayType(
                        SubstanceNucleicAcid_Linkage.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # 5.3.6.8.1 Sugar ID (Mandatory).
                StructField(
                    "sugar",
                    ArrayType(
                        SubstanceNucleicAcid_Sugar.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
