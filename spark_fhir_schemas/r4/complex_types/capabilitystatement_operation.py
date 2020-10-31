from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CapabilityStatement_Operation:
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

        name: The name of the operation or query. For an operation, this is the name
            prefixed with $ and used in the URL. For a query, this is the name used in the
            _query parameter when the query is called.

        definition: Where the formal definition can be found. If a server references the base
            definition of an Operation (i.e. from the specification itself such as
            ```http://hl7.org/fhir/OperationDefinition/ValueSet-expand```), that means it
            supports the full capabilities of the operation - e.g. both GET and POST
            invocation.  If it only supports a subset, it must define its own custom
            [[[OperationDefinition]]] with a 'base' of the original OperationDefinition.
            The custom definition would describe the specific subset of functionality
            supported.

        documentation: Documentation that describes anything special about the operation behavior,
            possibly detailing different behavior for system, type and instance-level
            invocation of the operation.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
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
                # The name of the operation or query. For an operation, this is the name
                # prefixed with $ and used in the URL. For a query, this is the name used in the
                # _query parameter when the query is called.
                StructField("name", StringType(), True),
                # Where the formal definition can be found. If a server references the base
                # definition of an Operation (i.e. from the specification itself such as
                # ```http://hl7.org/fhir/OperationDefinition/ValueSet-expand```), that means it
                # supports the full capabilities of the operation - e.g. both GET and POST
                # invocation.  If it only supports a subset, it must define its own custom
                # [[[OperationDefinition]]] with a 'base' of the original OperationDefinition.
                # The custom definition would describe the specific subset of functionality
                # supported.
                StructField(
                    "definition", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                # Documentation that describes anything special about the operation behavior,
                # possibly detailing different behavior for system, type and instance-level
                # invocation of the operation.
                StructField(
                    "documentation", markdown.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
