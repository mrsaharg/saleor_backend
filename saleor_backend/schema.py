import graphene
from store.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
