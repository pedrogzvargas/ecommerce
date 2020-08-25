from django.urls import path
from rest_framework.authtoken import views
from ecommerce_projec.ecommerce.views.api.v1 import (
    CategoriesView,
    CategoryView,
    ProductsView,
    ProductView,
    CustomersView,
    ShoppingCarView,
    CustomerView,
    PurchasesView,
    PurchaseView,
    ConfirmShoppingCarView
)

urlpatterns = [
    path('category/', CategoriesView.as_view()),
    path('category/<int:category_id>/', CategoryView.as_view()),
    path('product/', ProductsView.as_view()),
    path('product/<int:product_id>/', ProductView.as_view()),
    path('customer/', CustomersView.as_view()),
    path('customer/<int:customer_id>/', CustomerView.as_view()),
    path('shopping-car/<int:customer_id>/', ShoppingCarView.as_view()),
    path('shopping-car/<int:customer_id>/confirm/', ConfirmShoppingCarView.as_view()),
    path('login/', views.obtain_auth_token),
    path('purchase/', PurchasesView.as_view()),
    path('purchase/<int:purchase_id>/', PurchaseView.as_view()),
]
