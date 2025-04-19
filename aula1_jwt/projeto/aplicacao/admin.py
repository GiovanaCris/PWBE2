from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDSAdmin(UserAdmin):
    list_display = ('username', 'idade', 'escolaridade', 'endereco')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('animais', 'biografia', 'telefone')}),
    )

    # add_fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('', 'edv', 'padrinho', 'apelido')}),
    # )

admin.site.register(UsuarioDS16, UsuarioDSAdmin)