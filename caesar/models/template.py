"""
This model represents a Template.
"""

from django.db import models
from django.contrib import admin
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _


class TemplateAdmin(admin.ModelAdmin):
    """
    All fields are listed for the admin.Model
    """
    list_display = ['reference', 'subject', 'content', 'format']


class Template(models.Model):
    """
    """
    FORMAT_CHOICES = (
        ('PLAIN', _('plain')),
        ('HTML', 'HTML')
    )

    reference = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    content = TextField(blank=True)
    format = models.CharField(max_length=15, choices=FORMAT_CHOICES)

    def __str__(self):
        return self.reference
