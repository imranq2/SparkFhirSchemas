from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CoverageEligibilityResponse_Item:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource provides eligibility and plan details from the processing of an
        CoverageEligibilityRequest resource.


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

        category: Code to identify the general type of benefits under which products and
            services are provided.

        productOrService: This contains the product, service, drug or other billing code for the item.

        modifier: Item typification or modifiers codes to convey additional context for the
            product or service.

        provider: The practitioner who is eligible for the provision of the product or service.

        excluded: True if the indicated class of service is excluded from the plan, missing or
            False indicates the product or service is included in the coverage.

        name: A short name or tag for the benefit.

        description: A richer description of the benefit or services covered.

        network: Is a flag to indicate whether the benefits refer to in-network providers or
            out-of-network providers.

        unit: Indicates if the benefits apply to an individual or to the family.

        term: The term or period of the values such as 'maximum lifetime benefit' or
            'maximum annual visits'.

        benefit: Benefits used to date.

        authorizationRequired: A boolean flag indicating whether a preauthorization is required prior to
            actual service delivery.

        authorizationSupporting: Codes or comments regarding information or actions associated with the
            preauthorization.

        authorizationUrl: A web location for obtaining requirements or descriptive information regarding
            the preauthorization.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_benefit import CoverageEligibilityResponse_Benefit
        from spark_fhir_schemas.r4.simple_types.uri import uri
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
                # Code to identify the general type of benefits under which products and
                # services are provided.
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # This contains the product, service, drug or other billing code for the item.
                StructField(
                    "productOrService",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Item typification or modifiers codes to convey additional context for the
                # product or service.
                StructField(
                    "modifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The practitioner who is eligible for the provision of the product or service.
                StructField(
                    "provider", Reference.get_schema(recursion_depth + 1), True
                ),
                # True if the indicated class of service is excluded from the plan, missing or
                # False indicates the product or service is included in the coverage.
                StructField("excluded", BooleanType(), True),
                # A short name or tag for the benefit.
                StructField("name", StringType(), True),
                # A richer description of the benefit or services covered.
                StructField("description", StringType(), True),
                # Is a flag to indicate whether the benefits refer to in-network providers or
                # out-of-network providers.
                StructField(
                    "network", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates if the benefits apply to an individual or to the family.
                StructField(
                    "unit", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The term or period of the values such as 'maximum lifetime benefit' or
                # 'maximum annual visits'.
                StructField(
                    "term", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Benefits used to date.
                StructField(
                    "benefit",
                    ArrayType(
                        CoverageEligibilityResponse_Benefit.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A boolean flag indicating whether a preauthorization is required prior to
                # actual service delivery.
                StructField("authorizationRequired", BooleanType(), True),
                # Codes or comments regarding information or actions associated with the
                # preauthorization.
                StructField(
                    "authorizationSupporting",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A web location for obtaining requirements or descriptive information regarding
                # the preauthorization.
                StructField(
                    "authorizationUrl", uri.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
