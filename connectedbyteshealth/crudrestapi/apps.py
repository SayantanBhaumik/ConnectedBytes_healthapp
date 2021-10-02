from django.apps import AppConfig

#subclass of django.apps.AppConfig
#represents the Django app that we’ve just created with its configuration
class CrudrestapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crudrestapi'
