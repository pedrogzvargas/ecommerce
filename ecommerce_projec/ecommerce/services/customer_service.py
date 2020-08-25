from ecommerce_projec.ecommerce.models import Person, Customer
from ecommerce_projec.utils import ModelPopulate


class CustomerService:
    def __init__(self, person: Person):
        self.person = person

    def add(self, customer_information: dict):
        customer = Customer()
        customer = ModelPopulate.populate(customer, customer_information)
        customer.person_id = self.person.id
        customer.save()
        return customer

    def update(self, customer: Customer, customer_information: dict):
        customer = ModelPopulate.populate(customer, customer_information)
        customer.person_id = self.person.id
        customer.save()
        return customer

    @staticmethod
    def soft_delete(customer):
        customer.is_deleted = True
        customer.save()
        return customer

    @staticmethod
    def get_customers():
        customers = Customer.objects.filter(is_deleted=False).order_by('id')
        return customers

    @staticmethod
    def get_customer(customer_id):
        customer = Customer.objects.get(id=customer_id)
        return customer
