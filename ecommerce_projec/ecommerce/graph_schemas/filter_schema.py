import graphene
from graphene import relay, ObjectType, Mutation, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ecommerce_projec.ecommerce.models import Product, Category


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'products']
        interfaces = (relay.Node,)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = String()

    ok = graphene.Boolean()
    category = graphene.Field(lambda: Category)

    def mutate(root, info, name):
        category = Category(name=name)
        ok = True
        return CreateCategory(category=category, ok=ok)


class MyMutations(graphene.ObjectType):
    create_category = CreateCategory.Field()


class PeoductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    product = relay.Node.Field(PeoductNode)
    all_products = DjangoFilterConnectionField(PeoductNode)
