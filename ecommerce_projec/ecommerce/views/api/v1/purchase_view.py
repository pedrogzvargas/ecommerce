import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.ecommerce.serializers import PurchaseSerializer, MakePurchaseSerializer
from ecommerce_projec.ecommerce.services import PurchaseService, ProductService, MakePurchaseService


class PurchaseView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, purchase_id: int):
        try:
            purchase = PurchaseService.get_purchase(purchase_id)
            serializer = PurchaseSerializer(purchase)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"PurchaseView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, purchase_id: int):
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
            logging.info(f"PurchaseView::delete Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, purchase_id: int):
        try:
            purchase = PurchaseService.get_purchase(purchase_id)
            PurchaseService.delete(purchase)
            return Response(None, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"PurchaseView::delete Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
