from rest_framework import serializers
from ecommerce_projec.ecommerce.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }
