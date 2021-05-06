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
class PractitionerSchema:
    """
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
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
        A person who is directly or indirectly involved in the provisioning of
        healthcare.


        resourceType: This is a Practitioner resource

        identifier: An identifier that applies to this person in this role.

        active: Whether this practitioner's record is in active use.

        name: The name(s) associated with the practitioner.

        telecom: A contact detail for the practitioner, e.g. a telephone number or an email
            address.

        address: Address(es) of the practitioner that are not role specific (typically home
            address).
            Work addresses are not typically entered in this property as they are usually
            role dependent.

        gender: Administrative Gender - the gender that the person is considered to have for
            administration and record keeping purposes.

        birthDate: The date of birth for the practitioner.

        photo: Image of the person.

        qualification: Qualifications obtained by training and certification.

        communication: A language the practitioner is able to use in patient communication.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.humanname import HumanNameSchema
        from spark_fhir_schemas.stu3.complex_types.contactpoint import ContactPointSchema
        from spark_fhir_schemas.stu3.complex_types.address import AddressSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.practitioner_qualification import Practitioner_QualificationSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        if (
            max_recursion_limit
            and nesting_list.count("Practitioner") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Practitioner"]
        schema = StructType(
            [
                # This is a Practitioner resource
                StructField("resourceType", StringType(), True),
                # An identifier that applies to this person in this role.
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
                # Whether this practitioner's record is in active use.
                StructField("active", BooleanType(), True),
                # The name(s) associated with the practitioner.
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
                # A contact detail for the practitioner, e.g. a telephone number or an email
                # address.
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
                # Address(es) of the practitioner that are not role specific (typically home
                # address).
                # Work addresses are not typically entered in this property as they are usually
                # role dependent.
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
                # Administrative Gender - the gender that the person is considered to have for
                # administration and record keeping purposes.
                StructField("gender", StringType(), True),
                # The date of birth for the practitioner.
                StructField("birthDate", StringType(), True),
                # Image of the person.
                StructField(
                    "photo",
                    ArrayType(
                        AttachmentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Qualifications obtained by training and certification.
                StructField(
                    "qualification",
                    ArrayType(
                        Practitioner_QualificationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A language the practitioner is able to use in patient communication.
                StructField(
                    "communication",
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
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
