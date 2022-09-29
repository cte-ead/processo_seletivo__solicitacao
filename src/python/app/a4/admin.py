from django.utils.translation import gettext as _
from django.contrib.admin import ModelAdmin, register, site, display 
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from .models import Usuario, Grupo
from .resources import UsuarioResource


site.unregister(Group)


@register(Grupo)
class GrupoAdmin(ModelAdmin):
    pass


@register(Usuario)
class UsuarioAdmin(ImportExportModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_superuser')
    search_fields = ['username', 'first_name', 'last_name', 'email']
    resource_class = UsuarioResource
    fieldsets = [
        (None, {"fields": ['username', 'email'],}),
        (_('Auth'), {"fields": ['is_active', 'is_superuser', 'groups'],}),
        (_('Dates'), {"fields": ['date_joined', 'first_login', 'last_login'],}),
    ]
