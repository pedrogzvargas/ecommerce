from rest_framework import serializers
from ecommerce_projec.ecommerce.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='person.user.username')
    password = serializers.CharField(required=False)
    email = serializers.EmailField(source='person.user.email')
    name = serializers.CharField(source='person.name')
    last_name = serializers.CharField(source='person.last_name')

    class Meta:
        model = Customer
        fields = (
            'id',
            'username',
            'password',
            'email',
            'name',
            'last_name',
            'is_active',
            'is_deleted',
        )
