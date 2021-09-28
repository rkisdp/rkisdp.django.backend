# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampable(models.Model):
    """
    Record timestamps of a Content.
    * Model instance is never deleted, its marked as deleted with is_deleted.
    """
    create_date = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True
    )
    modified_date = models.DateTimeField(
        verbose_name=_("Modified At"),
        auto_now=True
    )
    is_deleted = models.BooleanField(
        verbose_name=_("Is Instance marked deleted"),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Instance marked Active"),
        default=True
    )

    class Meta:
        abstract = True
