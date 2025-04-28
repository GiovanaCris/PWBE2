from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

#Campos do admin
class UsuarioDSAdmin(UserAdmin):
    list_display = ('username', 'idade', 'escolaridade', 'endereco')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('animais', 'biografia', 'telefone')}),
    )
admin.site.register(UsuarioDS16, UsuarioDSAdmin)