from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class MolecularSequence_QualitySchema:
    """
    Raw data describing a biological sequence.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2
    ) -> Union[StructType, DataType]:
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

        type: INDEL / SNP / Undefined variant.

        standardSequence: Gold standard sequence used for comparing against.

        start: Start position of the sequence. If the coordinate system is either 0-based or
            1-based, then start position is inclusive.

        end: End position of the sequence. If the coordinate system is 0-based then end is
            exclusive and does not include the last position. If the coordinate system is
            1-base, then end is inclusive and includes the last position.

        score: The score of an experimentally derived feature such as a p-value ([SO:0001685]
            (http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).

        method: Which method is used to get sequence quality.

        truthTP: True positives, from the perspective of the truth data, i.e. the number of
            sites in the Truth Call Set for which there are paths through the Query Call
            Set that are consistent with all of the alleles at this site, and for which
            there is an accurate genotype call for the event.

        queryTP: True positives, from the perspective of the query data, i.e. the number of
            sites in the Query Call Set for which there are paths through the Truth Call
            Set that are consistent with all of the alleles at this site, and for which
            there is an accurate genotype call for the event.

        truthFN: False negatives, i.e. the number of sites in the Truth Call Set for which
            there is no path through the Query Call Set that is consistent with all of the
            alleles at this site, or sites for which there is an inaccurate genotype call
            for the event. Sites with correct variant but incorrect genotype are counted
            here.

        queryFP: False positives, i.e. the number of sites in the Query Call Set for which
            there is no path through the Truth Call Set that is consistent with this site.
            Sites with correct variant but incorrect genotype are counted here.

        gtFP: The number of false positives where the non-REF alleles in the Truth and Query
            Call Sets match (i.e. cases where the truth is 1/1 and the query is 0/1 or
            similar).

        precision: QUERY.TP / (QUERY.TP + QUERY.FP).

        recall: TRUTH.TP / (TRUTH.TP + TRUTH.FN).

        fScore: Harmonic mean of Recall and Precision, computed as: 2 * precision * recall /
            (precision + recall).

        roc: Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity
            tradeoff.

        """
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.simple_types.integer import integerSchema
        from spark_fhir_schemas.r4.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4.simple_types.decimal import decimalSchema
        from spark_fhir_schemas.r4.complex_types.molecularsequence_roc import MolecularSequence_RocSchema
        if (
            max_recursion_limit
            and nesting_list.count("MolecularSequence_Quality") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "MolecularSequence_Quality"
        ]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.

                # >>> Hiding extension Extension

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

                # >>> Hiding modifierExtension Extension

                # INDEL / SNP / Undefined variant.
                StructField("type", StringType(), True),
                # Gold standard sequence used for comparing against.
                StructField(
                    "standardSequence",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Start position of the sequence. If the coordinate system is either 0-based or
                # 1-based, then start position is inclusive.
                StructField(
                    "start",
                    integerSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # End position of the sequence. If the coordinate system is 0-based then end is
                # exclusive and does not include the last position. If the coordinate system is
                # 1-base, then end is inclusive and includes the last position.
                StructField(
                    "end",
                    integerSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The score of an experimentally derived feature such as a p-value ([SO:0001685]
                # (http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).
                StructField(
                    "score",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Which method is used to get sequence quality.
                StructField(
                    "method",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # True positives, from the perspective of the truth data, i.e. the number of
                # sites in the Truth Call Set for which there are paths through the Query Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField(
                    "truthTP",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # True positives, from the perspective of the query data, i.e. the number of
                # sites in the Query Call Set for which there are paths through the Truth Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField(
                    "queryTP",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # False negatives, i.e. the number of sites in the Truth Call Set for which
                # there is no path through the Query Call Set that is consistent with all of the
                # alleles at this site, or sites for which there is an inaccurate genotype call
                # for the event. Sites with correct variant but incorrect genotype are counted
                # here.
                StructField(
                    "truthFN",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # False positives, i.e. the number of sites in the Query Call Set for which
                # there is no path through the Truth Call Set that is consistent with this site.
                # Sites with correct variant but incorrect genotype are counted here.
                StructField(
                    "queryFP",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # The number of false positives where the non-REF alleles in the Truth and Query
                # Call Sets match (i.e. cases where the truth is 1/1 and the query is 0/1 or
                # similar).
                StructField(
                    "gtFP",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # QUERY.TP / (QUERY.TP + QUERY.FP).
                StructField(
                    "precision",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # TRUTH.TP / (TRUTH.TP + TRUTH.FN).
                StructField(
                    "recall",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Harmonic mean of Recall and Precision, computed as: 2 * precision * recall /
                # (precision + recall).
                StructField(
                    "fScore",
                    decimalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
                # Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity
                # tradeoff.
                StructField(
                    "roc",
                    MolecularSequence_RocSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit
                    ), True
                ),
            ]
        )
        return schema
