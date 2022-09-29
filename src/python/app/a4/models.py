from django.utils.translation import gettext as _
from django.db.models import ForeignKey, PROTECT, CharField, DateTimeField
from django_better_choices import Choices
from django.contrib.auth.models import AbstractUser, Group


class Grupo(Group):
    pass


class Usuario(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
