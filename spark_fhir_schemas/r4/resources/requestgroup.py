from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RequestGroup:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A group of related requests that can be used to capture intended activities
        that have inter-dependencies such as "give this medication after that one".


        resourceType: This is a RequestGroup resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: Allows a service to provide a unique, business identifier for the request.

        instantiatesCanonical: A canonical URL referencing a FHIR-defined protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this request.

        instantiatesUri: A URL referencing an externally defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this request.

        basedOn: A plan, proposal or order that is fulfilled in whole or in part by this
            request.

        replaces: Completed or terminated request(s) whose function is taken by this new
            request.

        groupIdentifier: A shared identifier common to all requests that were authorized more or less
            simultaneously by a single author, representing the identifier of the
            requisition, prescription or similar form.

        status: The current state of the request. For request groups, the status reflects the
            status of all the requests in the group.

        intent: Indicates the level of authority/intentionality associated with the request
            and where the request fits into the workflow chain.

        priority: Indicates how quickly the request should be addressed with respect to other
            requests.

        code: A code that identifies what the overall request group is.

        subject: The subject for which the request group was created.

        encounter: Describes the context of the request group, if any.

        authoredOn: Indicates when the request group was created.

        author: Provides a reference to the author of the request group.

        reasonCode: Describes the reason for the request group in coded or textual form.

        reasonReference: Indicates another resource whose existence justifies this request group.

        note: Provides a mechanism to communicate additional information about the response.

        action: The actions, if any, produced by the evaluation of the artifact.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.requestgroup_action import RequestGroup_Action
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a RequestGroup resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Allows a service to provide a unique, business identifier for the request.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # A canonical URL referencing a FHIR-defined protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this request.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # A URL referencing an externally defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this request.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # A plan, proposal or order that is fulfilled in whole or in part by this
                # request.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Completed or terminated request(s) whose function is taken by this new
                # request.
                StructField(
                    "replaces",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A shared identifier common to all requests that were authorized more or less
                # simultaneously by a single author, representing the identifier of the
                # requisition, prescription or similar form.
                StructField(
                    "groupIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The current state of the request. For request groups, the status reflects the
                # status of all the requests in the group.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates the level of authority/intentionality associated with the request
                # and where the request fits into the workflow chain.
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates how quickly the request should be addressed with respect to other
                # requests.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # A code that identifies what the overall request group is.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The subject for which the request group was created.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # Describes the context of the request group, if any.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates when the request group was created.
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Provides a reference to the author of the request group.
                StructField(
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                # Describes the reason for the request group in coded or textual form.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource whose existence justifies this request group.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Provides a mechanism to communicate additional information about the response.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # The actions, if any, produced by the evaluation of the artifact.
                StructField(
                    "action",
                    ArrayType(
                        RequestGroup_Action.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
