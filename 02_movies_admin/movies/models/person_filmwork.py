from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import UUIDMixin


class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE,
                               verbose_name=_('person'))
    role = models.CharField(_('role'), max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('person')
        verbose_name_plural = _('persons')
