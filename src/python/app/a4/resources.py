from import_export import resources
from .models import Usuario, Group


class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
