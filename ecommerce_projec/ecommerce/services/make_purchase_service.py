from typing import List
from django.db import transaction
from ecommerce_projec.ecommerce.models import Customer, Product
from ecommerce_projec.ecommerce.services import PurchaseService, PurchaseProductService

Products = List[Product]


class MakePurchaseService:
    def __init__(self, customer: Customer):
        self.customer = customer

    @transaction.atomic
    def shop(self, products: Products):
        purchase_information = dict(customer=self.customer)
        purchase = PurchaseService(self.customer).add(purchase_information)
        PurchaseProductService(purchase).add_products(products)
        return purchase
