from django_redis import get_redis_connection
from django.conf import settings


class Redis:
    def __init__(self, cache_name=settings.CACHE_NAME):
        self.cache_name = cache_name

    def get_connection(self):
        connection = get_redis_connection(self.cache_name)
        return connection
