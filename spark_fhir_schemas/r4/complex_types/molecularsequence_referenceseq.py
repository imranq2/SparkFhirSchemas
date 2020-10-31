from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence_ReferenceSeq:
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

        chromosome: Structural unit composed of a nucleic acid molecule which controls its own
            replication through the interaction of specific proteins at one or more
            origins of replication ([SO:0000340](http://www.sequenceontology.org/browser/c
            urrent_svn/term/SO:0000340)).

        genomeBuild: The Genome Build used for reference, following GRCh build versions e.g. 'GRCh
            37'.  Version number must be included if a versioned release of a primary
            build was used.

        orientation: A relative reference to a DNA strand based on gene orientation. The strand
            that contains the open reading frame of the gene is the "sense" strand, and
            the opposite complementary strand is the "antisense" strand.

        referenceSeqId: Reference identifier of reference sequence submitted to NCBI. It must match
            the type in the MolecularSequence.type field. For example, the prefix, “NG_”
            identifies reference sequence for genes, “NM_” for messenger RNA transcripts,
            and “NP_” for amino acid sequences.

        referenceSeqPointer: A pointer to another MolecularSequence entity as reference sequence.

        referenceSeqString: A string like "ACGT".

        strand: An absolute reference to a strand. The Watson strand is the strand whose
            5'-end is on the short arm of the chromosome, and the Crick strand as the one
            whose 5'-end is on the long arm.

        windowStart: Start position of the window on the reference sequence. If the coordinate
            system is either 0-based or 1-based, then start position is inclusive.

        windowEnd: End position of the window on the reference sequence. If the coordinate system
            is 0-based then end is exclusive and does not include the last position. If
            the coordinate system is 1-base, then end is inclusive and includes the last
            position.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.integer import integer
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
                # Structural unit composed of a nucleic acid molecule which controls its own
                # replication through the interaction of specific proteins at one or more
                # origins of replication ([SO:0000340](http://www.sequenceontology.org/browser/c
                # urrent_svn/term/SO:0000340)).
                StructField(
                    "chromosome",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The Genome Build used for reference, following GRCh build versions e.g. 'GRCh
                # 37'.  Version number must be included if a versioned release of a primary
                # build was used.
                StructField("genomeBuild", StringType(), True),
                # A relative reference to a DNA strand based on gene orientation. The strand
                # that contains the open reading frame of the gene is the "sense" strand, and
                # the opposite complementary strand is the "antisense" strand.
                StructField("orientation", StringType(), True),
                # Reference identifier of reference sequence submitted to NCBI. It must match
                # the type in the MolecularSequence.type field. For example, the prefix, “NG_”
                # identifies reference sequence for genes, “NM_” for messenger RNA transcripts,
                # and “NP_” for amino acid sequences.
                StructField(
                    "referenceSeqId",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A pointer to another MolecularSequence entity as reference sequence.
                StructField(
                    "referenceSeqPointer",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A string like "ACGT".
                StructField("referenceSeqString", StringType(), True),
                # An absolute reference to a strand. The Watson strand is the strand whose
                # 5'-end is on the short arm of the chromosome, and the Crick strand as the one
                # whose 5'-end is on the long arm.
                StructField("strand", StringType(), True),
                # Start position of the window on the reference sequence. If the coordinate
                # system is either 0-based or 1-based, then start position is inclusive.
                StructField(
                    "windowStart", integer.get_schema(recursion_depth + 1),
                    True
                ),
                # End position of the window on the reference sequence. If the coordinate system
                # is 0-based then end is exclusive and does not include the last position. If
                # the coordinate system is 1-base, then end is inclusive and includes the last
                # position.
                StructField(
                    "windowEnd", integer.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
