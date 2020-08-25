import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.ecommerce.services import CategoryService
from ecommerce_projec.ecommerce.serializers import CategorySerializer


class CategoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, category_id):
        try:
            category = CategoryService.get_category(category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CategoryView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, category_id):
        try:
            serializer = CategorySerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            category = CategoryService.get_category(category_id)
            CategoryService.update(category, serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CategoryView::put Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, category_id):
        try:
            CategoryService.delete(category_id)
            return Response(status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CategoryView::delete Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
