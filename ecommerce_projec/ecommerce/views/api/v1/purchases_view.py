import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.ecommerce.serializers import PurchaseSerializer, MakePurchaseSerializer
from ecommerce_projec.ecommerce.services import PurchaseService, ProductService, MakePurchaseService


class PurchasesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            purchases = PurchaseService.get_purchases()
            serializer = PurchaseSerializer(purchases, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"PurchasesView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        try:
            serializer = MakePurchaseSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            product_id = serializer.data.get('product_id')
            quantity = serializer.data.get('quantity')
            customer = request.user.person.customer
            product = ProductService.get_product(product_id)
            products = [product for i in range(quantity)]
            MakePurchaseService(customer).shop(products)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"PurchasesView::post Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
