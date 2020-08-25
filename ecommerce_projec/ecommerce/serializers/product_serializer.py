from rest_framework import serializers
from ecommerce_projec.ecommerce.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='category.id')

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'category_id'
        )
