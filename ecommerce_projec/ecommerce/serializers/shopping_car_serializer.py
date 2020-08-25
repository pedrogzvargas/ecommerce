from rest_framework import serializers


class ShoppingCarProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ShoppingCarSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    products = ShoppingCarProductSerializer(many=True)
