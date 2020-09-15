import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from ecommerce_projec.ecommerce.models import Category
from ecommerce_projec.ecommerce.serializers import CategorySerializer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class DeleteCategory(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        category = Category.objects.get(id=kwargs.get('id'))
        category.delete()
        return cls(ok=True)


class CategorySerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = CategorySerializer
        model_operation = ['crate', 'update', ]
        lookup_field = 'id'


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, category_id=graphene.String())

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category(self, info, category_id):
        return Category.objects.get(id=category_id)


class Mutation(graphene.ObjectType):
    category_mutation = CategorySerializerMutation.Field()
