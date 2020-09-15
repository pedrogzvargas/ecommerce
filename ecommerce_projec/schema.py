import graphene
from ecommerce_projec.ecommerce.graph_schemas import ecommerce_schema, filter_schema, product_mutation


class Query(filter_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=product_mutation.Query, mutation=product_mutation.Mutation)
