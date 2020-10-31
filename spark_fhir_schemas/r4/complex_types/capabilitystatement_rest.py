from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CapabilityStatement_Rest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server for a particular version of FHIR that may be used as a statement of
        actual server functionality or a statement of required or desired server
        implementation.


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

        mode: Identifies whether this portion of the statement is describing the ability to
            initiate or receive restful operations.

        documentation: Information about the system's restful capabilities that apply across all
            applications, such as security.

        security: Information about security implementation from an interface perspective - what
            a client needs to know.

        resource: A specification of the restful capabilities of the solution for a specific
            resource type.

        interaction: A specification of restful operations supported by the system.

        searchParam: Search parameters that are supported for searching all resources for
            implementations to support and/or make use of - either references to ones
            defined in the specification, or additional ones defined for/by the
            implementation.

        operation: Definition of an operation or a named query together with its parameters and
            their meaning and type.

        compartment: An absolute URI which is a reference to the definition of a compartment that
            the system supports. The reference is to a CompartmentDefinition resource by
            its canonical URL .

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_security import CapabilityStatement_Security
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_resource import CapabilityStatement_Resource
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_interaction1 import CapabilityStatement_Interaction1
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_searchparam import CapabilityStatement_SearchParam
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_operation import CapabilityStatement_Operation
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
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
                # Identifies whether this portion of the statement is describing the ability to
                # initiate or receive restful operations.
                StructField("mode", StringType(), True),
                # Information about the system's restful capabilities that apply across all
                # applications, such as security.
                StructField(
                    "documentation", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # Information about security implementation from an interface perspective - what
                # a client needs to know.
                StructField(
                    "security",
                    CapabilityStatement_Security.
                    get_schema(recursion_depth + 1), True
                ),
                # A specification of the restful capabilities of the solution for a specific
                # resource type.
                StructField(
                    "resource",
                    ArrayType(
                        CapabilityStatement_Resource.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A specification of restful operations supported by the system.
                StructField(
                    "interaction",
                    ArrayType(
                        CapabilityStatement_Interaction1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Search parameters that are supported for searching all resources for
                # implementations to support and/or make use of - either references to ones
                # defined in the specification, or additional ones defined for/by the
                # implementation.
                StructField(
                    "searchParam",
                    ArrayType(
                        CapabilityStatement_SearchParam.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Definition of an operation or a named query together with its parameters and
                # their meaning and type.
                StructField(
                    "operation",
                    ArrayType(
                        CapabilityStatement_Operation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # An absolute URI which is a reference to the definition of a compartment that
                # the system supports. The reference is to a CompartmentDefinition resource by
                # its canonical URL .
                StructField(
                    "compartment",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
