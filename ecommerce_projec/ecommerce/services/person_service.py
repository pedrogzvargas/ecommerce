from django.contrib.auth.models import User
from ecommerce_projec.ecommerce.models import Person
from ecommerce_projec.utils import ModelPopulate


class PersonService:
    def __init__(self, user: User):
        self.user = user

    def add(self, person_information: dict):
        person = Person()
        person = ModelPopulate.populate(person, person_information)
        person.user = self.user
        person.save()
        return person

    def update(self, person: Person, person_information: dict):
        person = ModelPopulate.populate(person, person_information)
        person.user = self.user
        person.save()
        return person

    @staticmethod
    def get_people():
        people = Person.objects.all().order_by('id')
        return people

    @staticmethod
    def get_person(person_id):
        person = Person.objects.get(id=person_id)
        return person
