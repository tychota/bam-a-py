import graphene
import bam_a_py.users.schema


class Query(bam_a_py.users.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
