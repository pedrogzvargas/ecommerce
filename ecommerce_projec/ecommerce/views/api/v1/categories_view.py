import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ecommerce_projec.ecommerce.serializers import CategorySerializer
from ecommerce_projec.ecommerce.services import CategoryService


class CategoriesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            categories = CategoryService.get_categories()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CategoriesView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            CategoryService.add(serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CategoriesView::post Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
