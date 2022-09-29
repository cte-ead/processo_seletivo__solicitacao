from django.utils.translation import gettext as _
from django.db.models import Model
from django.contrib.admin import register, display, ModelAdmin, StackedInline, TabularInline
from .models import UnidadeOrganizadora, Campus, Edital, TipoArquivo


#### 
# Inlines
####

# class CampusInline(StackedInline):
#     model: Model = Campus
#     extra: int = 0


#### 
# Admins
####

@register(UnidadeOrganizadora)
class UnidadeOrganizadoraAdmin(ModelAdmin):
    list_display = ['sigla_completa']
    search_fields = ['sigla_completa']


@register(Campus)
class CampusAdmin(ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@register(Edital)
class EditalAdmin(ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    
    # tipo = CharField(_('tipo de avaliação'), max_length=1, choices=TipoDeAvaliacao, default=TipoDeAvaliacao.CURRICULUM)
    # publico_alvo = CharField(_('público alvo'), max_length=1, choices=PublicoAlvo, default=PublicoAlvo.ALUNOS)
    # numero = CharField(_('número do edital'), max_length=255, unique=True)
    # ano = CharField(_('ano do edital'), max_length=255)
    # solicitante = ForeignKey(Usuario, on_delete=PROTECT)
    # unidade_organizadora = ForeignKey(UnidadeOrganizadora, on_delete=PROTECT)
    # campi = ManyToManyField(Campus)


# @register(Campus)
# class CampusAdmin(ModelAdmin):
#     list_display = ['sigla', 'descricao', 'ambiente', 'active']
#     list_filter = ['active', 'ambiente']
#     search_fields = ['sigla', 'descricao', 'suap_id']


# @register(Curso)
# class CursoAdmin(ModelAdmin):
#     list_display = ['codigo', 'nome']
#     search_fields = ['codigo', 'nome', 'suap_id', 'descricao']


# @register(Turma)
# class TurmaAdmin(ModelAdmin):
#     list_display = ['codigo', 'campus', 'ano_mes', 'periodo', 'curso', 'sigla', 'turno']
#     list_filter = ['turno', 'ano_mes', 'periodo', 'campus', 'curso']
#     readonly_fields = ['ano_mes', 'periodo', 'curso', 'sigla', 'turno']
#     search_fields = ['codigo']


# @register(Componente)
# class ComponenteAdmin(ModelAdmin):
#     list_display = ['sigla', 'descricao', 'periodo']
#     list_filter = ['optativo', 'qtd_avaliacoes', 'periodo', 'tipo']
#     search_fields =  ['sigla', 'suap_id', 'descricao', 'descricao_historico']


# @register(Diario)
# class DiarioAdmin(ModelAdmin):
#     list_display = ['codigo', 'situacao', 'descricao', 'turma', 'componente']
#     list_filter = ['situacao']
#     search_fields =  ['codigo', 'suap_id', 'descricao', 'descricao_historico', 'sigla']


# @register(Polo)
# class PoloAdmin(ModelAdmin):
#     list_display = ['nome']
#     search_fields =  ['nome', 'suap_id']


# @register(Inscricao)
# class InscricaoAdfmin(ModelAdmin):
#     list_display = ['diario', 'usuario', 'papel', 'polo', 'active']
#     list_filter = ['active', 'papel', 'polo']
#     search_fields =  ['diario__codigo', 'usuario__username']
    
#     class Meta:
#         verbose_name = _("inscrição")
#         verbose_name_plural = _("inscrições")
#         ordering = ['diario', 'usuario']

#     def __str__(self):
#         return f'{self.diario} - {self.usuario}'
