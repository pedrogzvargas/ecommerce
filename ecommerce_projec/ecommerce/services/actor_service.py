from django.db import transaction
from django.contrib.auth.models import User
from ecommerce_projec.utils import ModelPopulate
from ecommerce_projec.ecommerce.models import Customer
from ecommerce_projec.ecommerce.services import PersonService, CustomerService


class ActorService:
    @staticmethod
    @transaction.atomic
    def create_customer(customer_information: dict):
        user = User()
        user = ModelPopulate.populate(user, customer_information)
        user.set_password(customer_information.get('password'))
        user.save()
        person = PersonService(user).add(customer_information)
        customer = CustomerService(person).add(customer_information)
        return customer

    @staticmethod
    @transaction.atomic
    def update_customer(customer: Customer, customer_information: dict):
        user = customer.person.user
        person = customer.person
        user = ModelPopulate.populate(user, customer_information)
        user.set_password(customer_information.get('password'))
        user.save()
        person = PersonService(user).update(person, customer_information)
        customer = CustomerService(person).update(customer, customer_information)
        return customer
