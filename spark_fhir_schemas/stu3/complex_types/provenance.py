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
class ProvenanceSchema:
    """
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that resource.
    Provenance provides a critical foundation for assessing authenticity, enabling
    trust, and allowing reproducibility. Provenance assertions are a form of
    contextual metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in terms of
    confidence in authenticity, reliability, and trustworthiness, integrity, and
    stage in lifecycle (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust policies.
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
        Provenance of a resource is a record that describes entities and processes
        involved in producing and delivering or otherwise influencing that resource.
        Provenance provides a critical foundation for assessing authenticity, enabling
        trust, and allowing reproducibility. Provenance assertions are a form of
        contextual metadata and can themselves become important records with their own
        provenance. Provenance statement indicates clinical significance in terms of
        confidence in authenticity, reliability, and trustworthiness, integrity, and
        stage in lifecycle (e.g. Document Completion - has the artifact been legally
        authenticated), all of which may impact security, privacy, and trust policies.


        resourceType: This is a Provenance resource

        target: The Reference(s) that were generated or updated by  the activity described in
            this resource. A provenance can point to more than one target if multiple
            resources were created/updated by the same activity.

        period: The period during which the activity occurred.

        recorded: The instant of time at which the activity was recorded.

        policy: Policy or plan the activity was defined by. Typically, a single activity may
            have multiple applicable policy documents, such as patient consent, guarantor
            funding, etc.

        location: Where the activity occurred, if relevant.

        reason: The reason that the activity was taking place.

        activity: An activity is something that occurs over a period of time and acts upon or
            with entities; it may include consuming, processing, transforming, modifying,
            relocating, using, or generating entities.

        agent: An actor taking a role in an activity  for which it can be assigned some
            degree of responsibility for the activity taking place.

        entity: An entity used in this activity.

        signature: A digital signature on the target Reference(s). The signer should match a
            Provenance.agent. The purpose of the signature is indicated.

        """
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.provenance_agent import Provenance_AgentSchema
        from spark_fhir_schemas.stu3.complex_types.provenance_entity import Provenance_EntitySchema
        from spark_fhir_schemas.stu3.complex_types.signature import SignatureSchema
        if (
            max_recursion_limit
            and nesting_list.count("Provenance") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Provenance"]
        schema = StructType(
            [
                # This is a Provenance resource
                StructField("resourceType", StringType(), True),
                # The Reference(s) that were generated or updated by  the activity described in
                # this resource. A provenance can point to more than one target if multiple
                # resources were created/updated by the same activity.
                StructField(
                    "target",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The period during which the activity occurred.
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
                # The instant of time at which the activity was recorded.
                StructField("recorded", StringType(), True),
                # Policy or plan the activity was defined by. Typically, a single activity may
                # have multiple applicable policy documents, such as patient consent, guarantor
                # funding, etc.
                # Where the activity occurred, if relevant.
                StructField(
                    "location",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The reason that the activity was taking place.
                StructField(
                    "reason",
                    ArrayType(
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # An activity is something that occurs over a period of time and acts upon or
                # with entities; it may include consuming, processing, transforming, modifying,
                # relocating, using, or generating entities.
                StructField(
                    "activity",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # An actor taking a role in an activity  for which it can be assigned some
                # degree of responsibility for the activity taking place.
                StructField(
                    "agent",
                    ArrayType(
                        Provenance_AgentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # An entity used in this activity.
                StructField(
                    "entity",
                    ArrayType(
                        Provenance_EntitySchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A digital signature on the target Reference(s). The signer should match a
                # Provenance.agent. The purpose of the signature is indicated.
                StructField(
                    "signature",
                    ArrayType(
                        SignatureSchema.get_schema(
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
