import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.ecommerce.services import CustomerService, ActorService
from ecommerce_projec.ecommerce.serializers import CustomerSerializer


class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, customer_id):
        try:
            customer = CustomerService.get_customer(customer_id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CustomerView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, customer_id):
        try:
            serializer = CustomerSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            customer = CustomerService.get_customer(customer_id)
            ActorService.update_customer(customer, serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CustomerView::put Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, customer_id):
        try:
            customer = CustomerService.get_customer(customer_id)
            CustomerService.soft_delete(customer)
            return Response(None, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CustomerView::delete Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
