from django.utils.translation import gettext as _
from django.db.models import Model
from django.contrib.admin import register, display, ModelAdmin, StackedInline, TabularInline
from import_export.admin import ImportExportModelAdmin
from .models import UnidadeOrganizadora, Campus, Edital, TipoArquivo


#### 
# Inlines
####

class TipoArquivoInline(StackedInline):
    model: Model = TipoArquivo
    extra: int = 0


#### 
# Admins
####

@register(UnidadeOrganizadora)
class UnidadeOrganizadoraAdmin(ImportExportModelAdmin):
    list_display = ['sigla_completa']
    search_fields = ['sigla_completa']


@register(Campus)
class CampusAdmin(ImportExportModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@register(Edital)
class EditalAdmin(ImportExportModelAdmin):
    list_display = ['identificacao', 'tipo', 'publico_alvo', 'solicitante', 'acoes']
    search_fields = ['numero', 'ano']
    list_filter = ['tipo', 'publico_alvo', 'ano', 'unidade_organizadora__sigla_completa']
    autocomplete_fields = ['solicitante', 'unidade_organizadora', 'campi']
    inlines = [TipoArquivoInline]
    
    def acoes(self, obj):
        return 'Baixar'
