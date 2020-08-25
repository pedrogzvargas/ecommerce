from rest_framework import serializers
from ecommerce_projec.ecommerce.models import Purchase, Product


class PurchaseProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='category.id')

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'category_id'
        )


class PurchaseSerializer(serializers.ModelSerializer):
    products = PurchaseProductSerializer(many=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'customer',
            'iva',
            'subtotal',
            'total',
            'products'
        )


class MakePurchaseSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
