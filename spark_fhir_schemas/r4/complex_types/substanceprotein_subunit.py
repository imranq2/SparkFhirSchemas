from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceProtein_Subunit:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A SubstanceProtein is defined as a single unit of a linear amino acid
        sequence, or a combination of subunits that are either covalently linked or
        have a defined invariant stoichiometric relationship. This includes all
        synthetic, recombinant and purified SubstanceProteins of defined sequence,
        whether the use is therapeutic or prophylactic. This set of elements will be
        used to describe albumins, coagulation factors, cytokines, growth factors,
        peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant
        vaccines, and immunomodulators.


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

        subunit: Index of primary sequences of amino acids linked through peptide bonds in
            order of decreasing length. Sequences of the same length will be ordered by
            molecular weight. Subunits that have identical sequences will be repeated and
            have sequential subscripts.

        sequence: The sequence information shall be provided enumerating the amino acids from N-
            to C-terminal end using standard single-letter amino acid codes. Uppercase
            shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
            SubstanceProteins will always be described using the translated sequence; for
            synthetic peptide containing amino acids that are not represented with a
            single letter code an X should be used within the sequence. The modified amino
            acids will be distinguished by their position in the sequence.

        length: Length of linear sequences of amino acids contained in the subunit.

        sequenceAttachment: The sequence information shall be provided enumerating the amino acids from N-
            to C-terminal end using standard single-letter amino acid codes. Uppercase
            shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
            SubstanceProteins will always be described using the translated sequence; for
            synthetic peptide containing amino acids that are not represented with a
            single letter code an X should be used within the sequence. The modified amino
            acids will be distinguished by their position in the sequence.

        nTerminalModificationId: Unique identifier for molecular fragment modification based on the ISO 11238
            Substance ID.

        nTerminalModification: The name of the fragment modified at the N-terminal of the SubstanceProtein
            shall be specified.

        cTerminalModificationId: Unique identifier for molecular fragment modification based on the ISO 11238
            Substance ID.

        cTerminalModification: The modification at the C-terminal shall be specified.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
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
                # Index of primary sequences of amino acids linked through peptide bonds in
                # order of decreasing length. Sequences of the same length will be ordered by
                # molecular weight. Subunits that have identical sequences will be repeated and
                # have sequential subscripts.
                StructField(
                    "subunit", integer.get_schema(recursion_depth + 1), True
                ),
                # The sequence information shall be provided enumerating the amino acids from N-
                # to C-terminal end using standard single-letter amino acid codes. Uppercase
                # shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
                # SubstanceProteins will always be described using the translated sequence; for
                # synthetic peptide containing amino acids that are not represented with a
                # single letter code an X should be used within the sequence. The modified amino
                # acids will be distinguished by their position in the sequence.
                StructField("sequence", StringType(), True),
                # Length of linear sequences of amino acids contained in the subunit.
                StructField(
                    "length", integer.get_schema(recursion_depth + 1), True
                ),
                # The sequence information shall be provided enumerating the amino acids from N-
                # to C-terminal end using standard single-letter amino acid codes. Uppercase
                # shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
                # SubstanceProteins will always be described using the translated sequence; for
                # synthetic peptide containing amino acids that are not represented with a
                # single letter code an X should be used within the sequence. The modified amino
                # acids will be distinguished by their position in the sequence.
                StructField(
                    "sequenceAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # Unique identifier for molecular fragment modification based on the ISO 11238
                # Substance ID.
                StructField(
                    "nTerminalModificationId",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The name of the fragment modified at the N-terminal of the SubstanceProtein
                # shall be specified.
                StructField("nTerminalModification", StringType(), True),
                # Unique identifier for molecular fragment modification based on the ISO 11238
                # Substance ID.
                StructField(
                    "cTerminalModificationId",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The modification at the C-terminal shall be specified.
                StructField("cTerminalModification", StringType(), True),
            ]
        )
        return schema
