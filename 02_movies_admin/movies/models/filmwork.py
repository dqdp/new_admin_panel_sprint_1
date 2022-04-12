from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import TimeStampedMixin, UUIDMixin


class Types(models.TextChoices):
    MOVIE = 'movie', _('movie')
    TV_SHOW = 'tv_show', _('tv_show')


class Filmwork(UUIDMixin, TimeStampedMixin):

    title = models.CharField(_('title'), max_length=320)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation_date'), null=True, blank=True)
    file_path = models.FileField(_('file'), blank=True, null=True,
                                 upload_to='movies/')
    rating = models.FloatField(_('rating'), null=True, blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField(_('type'),
                            max_length=20,
                            choices=Types.choices)

    genres = models.ManyToManyField('Genre', through='GenreFilmwork')
    persons = models.ManyToManyField('Person', through='PersonFilmWork')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        indexes = [
            models.Index(fields=['creation_date'], name='film_work_creation_date_idx'),
            models.Index(fields=['title'], name='film_work_title_idx')
        ]
        verbose_name = _('filmwork')
        verbose_name_plural = _('filmworks')
