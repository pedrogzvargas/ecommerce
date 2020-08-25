from datetime import timedelta
import pickle
from django.db import transaction
from django.conf import settings
from ecommerce_projec.ecommerce.models import Customer
from ecommerce_projec.ecommerce.services import PurchaseService, PurchaseProductService, ProductService


class ShoppingCar:
    def __init__(self, connection, customer: Customer, ttl=settings.CACHE_TTL):
        self.connection = connection
        self.customer = customer
        self.ttl = ttl

    def get(self):
        unpacked_object = None
        cache_key = f'purchase_{self.customer.id}'
        purchase = self.connection.get(f'{cache_key}')
        if purchase:
            unpacked_object = pickle.loads(purchase)
        return unpacked_object

    def add(self, product_information: dict):
        cache_key = f'purchase_{self.customer.id}'
        product_id = product_information.get('product_id')
        purchase = self.get()
        if purchase:
            products_list = purchase.get('products', [])
            quantity = product_information.get('quantity')
            for item in products_list:
                item_product = item.get('product_id')
                if item_product == product_id:
                    item_quantity = item.get('quantity')
                    item['quantity'] = quantity + item_quantity
                    pickled_object = pickle.dumps(purchase)
                    self.connection.setex(f'{cache_key}', timedelta(seconds=self.ttl), pickled_object)
                    return purchase
            products_list.append(product_information)
            purchase_dict = dict(
                customer_id=self.customer.id,
                products=products_list
            )
            pickled_object = pickle.dumps(purchase_dict)
            self.connection.setex(f'{cache_key}', timedelta(seconds=self.ttl), pickled_object)
        else:
            products_list = list()
            products_list.append(product_information)
            purchase_dict = dict(
                customer_id=self.customer.id,
                products=products_list
            )
            pickled_object = pickle.dumps(purchase_dict)
            self.connection.setex(f'{cache_key}', timedelta(seconds=self.ttl), pickled_object)

    def clean(self):
        cache_key = f'purchase_{self.customer.id}'
        self.connection.expire(f'{cache_key}', 0)

    @transaction.atomic
    def confirm(self):
        shopping_car = self.get()
        if shopping_car:
            products = shopping_car.get('products', [])
            purchase = PurchaseService(self.customer).add({})
            for product in products:
                product_id = product.get('product_id')
                quantity = product.get('quantity')
                product = ProductService.get_product(product_id)
                items = [product for i in range(quantity)]
                PurchaseProductService(purchase).add_products(items)
            self.clean()
