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
class PersonSchema:
    """
    Demographics and administrative information about a person independent of a
    specific health-related context.
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
        Demographics and administrative information about a person independent of a
        specific health-related context.


        resourceType: This is a Person resource

        identifier: Identifier for a person within a particular scope.

        name: A name associated with the person.

        telecom: A contact detail for the person, e.g. a telephone number or an email address.

        gender: Administrative Gender.

        birthDate: The birth date for the person.

        address: One or more addresses for the person.

        photo: An image that can be displayed as a thumbnail of the person to enhance the
            identification of the individual.

        managingOrganization: The organization that is the custodian of the person record.

        active: Whether this person's record is in active use.

        link: Link to a resource that concerns the same actual person.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.humanname import HumanNameSchema
        from spark_fhir_schemas.stu3.complex_types.contactpoint import ContactPointSchema
        from spark_fhir_schemas.stu3.complex_types.address import AddressSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.person_link import Person_LinkSchema
        if (
            max_recursion_limit
            and nesting_list.count("Person") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Person"]
        schema = StructType(
            [
                # This is a Person resource
                StructField("resourceType", StringType(), True),
                # Identifier for a person within a particular scope.
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
                # A name associated with the person.
                StructField(
                    "name",
                    ArrayType(
                        HumanNameSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A contact detail for the person, e.g. a telephone number or an email address.
                StructField(
                    "telecom",
                    ArrayType(
                        ContactPointSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Administrative Gender.
                StructField("gender", StringType(), True),
                # The birth date for the person.
                StructField("birthDate", StringType(), True),
                # One or more addresses for the person.
                StructField(
                    "address",
                    ArrayType(
                        AddressSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # An image that can be displayed as a thumbnail of the person to enhance the
                # identification of the individual.
                StructField(
                    "photo",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The organization that is the custodian of the person record.
                StructField(
                    "managingOrganization",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Whether this person's record is in active use.
                StructField("active", BooleanType(), True),
                # Link to a resource that concerns the same actual person.
                StructField(
                    "link",
                    ArrayType(
                        Person_LinkSchema.get_schema(
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
