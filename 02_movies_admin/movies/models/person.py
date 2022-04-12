from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import TimeStampedMixin, UUIDMixin


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        indexes = [
            models.Index(fields=['full_name'], name='person_full_name_idx')
        ]
        verbose_name = _('person')
        verbose_name_plural = _('persons')
