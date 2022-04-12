from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import UUIDMixin


class Roles(models.TextChoices):
    DIRECTOR = 'director', _('director')
    WRITER = 'writer', _('writer')
    ACTOR = 'actor', _('actor')


class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person',
                               on_delete=models.CASCADE,
                               verbose_name=_('person'))
    role = models.CharField(_('role'),
                            max_length=20,
                            choices=Roles.choices)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        constraints = [
            models.UniqueConstraint(fields=['film_work', 'person'],
                                    name='film_work_person_uniq')
        ]
        indexes = [
            models.Index(fields=['film_work', 'person'],
                         name='film_work_person_idx')
        ]
        verbose_name = _('person')
        verbose_name_plural = _('persons')
