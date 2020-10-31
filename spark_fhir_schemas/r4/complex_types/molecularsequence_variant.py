from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence_Variant:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Raw data describing a biological sequence.


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

        start: Start position of the variant on the  reference sequence. If the coordinate
            system is either 0-based or 1-based, then start position is inclusive.

        end: End position of the variant on the reference sequence. If the coordinate
            system is 0-based then end is exclusive and does not include the last
            position. If the coordinate system is 1-base, then end is inclusive and
            includes the last position.

        observedAllele: An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
            23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
            Nucleotide(s)/amino acids from start position of sequence to stop position of
            sequence on the positive (+) strand of the observed  sequence. When the
            sequence  type is DNA, it should be the sequence on the positive (+) strand.
            This will lay in the range between variant.start and variant.end.

        referenceAllele: An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
            23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
            Nucleotide(s)/amino acids from start position of sequence to stop position of
            sequence on the positive (+) strand of the reference sequence. When the
            sequence  type is DNA, it should be the sequence on the positive (+) strand.
            This will lay in the range between variant.start and variant.end.

        cigar: Extended CIGAR string for aligning the sequence with reference bases. See
            detailed documentation [here](http://support.illumina.com/help/SequencingAnaly
            sisWorkflow/Content/Vault/Informatics/Sequencing_Analysis/CASAVA/swSEQ_mCA_Ext
            endedCIGARFormat.htm).

        variantPointer: A pointer to an Observation containing variant information.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # Start position of the variant on the  reference sequence. If the coordinate
                # system is either 0-based or 1-based, then start position is inclusive.
                StructField(
                    "start", integer.get_schema(recursion_depth + 1), True
                ),
                # End position of the variant on the reference sequence. If the coordinate
                # system is 0-based then end is exclusive and does not include the last
                # position. If the coordinate system is 1-base, then end is inclusive and
                # includes the last position.
                StructField(
                    "end", integer.get_schema(recursion_depth + 1), True
                ),
                # An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
                # 23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
                # Nucleotide(s)/amino acids from start position of sequence to stop position of
                # sequence on the positive (+) strand of the observed  sequence. When the
                # sequence  type is DNA, it should be the sequence on the positive (+) strand.
                # This will lay in the range between variant.start and variant.end.
                StructField("observedAllele", StringType(), True),
                # An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
                # 23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
                # Nucleotide(s)/amino acids from start position of sequence to stop position of
                # sequence on the positive (+) strand of the reference sequence. When the
                # sequence  type is DNA, it should be the sequence on the positive (+) strand.
                # This will lay in the range between variant.start and variant.end.
                StructField("referenceAllele", StringType(), True),
                # Extended CIGAR string for aligning the sequence with reference bases. See
                # detailed documentation [here](http://support.illumina.com/help/SequencingAnaly
                # sisWorkflow/Content/Vault/Informatics/Sequencing_Analysis/CASAVA/swSEQ_mCA_Ext
                # endedCIGARFormat.htm).
                StructField("cigar", StringType(), True),
                # A pointer to an Observation containing variant information.
                StructField(
                    "variantPointer",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
