from ecommerce_projec.ecommerce.models import Product
from ecommerce_projec.utils import ModelPopulate


class ProductService:
    @staticmethod
    def get_products():
        products = Product.objects.all().order_by('-id')
        return products

    @staticmethod
    def get_product(product_id: int):
        product = Product.objects.get(id=product_id)
        return product

    @staticmethod
    def add(product_information: dict):
        product = Product()
        product = ModelPopulate.populate(product, product_information)
        product.save()
        return product

    @staticmethod
    def update(product: Product, product_information: dict):
        product = ModelPopulate.populate(product, product_information)
        product.save()
        return product

    @staticmethod
    def delete(product_id: int):
        product = ProductService.get_product(product_id)
        product.delete()
