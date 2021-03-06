from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Sequence_QualitySchema:
    """
    Raw data describing a biological sequence.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        Raw data describing a biological sequence.


        type: INDEL / SNP / Undefined variant.

        standardSequence: Gold standard sequence used for comparing against.

        start: Start position of the sequence. If the coordinate system is either 0-based or
            1-based, then start position is inclusive.

        end: End position of the sequence.If the coordinate system is 0-based then end is
            is exclusive and does not include the last position. If the coordinate system
            is 1-base, then end is inclusive and includes the last position.

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

        """
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        if (
            max_recursion_limit
            and nesting_list.count("Sequence_Quality") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Sequence_Quality"]
        schema = StructType(
            [
                # INDEL / SNP / Undefined variant.
                StructField("type", StringType(), True),
                # Gold standard sequence used for comparing against.
                StructField(
                    "standardSequence",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Start position of the sequence. If the coordinate system is either 0-based or
                # 1-based, then start position is inclusive.
                StructField("start", IntegerType(), True),
                # End position of the sequence.If the coordinate system is 0-based then end is
                # is exclusive and does not include the last position. If the coordinate system
                # is 1-base, then end is inclusive and includes the last position.
                StructField("end", IntegerType(), True),
                # The score of an experimentally derived feature such as a p-value ([SO:0001685]
                # (http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).
                StructField(
                    "score",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Which method is used to get sequence quality.
                StructField(
                    "method",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # True positives, from the perspective of the truth data, i.e. the number of
                # sites in the Truth Call Set for which there are paths through the Query Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField("truthTP", IntegerType(), True),
                # True positives, from the perspective of the query data, i.e. the number of
                # sites in the Query Call Set for which there are paths through the Truth Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField("queryTP", IntegerType(), True),
                # False negatives, i.e. the number of sites in the Truth Call Set for which
                # there is no path through the Query Call Set that is consistent with all of the
                # alleles at this site, or sites for which there is an inaccurate genotype call
                # for the event. Sites with correct variant but incorrect genotype are counted
                # here.
                StructField("truthFN", IntegerType(), True),
                # False positives, i.e. the number of sites in the Query Call Set for which
                # there is no path through the Truth Call Set that is consistent with this site.
                # Sites with correct variant but incorrect genotype are counted here.
                StructField("queryFP", IntegerType(), True),
                # The number of false positives where the non-REF alleles in the Truth and Query
                # Call Sets match (i.e. cases where the truth is 1/1 and the query is 0/1 or
                # similar).
                StructField("gtFP", IntegerType(), True),
                # QUERY.TP / (QUERY.TP + QUERY.FP).
                StructField("precision", IntegerType(), True),
                # TRUTH.TP / (TRUTH.TP + TRUTH.FN).
                StructField("recall", IntegerType(), True),
                # Harmonic mean of Recall and Precision, computed as: 2 * precision * recall /
                # (precision + recall).
                StructField("fScore", IntegerType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
