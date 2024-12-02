from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    def ready(self):
        from .load_data_on_startup import load_data_if_needed
        load_data_if_needed()
