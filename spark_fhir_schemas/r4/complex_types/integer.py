from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class integer:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType([])

        return schema
