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
class SearchParameterSchema:
    """
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
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
        A search parameter that defines a named search item that can be used to
        search/filter on a resource.


        resourceType: This is a SearchParameter resource

        url: An absolute URI that is used to identify this search parameter when it is
            referenced in a specification, model, design or an instance. This SHALL be a
            URL, SHOULD be globally unique, and SHOULD be an address at which this search
            parameter is (or will be) published. The URL SHOULD include the major version
            of the search parameter. For more information see [Technical and Business
            Versions](resource.html#versions).

        version: The identifier that is used to identify this version of the search parameter
            when it is referenced in a specification, model, design or instance. This is
            an arbitrary value managed by the search parameter author and is not expected
            to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
            a managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the search parameter. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        status: The status of this search parameter. Enables tracking the life-cycle of the
            content.

        experimental: A boolean value to indicate that this search parameter is authored for testing
            purposes (or education/evaluation/marketing), and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the search parameter was published. The
            date must change if and when the business version changes and it must change
            if the status code changes. In addition, it should change when the substantive
            content of the search parameter changes.

        publisher: The name of the individual or organization that published the search
            parameter.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These terms may be used to assist with indexing and searching
            for appropriate search parameter instances.

        jurisdiction: A legal or geographic region in which the search parameter is intended to be
            used.

        purpose: Explaination of why this search parameter is needed and why it has been
            designed as it has.

        code: The code used in the URL or the parameter name in a parameters resource for
            this search parameter.

        base: The base resource type(s) that this search parameter can be used against.

        type: The type of value a search parameter refers to, and how the content is
            interpreted.

        derivedFrom: Where this search parameter is originally defined. If a derivedFrom is
            provided, then the details in the search parameter must be consistent with the
            definition from which it is defined. I.e. the parameter should have the same
            meaning, and (usually) the functionality should be a proper subset of the
            underlying search parameter.

        description: A free text natural language description of the search parameter from a
            consumer's perspective. and how it used.

        expression: A FHIRPath expression that returns a set of elements for the search parameter.

        xpath: An XPath expression that returns a set of elements for the search parameter.

        xpathUsage: How the search parameter relates to the set of elements returned by evaluating
            the xpath query.

        target: Types of resource (if a resource is referenced).

        comparator: Comparators supported for the search parameter.

        modifier: A modifier supported for the search parameter.

        chain: Contains the names of any search parameters which may be chained to the
            containing search parameter. Chained parameters may be added to search
            parameters of type reference, and specify that resources will only be returned
            if they contain a reference to a resource which matches the chained parameter
            value. Values for this field should be drawn from SearchParameter.code for a
            parameter on the target resource type.

        component: Used to define the parts of a composite search parameter.

        """
        from spark_fhir_schemas.stu3.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.stu3.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.searchparameter_component import SearchParameter_ComponentSchema
        if (
            max_recursion_limit
            and nesting_list.count("SearchParameter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SearchParameter"]
        schema = StructType(
            [
                # This is a SearchParameter resource
                StructField("resourceType", StringType(), True),
                # An absolute URI that is used to identify this search parameter when it is
                # referenced in a specification, model, design or an instance. This SHALL be a
                # URL, SHOULD be globally unique, and SHOULD be an address at which this search
                # parameter is (or will be) published. The URL SHOULD include the major version
                # of the search parameter. For more information see [Technical and Business
                # Versions](resource.html#versions).
                StructField("url", StringType(), True),
                # The identifier that is used to identify this version of the search parameter
                # when it is referenced in a specification, model, design or instance. This is
                # an arbitrary value managed by the search parameter author and is not expected
                # to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
                # a managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the search parameter. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # The status of this search parameter. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A boolean value to indicate that this search parameter is authored for testing
                # purposes (or education/evaluation/marketing), and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the search parameter was published. The
                # date must change if and when the business version changes and it must change
                # if the status code changes. In addition, it should change when the substantive
                # content of the search parameter changes.
                StructField("date", StringType(), True),
                # The name of the individual or organization that published the search
                # parameter.
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
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # for appropriate search parameter instances.
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
                # A legal or geographic region in which the search parameter is intended to be
                # used.
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
                # Explaination of why this search parameter is needed and why it has been
                # designed as it has.
                StructField("purpose", StringType(), True),
                # The code used in the URL or the parameter name in a parameters resource for
                # this search parameter.
                StructField("code", StringType(), True),
                # The base resource type(s) that this search parameter can be used against.
                # The type of value a search parameter refers to, and how the content is
                # interpreted.
                StructField("type", StringType(), True),
                # Where this search parameter is originally defined. If a derivedFrom is
                # provided, then the details in the search parameter must be consistent with the
                # definition from which it is defined. I.e. the parameter should have the same
                # meaning, and (usually) the functionality should be a proper subset of the
                # underlying search parameter.
                StructField("derivedFrom", StringType(), True),
                # A free text natural language description of the search parameter from a
                # consumer's perspective. and how it used.
                StructField("description", StringType(), True),
                # A FHIRPath expression that returns a set of elements for the search parameter.
                StructField("expression", StringType(), True),
                # An XPath expression that returns a set of elements for the search parameter.
                StructField("xpath", StringType(), True),
                # How the search parameter relates to the set of elements returned by evaluating
                # the xpath query.
                StructField("xpathUsage", StringType(), True),
                # Types of resource (if a resource is referenced).
                # Comparators supported for the search parameter.
                # A modifier supported for the search parameter.
                # Contains the names of any search parameters which may be chained to the
                # containing search parameter. Chained parameters may be added to search
                # parameters of type reference, and specify that resources will only be returned
                # if they contain a reference to a resource which matches the chained parameter
                # value. Values for this field should be drawn from SearchParameter.code for a
                # parameter on the target resource type.
                # Used to define the parts of a composite search parameter.
                StructField(
                    "component",
                    ArrayType(
                        SearchParameter_ComponentSchema.get_schema(
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
