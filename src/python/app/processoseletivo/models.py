from django.utils.translation import gettext as _
from django.db.models import Model, PROTECT, ForeignKey, ManyToManyField
from django.db.models import CharField, TextField
from django_better_choices import Choices
from a4.models import Usuario


class UnidadeOrganizadora(Model):
    sigla_completa = CharField(_('tipo de avaliação'), help_text=_('Ex.: DG/ZL/RE/IFRN, PROEN/IFRN'))

    class Meta:
        verbose_name = _("unidade organizadora")
        verbose_name_plural = _("unidades organizadoras")
        ordering = ['sigla_completa']

    def __str__(self):
        return self.sigla_completa


class Campus(Model):
    nome = CharField(_('nome'), max_length=255)

    class Meta:
        verbose_name = _("campus")
        verbose_name_plural = _("campi")
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Edital(Model):

    class TipoDeAvaliacao(Choices):
        CURRICULUM = Choices.Value(_("Curriculum"), value='C')
        CURRICULUM_E_ENTREVISTA = Choices.Value(_("Curriculum + Entrevista"), value='CE')
        SORTEIO = Choices.Value(_("Sorteio"), value='S')
        ORDEM_DE_INSCRICAO = Choices.Value(_("Ordem de inscrição"), value='OI')


    class PublicoAlvo(Choices):
        ALUNOS = Choices.Value(_("Alunos"), value='A')
        # PESSOAL
        COLABORADORES = Choices.Value(_("Colaboradores"), value='C')
        INTERNOS = Choices.Value(_("Internos"), value='I')
    
    tipo = CharField(_('tipo de avaliação'), max_length=1, choices=TipoDeAvaliacao, default=TipoDeAvaliacao.CURRICULUM)
    publico_alvo = CharField(_('público alvo'), max_length=1, choices=PublicoAlvo, default=PublicoAlvo.ALUNOS)
    numero = CharField(_('número do edital'), max_length=255, unique=True)
    ano = CharField(_('ano do edital'), max_length=255)
    solicitante = ForeignKey(Usuario, on_delete=PROTECT)
    unidade_organizadora = ForeignKey(UnidadeOrganizadora, on_delete=PROTECT)
    campi = ManyToManyField(Campus)

    class Meta:
        verbose_name = _("edital")
        verbose_name_plural = _("editais")
        ordering = ['-ano', 'numero']

    def __str__(self):
        return f'{self.numero}/{self.ano}-{self.unidade_organizadora} ({self.tipo} para {self.publico_alvo})'

class TipoArquivo(Model):
    nome = CharField(_('nome'), max_length=255)
    descricao = TextField(_('descrição'))
    edital = ForeignKey(Edital, on_delete=PROTECT)

    class Meta:
        verbose_name = _("tipo de documento")
        verbose_name_plural = _("tipos de documentos")
        ordering = ['edital', 'nome']

    def __str__(self):
        return self.nome