from ecommerce_projec.ecommerce.models import Category
from ecommerce_projec.utils import ModelPopulate


class CategoryService:
    @staticmethod
    def get_categories():
        categories = Category.objects.all()
        return categories

    @staticmethod
    def get_category(category_id: int):
        category = Category.objects.get(id=category_id)
        return category

    @staticmethod
    def add(category_information: dict):
        category = Category()
        category = ModelPopulate.populate(category, category_information)
        category.save()
        return category

    @staticmethod
    def update(category: Category, category_information: dict):
        category = ModelPopulate.populate(category, category_information)
        category.save()
        return category

    @staticmethod
    def delete(category_id: int):
        category = CategoryService.get_category(category_id)
        category.delete()
