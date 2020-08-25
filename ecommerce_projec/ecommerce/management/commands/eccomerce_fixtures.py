from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings

ECOMMERCE_FIXTURES = [
    'categories.json',
    'products.json',
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for fixture in ECOMMERCE_FIXTURES:
            try:
                call_command('loaddata', f'{settings.DJANGO_ROOT}/ecommerce/fixtures/{fixture}')
            except Exception as err:
                raise CommandError('Message {}'.format(err))
