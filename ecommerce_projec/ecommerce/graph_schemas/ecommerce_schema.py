import graphene
from graphene_django import DjangoObjectType
from ecommerce_projec.ecommerce.models import Product, Category


class EcommerceProduct(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'


class EcommerceCategory(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class Query(graphene.ObjectType):
    all_products = graphene.List(EcommerceProduct)
    category_by_name = graphene.Field(EcommerceCategory, name=graphene.String(required=True))

    def resolve_all_products(root, info):
        # We can easily optimize query count in the resolve method
        return Product.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
