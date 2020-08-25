from rest_framework import serializers
from ecommerce_projec.ecommerce.models import PurchaseProducts


class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseProducts
        fields = '__all__'
