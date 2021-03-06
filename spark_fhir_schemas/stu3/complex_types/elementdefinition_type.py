from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ElementDefinition_TypeSchema:
    """
    Captures constraints on each element within the resource, profile, or
    extension.
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
        Captures constraints on each element within the resource, profile, or
        extension.


        code: URL of Data type or Resource that is a(or the) type used for this element.
            References are URLs that are relative to
            http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to
            http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed
            in logical models.

        profile: Identifies a profile structure or implementation Guide that SHALL hold for the
            datatype this element refers to. Can be a local reference - to a contained
            StructureDefinition, or a reference to another StructureDefinition or
            Implementation Guide by a canonical URL. When an implementation guide is
            specified, the resource SHALL conform to at least one profile defined in the
            implementation guide.

        targetProfile: Identifies a profile structure or implementation Guide that SHALL hold for the
            target of the reference this element refers to. Can be a local reference - to
            a contained StructureDefinition, or a reference to another StructureDefinition
            or Implementation Guide by a canonical URL. When an implementation guide is
            specified, the resource SHALL conform to at least one profile defined in the
            implementation guide.

        aggregation: If the type is a reference to another resource, how the resource is or can be
            aggregated - is it a contained resource, or a reference, and if the context is
            a bundle, is it included in the bundle.

        versioning: Whether this reference needs to be version specific or version independent, or
            whether either can be used.

        """
        if (
            max_recursion_limit and
            nesting_list.count("ElementDefinition_Type") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ElementDefinition_Type"]
        schema = StructType(
            [
                # URL of Data type or Resource that is a(or the) type used for this element.
                # References are URLs that are relative to
                # http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to
                # http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed
                # in logical models.
                StructField("code", StringType(), True),
                # Identifies a profile structure or implementation Guide that SHALL hold for the
                # datatype this element refers to. Can be a local reference - to a contained
                # StructureDefinition, or a reference to another StructureDefinition or
                # Implementation Guide by a canonical URL. When an implementation guide is
                # specified, the resource SHALL conform to at least one profile defined in the
                # implementation guide.
                StructField("profile", StringType(), True),
                # Identifies a profile structure or implementation Guide that SHALL hold for the
                # target of the reference this element refers to. Can be a local reference - to
                # a contained StructureDefinition, or a reference to another StructureDefinition
                # or Implementation Guide by a canonical URL. When an implementation guide is
                # specified, the resource SHALL conform to at least one profile defined in the
                # implementation guide.
                StructField("targetProfile", StringType(), True),
                # If the type is a reference to another resource, how the resource is or can be
                # aggregated - is it a contained resource, or a reference, and if the context is
                # a bundle, is it included in the bundle.
                # Whether this reference needs to be version specific or version independent, or
                # whether either can be used.
                StructField("versioning", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
