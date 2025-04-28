from django.contrib import admin
from .models import Piloto

#Acessar as informações do models na página de admin
admin.site.register(Piloto)