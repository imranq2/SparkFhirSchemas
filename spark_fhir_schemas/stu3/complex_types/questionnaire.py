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
class QuestionnaireSchema:
    """
    A structured set of questions intended to guide the collection of answers from
    end-users. Questionnaires provide detailed control over order, presentation,
    phraseology and grouping to allow coherent, consistent data collection.
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
        A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.


        resourceType: This is a Questionnaire resource

        url: An absolute URI that is used to identify this questionnaire when it is
            referenced in a specification, model, design or an instance. This SHALL be a
            URL, SHOULD be globally unique, and SHOULD be an address at which this
            questionnaire is (or will be) published. The URL SHOULD include the major
            version of the questionnaire. For more information see [Technical and Business
            Versions](resource.html#versions).

        identifier: A formal identifier that is used to identify this questionnaire when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the questionnaire when
            it is referenced in a specification, model, design or instance. This is an
            arbitrary value managed by the questionnaire author and is not expected to be
            globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
            managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the questionnaire. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        title: A short, descriptive, user-friendly title for the questionnaire.

        status: The status of this questionnaire. Enables tracking the life-cycle of the
            content.

        experimental: A boolean value to indicate that this questionnaire is authored for testing
            purposes (or education/evaluation/marketing), and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the questionnaire was published. The date
            must change if and when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the questionnaire changes.

        publisher: The name of the individual or organization that published the questionnaire.

        description: A free text natural language description of the questionnaire from a
            consumer's perspective.

        purpose: Explaination of why this questionnaire is needed and why it has been designed
            as it has.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval, but doesn't change the original approval date.

        effectivePeriod: The period during which the questionnaire content was or is planned to be in
            active use.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These terms may be used to assist with indexing and searching
            for appropriate questionnaire instances.

        jurisdiction: A legal or geographic region in which the questionnaire is intended to be
            used.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        copyright: A copyright statement relating to the questionnaire and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the questionnaire.

        code: An identifier for this question or group of questions in a particular
            terminology such as LOINC.

        subjectType: The types of subjects that can be the subject of responses created for the
            questionnaire.

        item: A particular question, question grouping or display text that is part of the
            questionnaire.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.contactdetail import ContactDetailSchema
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.questionnaire_item import Questionnaire_ItemSchema
        if (
            max_recursion_limit
            and nesting_list.count("Questionnaire") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Questionnaire"]
        schema = StructType(
            [
                # This is a Questionnaire resource
                StructField("resourceType", StringType(), True),
                # An absolute URI that is used to identify this questionnaire when it is
                # referenced in a specification, model, design or an instance. This SHALL be a
                # URL, SHOULD be globally unique, and SHOULD be an address at which this
                # questionnaire is (or will be) published. The URL SHOULD include the major
                # version of the questionnaire. For more information see [Technical and Business
                # Versions](resource.html#versions).
                StructField("url", StringType(), True),
                # A formal identifier that is used to identify this questionnaire when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The identifier that is used to identify this version of the questionnaire when
                # it is referenced in a specification, model, design or instance. This is an
                # arbitrary value managed by the questionnaire author and is not expected to be
                # globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
                # managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the questionnaire. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the questionnaire.
                StructField("title", StringType(), True),
                # The status of this questionnaire. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A boolean value to indicate that this questionnaire is authored for testing
                # purposes (or education/evaluation/marketing), and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the questionnaire was published. The date
                # must change if and when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the questionnaire changes.
                StructField("date", StringType(), True),
                # The name of the individual or organization that published the questionnaire.
                StructField("publisher", StringType(), True),
                # A free text natural language description of the questionnaire from a
                # consumer's perspective.
                StructField("description", StringType(), True),
                # Explaination of why this questionnaire is needed and why it has been designed
                # as it has.
                StructField("purpose", StringType(), True),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", StringType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval, but doesn't change the original approval date.
                StructField("lastReviewDate", StringType(), True),
                # The period during which the questionnaire content was or is planned to be in
                # active use.
                StructField(
                    "effectivePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # for appropriate questionnaire instances.
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
                # A legal or geographic region in which the questionnaire is intended to be
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
                # A copyright statement relating to the questionnaire and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the questionnaire.
                StructField("copyright", StringType(), True),
                # An identifier for this question or group of questions in a particular
                # terminology such as LOINC.
                StructField(
                    "code",
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
                # The types of subjects that can be the subject of responses created for the
                # questionnaire.
                # A particular question, question grouping or display text that is part of the
                # questionnaire.
                StructField(
                    "item",
                    ArrayType(
                        Questionnaire_ItemSchema.get_schema(
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
