from django.apps import AppConfig

from django.db.models.signals import pre_delete


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    def ready(self) -> None:
        print("Deleting previous registery")
        from .models import ServerAddress
        ServerAddress.objects.all().delete() # Delete all records from last session
