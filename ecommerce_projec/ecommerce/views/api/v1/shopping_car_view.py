import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.utils import Redis
from ecommerce_projec.ecommerce.services.cache import ShoppingCar
from ecommerce_projec.ecommerce.services import CustomerService, ProductService
from ecommerce_projec.ecommerce.serializers import (
    ShoppingCarSerializer,
    ShoppingCarProductSerializer
)


class ShoppingCarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, customer_id):
        try:
            customer = CustomerService.get_customer(customer_id)
            connection = Redis().get_connection()
            shopping_car = ShoppingCar(connection, customer).get()
            if not shopping_car:
                shopping_car = dict(customer_id=customer.id, products=[])
            serializer = ShoppingCarSerializer(shopping_car)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ShoppingCarView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, customer_id):
        try:
            customer = CustomerService.get_customer(customer_id)
            serializer = ShoppingCarProductSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            product_id = serializer.data.get('product_id')
            ProductService.get_product(product_id)
            connection = Redis().get_connection()
            ShoppingCar(connection, customer).add(serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ShoppingCarView::post Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
