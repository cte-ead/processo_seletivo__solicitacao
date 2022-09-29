from import_export import resources
from .models import Campus, UnidadeOrganizadora, Edital


class CampusResource(resources.ModelResource):
    class Meta:
        model = Campus


class UnidadeOrganizadoraResource(resources.ModelResource):
    class Meta:
        model = UnidadeOrganizadora


class EditalResource(resources.ModelResource):
    class Meta:
        model = Edital
