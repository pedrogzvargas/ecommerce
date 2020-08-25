from rest_framework import serializers
from ecommerce_projec.ecommerce.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
