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
class AllergyIntolerance_ReactionSchema:
    """
    Risk of harmful or undesirable, physiological response which is unique to an
    individual and associated with exposure to a substance.
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
        Risk of harmful or undesirable, physiological response which is unique to an
        individual and associated with exposure to a substance.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        substance: Identification of the specific substance (or pharmaceutical product)
            considered to be responsible for the Adverse Reaction event. Note: the
            substance for a specific reaction may be different from the substance
            identified as the cause of the risk, but it must be consistent with it. For
            instance, it may be a more specific substance (e.g. a brand medication) or a
            composite product that includes the identified substance. It must be
            clinically safe to only process the 'code' and ignore the
            'reaction.substance'.  If a receiving system is unable to confirm that
            AllergyIntolerance.reaction.substance falls within the semantic scope of
            AllergyIntolerance.code, then the receiving system should ignore
            AllergyIntolerance.reaction.substance.

        manifestation: Clinical symptoms and/or signs that are observed or associated with the
            adverse reaction event.

        description: Text description about the reaction as a whole, including details of the
            manifestation if required.

        onset: Record of the date and/or time of the onset of the Reaction.

        severity: Clinical assessment of the severity of the reaction event as a whole,
            potentially considering multiple different manifestations.

        exposureRoute: Identification of the route by which the subject was exposed to the substance.

        note: Additional text about the adverse reaction event not captured in other fields.

        """
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.r4.simple_types.datetime import dateTimeSchema
        from spark_fhir_schemas.r4.complex_types.annotation import AnnotationSchema
        if (
            max_recursion_limit
            and nesting_list.count("AllergyIntolerance_Reaction") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "AllergyIntolerance_Reaction"
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
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Identification of the specific substance (or pharmaceutical product)
                # considered to be responsible for the Adverse Reaction event. Note: the
                # substance for a specific reaction may be different from the substance
                # identified as the cause of the risk, but it must be consistent with it. For
                # instance, it may be a more specific substance (e.g. a brand medication) or a
                # composite product that includes the identified substance. It must be
                # clinically safe to only process the 'code' and ignore the
                # 'reaction.substance'.  If a receiving system is unable to confirm that
                # AllergyIntolerance.reaction.substance falls within the semantic scope of
                # AllergyIntolerance.code, then the receiving system should ignore
                # AllergyIntolerance.reaction.substance.
                StructField(
                    "substance",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Clinical symptoms and/or signs that are observed or associated with the
                # adverse reaction event.
                StructField(
                    "manifestation",
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
                # Text description about the reaction as a whole, including details of the
                # manifestation if required.
                StructField("description", StringType(), True),
                # Record of the date and/or time of the onset of the Reaction.
                StructField(
                    "onset",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Clinical assessment of the severity of the reaction event as a whole,
                # potentially considering multiple different manifestations.
                StructField("severity", StringType(), True),
                # Identification of the route by which the subject was exposed to the substance.
                StructField(
                    "exposureRoute",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Additional text about the adverse reaction event not captured in other fields.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
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
