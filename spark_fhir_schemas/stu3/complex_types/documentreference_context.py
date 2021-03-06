from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DocumentReference_ContextSchema:
    """
    A reference to a document.
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
        A reference to a document.


        encounter: Describes the clinical encounter or type of care that the document content is
            associated with.

        event: This list of codes represents the main clinical acts, such as a colonoscopy or
            an appendectomy, being documented. In some cases, the event is inherent in the
            typeCode, such as a "History and Physical Report" in which the procedure being
            documented is necessarily a "History and Physical" act.

        period: The time period over which the service that is described by the document was
            provided.

        facilityType: The kind of facility where the patient was seen.

        practiceSetting: This property may convey specifics about the practice setting where the
            content was created, often reflecting the clinical specialty.

        sourcePatientInfo: The Patient Information as known when the document was published. May be a
            reference to a version specific, or contained.

        related: Related identifiers or resources associated with the DocumentReference.

        """
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.documentreference_related import DocumentReference_RelatedSchema
        if (
            max_recursion_limit
            and nesting_list.count("DocumentReference_Context") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "DocumentReference_Context"
        ]
        schema = StructType(
            [
                # Describes the clinical encounter or type of care that the document content is
                # associated with.
                StructField(
                    "encounter",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # This list of codes represents the main clinical acts, such as a colonoscopy or
                # an appendectomy, being documented. In some cases, the event is inherent in the
                # typeCode, such as a "History and Physical Report" in which the procedure being
                # documented is necessarily a "History and Physical" act.
                StructField(
                    "event",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The time period over which the service that is described by the document was
                # provided.
                StructField(
                    "period",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The kind of facility where the patient was seen.
                StructField(
                    "facilityType",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # This property may convey specifics about the practice setting where the
                # content was created, often reflecting the clinical specialty.
                StructField(
                    "practiceSetting",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The Patient Information as known when the document was published. May be a
                # reference to a version specific, or contained.
                StructField(
                    "sourcePatientInfo",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Related identifiers or resources associated with the DocumentReference.
                StructField(
                    "related",
                    ArrayType(
                        DocumentReference_RelatedSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
