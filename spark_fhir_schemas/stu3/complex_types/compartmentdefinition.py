from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CompartmentDefinitionSchema:
    """
    A compartment definition that defines how resources are accessed on a server.
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
        A compartment definition that defines how resources are accessed on a server.


        resourceType: This is a CompartmentDefinition resource

        url: An absolute URI that is used to identify this compartment definition when it
            is referenced in a specification, model, design or an instance. This SHALL be
            a URL, SHOULD be globally unique, and SHOULD be an address at which this
            compartment definition is (or will be) published. The URL SHOULD include the
            major version of the compartment definition. For more information see
            [Technical and Business Versions](resource.html#versions).

        name: A natural language name identifying the compartment definition. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.

        title: A short, descriptive, user-friendly title for the compartment definition.

        status: The status of this compartment definition. Enables tracking the life-cycle of
            the content.

        experimental: A boolean value to indicate that this compartment definition is authored for
            testing purposes (or education/evaluation/marketing), and is not intended to
            be used for genuine usage.

        date: The date  (and optionally time) when the compartment definition was published.
            The date must change if and when the business version changes and it must
            change if the status code changes. In addition, it should change when the
            substantive content of the compartment definition changes.

        publisher: The name of the individual or organization that published the compartment
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the compartment definition from a
            consumer's perspective.

        purpose: Explaination of why this compartment definition is needed and why it has been
            designed as it has.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These terms may be used to assist with indexing and searching
            for appropriate compartment definition instances.

        jurisdiction: A legal or geographic region in which the compartment definition is intended
            to be used.

        code: Which compartment this definition describes.

        search: Whether the search syntax is supported,.

        resource: Information about how a resource is related to the compartment.

        """
        from spark_fhir_schemas.stu3.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.stu3.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.compartmentdefinition_resource import CompartmentDefinition_ResourceSchema
        if (
            max_recursion_limit and
            nesting_list.count("CompartmentDefinition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CompartmentDefinition"]
        schema = StructType(
            [
                # This is a CompartmentDefinition resource
                StructField("resourceType", StringType(), True),
                # An absolute URI that is used to identify this compartment definition when it
                # is referenced in a specification, model, design or an instance. This SHALL be
                # a URL, SHOULD be globally unique, and SHOULD be an address at which this
                # compartment definition is (or will be) published. The URL SHOULD include the
                # major version of the compartment definition. For more information see
                # [Technical and Business Versions](resource.html#versions).
                StructField("url", StringType(), True),
                # A natural language name identifying the compartment definition. This name
                # should be usable as an identifier for the module by machine processing
                # applications such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the compartment definition.
                StructField("title", StringType(), True),
                # The status of this compartment definition. Enables tracking the life-cycle of
                # the content.
                StructField("status", StringType(), True),
                # A boolean value to indicate that this compartment definition is authored for
                # testing purposes (or education/evaluation/marketing), and is not intended to
                # be used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the compartment definition was published.
                # The date must change if and when the business version changes and it must
                # change if the status code changes. In addition, it should change when the
                # substantive content of the compartment definition changes.
                StructField("date", StringType(), True),
                # The name of the individual or organization that published the compartment
                # definition.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A free text natural language description of the compartment definition from a
                # consumer's perspective.
                StructField("description", StringType(), True),
                # Explaination of why this compartment definition is needed and why it has been
                # designed as it has.
                StructField("purpose", StringType(), True),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # for appropriate compartment definition instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A legal or geographic region in which the compartment definition is intended
                # to be used.
                StructField(
                    "jurisdiction",
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
                # Which compartment this definition describes.
                StructField("code", StringType(), True),
                # Whether the search syntax is supported,.
                StructField("search", BooleanType(), True),
                # Information about how a resource is related to the compartment.
                StructField(
                    "resource",
                    ArrayType(
                        CompartmentDefinition_ResourceSchema.get_schema(
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
