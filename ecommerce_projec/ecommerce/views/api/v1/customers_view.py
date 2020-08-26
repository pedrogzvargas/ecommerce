import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ecommerce_projec.ecommerce.serializers import CustomerSerializer
from ecommerce_projec.ecommerce.services import CustomerService, ActorService


class CustomersView(APIView):

    def get(self, request):
        try:
            customers = CustomerService.get_customers()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CustomersView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        try:
            serializer = CustomerSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            ActorService.create_customer(serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CustomersView::post Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
