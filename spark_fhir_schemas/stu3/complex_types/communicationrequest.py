from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CommunicationRequestSchema:
    """
    A request to convey information; e.g. the CDS system proposes that an alert be
    sent to a responsible provider, the CDS system proposes that the public health
    agency be notified about a reportable condition.
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
        A request to convey information; e.g. the CDS system proposes that an alert be
        sent to a responsible provider, the CDS system proposes that the public health
        agency be notified about a reportable condition.


        resourceType: This is a CommunicationRequest resource

        identifier: A unique ID of this request for reference purposes. It must be provided if
            user wants it returned as part of any output, otherwise it will be
            autogenerated, if needed, by CDS system. Does not need to be the actual ID of
            the source system.

        basedOn: A plan or proposal that is fulfilled in whole or in part by this request.

        replaces: Completed or terminated request(s) whose function is taken by this new
            request.

        groupIdentifier: A shared identifier common to all requests that were authorized more or less
            simultaneously by a single author, representing the identifier of the
            requisition, prescription or similar form.

        status: The status of the proposal or order.

        category: The type of message to be sent such as alert, notification, reminder,
            instruction, etc.

        priority: Characterizes how quickly the proposed act must be initiated. Includes
            concepts such as stat, urgent, routine.

        medium: A channel that was used for this communication (e.g. email, fax).

        subject: The patient or group that is the focus of this communication request.

        recipient: The entity (e.g. person, organization, clinical information system, device,
            group, or care team) which is the intended target of the communication.

        topic: The resources which were related to producing this communication request.

        context: The encounter or episode of care within which the communication request was
            created.

        payload: Text, attachment(s), or resource(s) to be communicated to the recipient.

        occurrenceDateTime: The time when this communication is to occur.

        occurrencePeriod: The time when this communication is to occur.

        authoredOn: For draft requests, indicates the date of initial creation.  For requests with
            other statuses, indicates the date of activation.

        sender: The entity (e.g. person, organization, clinical information system, or device)
            which is to be the source of the communication.

        requester: The individual who initiated the request and has responsibility for its
            activation.

        reasonCode: Describes why the request is being made in coded or textual form.

        reasonReference: Indicates another resource whose existence justifies this request.

        note: Comments made about the request by the requester, sender, recipient, subject
            or other participants.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.communicationrequest_payload import CommunicationRequest_PayloadSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.communicationrequest_requester import CommunicationRequest_RequesterSchema
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema
        if (
            max_recursion_limit and
            nesting_list.count("CommunicationRequest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CommunicationRequest"]
        schema = StructType(
            [
                # This is a CommunicationRequest resource
                StructField("resourceType", StringType(), True),
                # A unique ID of this request for reference purposes. It must be provided if
                # user wants it returned as part of any output, otherwise it will be
                # autogenerated, if needed, by CDS system. Does not need to be the actual ID of
                # the source system.
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
                # A plan or proposal that is fulfilled in whole or in part by this request.
                StructField(
                    "basedOn",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Completed or terminated request(s) whose function is taken by this new
                # request.
                StructField(
                    "replaces",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A shared identifier common to all requests that were authorized more or less
                # simultaneously by a single author, representing the identifier of the
                # requisition, prescription or similar form.
                StructField(
                    "groupIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The status of the proposal or order.
                StructField("status", StringType(), True),
                # The type of message to be sent such as alert, notification, reminder,
                # instruction, etc.
                StructField(
                    "category",
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
                # Characterizes how quickly the proposed act must be initiated. Includes
                # concepts such as stat, urgent, routine.
                StructField("priority", StringType(), True),
                # A channel that was used for this communication (e.g. email, fax).
                StructField(
                    "medium",
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
                # The patient or group that is the focus of this communication request.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The entity (e.g. person, organization, clinical information system, device,
                # group, or care team) which is the intended target of the communication.
                StructField(
                    "recipient",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The resources which were related to producing this communication request.
                StructField(
                    "topic",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The encounter or episode of care within which the communication request was
                # created.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Text, attachment(s), or resource(s) to be communicated to the recipient.
                StructField(
                    "payload",
                    ArrayType(
                        CommunicationRequest_PayloadSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The time when this communication is to occur.
                StructField("occurrenceDateTime", StringType(), True),
                # The time when this communication is to occur.
                StructField(
                    "occurrencePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # For draft requests, indicates the date of initial creation.  For requests with
                # other statuses, indicates the date of activation.
                StructField("authoredOn", StringType(), True),
                # The entity (e.g. person, organization, clinical information system, or device)
                # which is to be the source of the communication.
                StructField(
                    "sender",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The individual who initiated the request and has responsibility for its
                # activation.
                StructField(
                    "requester",
                    CommunicationRequest_RequesterSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Describes why the request is being made in coded or textual form.
                StructField(
                    "reasonCode",
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
                # Indicates another resource whose existence justifies this request.
                StructField(
                    "reasonReference",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Comments made about the request by the requester, sender, recipient, subject
                # or other participants.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
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
