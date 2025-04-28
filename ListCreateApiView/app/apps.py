from django.apps import AppConfig

#Configura uma aplicação Django que se chama 'app'
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
