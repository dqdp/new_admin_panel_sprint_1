from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import UUIDMixin


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              verbose_name=_('genre'))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        constraints = [
            models.UniqueConstraint(fields=['film_work', 'genre'],
                                    name='film_work_genre_uniq')
        ]
        indexes = [
            models.Index(fields=['film_work', 'genre'],
                         name='film_work_genre_idx')
        ]
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
