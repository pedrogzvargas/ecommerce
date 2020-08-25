import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.utils import Redis
from ecommerce_projec.ecommerce.services.cache import ShoppingCar
from ecommerce_projec.ecommerce.services import CustomerService


class ConfirmShoppingCarView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, customer_id):
        try:
            connection = Redis().get_connection()
            customer = CustomerService.get_customer(customer_id)
            ShoppingCar(connection, customer).confirm()
            return Response(None, status.HTTP_201_CREATED)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ShoppingCarView::post Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
