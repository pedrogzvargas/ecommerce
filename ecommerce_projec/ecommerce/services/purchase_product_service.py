from typing import List
from decimal import Decimal
from django.db.models import Sum
from ecommerce_projec.ecommerce.models import Product, Purchase, PurchaseProducts

Products = List[Product]


class PurchaseProductService:
    def __init__(self, purchase: Purchase):
        self.purchase = purchase

    def add_products(self, products: Products):
        products_list = list()
        for product in products:
            if not product.quantity:
                raise Exception(f"El producto '{product.name}' se encuentra agotado")
            purchase_product = PurchaseProducts()
            purchase_product.product_id = product.id
            purchase_product.purchase_id = self.purchase.id
            products_list.append(purchase_product)
            product.quantity -= 1
            product.save()
        PurchaseProducts.objects.bulk_create(products_list)
        self.calculate()
        return self.purchase

    def delete_product(self):
        pass

    def calculate(self):
        sum_dict = self.purchase.products.aggregate(Sum('price'))
        total = sum_dict.get('price__sum') or 0
        iva = total * Decimal(0.16)
        subtotal = total - iva
        self.purchase.total = total
        self.purchase.iva = iva
        self.purchase.subtotal = subtotal
        self.purchase.save()
        return self.purchase
