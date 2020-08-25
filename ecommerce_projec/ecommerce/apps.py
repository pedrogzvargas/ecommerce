from django.apps import AppConfig


class EcommerceConfig(AppConfig):
    name = 'ecommerce_projec.ecommerce'

    def ready(self):
        import ecommerce_projec.ecommerce.signals.auth_user_token
