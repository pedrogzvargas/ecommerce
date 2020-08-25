from django.db import transaction
from ecommerce_projec.ecommerce.models import Purchase, Customer, PurchaseProducts
from ecommerce_projec.utils import ModelPopulate


class PurchaseService:
    def __init__(self, customer: Customer):
        self.customer = customer

    @staticmethod
    def get_purchases():
        purchases = Purchase.objects.all().order_by('-id')
        return purchases

    @staticmethod
    def get_purchase(purchase_id: int):
        purchase = Purchase.objects.get(id=purchase_id)
        return purchase

    def add(self, purchase_information: dict):
        purchase = Purchase()
        purchase = ModelPopulate.populate(purchase, purchase_information)
        purchase.customer = self.customer
        purchase.save()
        return purchase

    @staticmethod
    def update(purchase: Purchase, purchase_information: dict):
        purchase = ModelPopulate.populate(purchase, purchase_information)
        purchase.save()
        return purchase

    @staticmethod
    @transaction.atomic
    def delete(purchase: Purchase):
        PurchaseProducts.objects.filter(purchase=purchase).delete()
        purchase.delete()
