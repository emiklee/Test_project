from django.apps import AppConfig


class KafeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kafe'
    verbose_name = 'Кафе'

    def ready(self):
        import kafe.signals
