import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.ecommerce.services import ProductService
from ecommerce_projec.ecommerce.serializers import ProductSerializer


class ProductView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, product_id):
        try:
            product = ProductService.get_product(product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ProductView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, product_id):
        try:
            serializer = ProductSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            product = ProductService.get_product(product_id)
            ProductService.update(product, serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ProductView::put Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, product_id):
        try:
            ProductService.delete(product_id)
            return Response(status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ProductView::delete Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
