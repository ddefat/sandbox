"""
This model represents a Contact.
A Contact is a an Artist or Staff Member emailed by a Member.
"""

from django.db import models    # pylint: disable=import-error
from django.contrib import admin    # pylint: disable=import-error


class ContactAdmin(admin.ModelAdmin):   # pylint: disable=too-few-public-methods
    """
    All fields are listed for the admin.Model
    """
    list_display = ['receiver', 'subject', 'content', 'sender']


class Contact(models.Model):    # pylint: disable=too-few-public-methodsé
    """
    """
    receiver = models.ForeignKey('auth.User', related_name='receiver_user', null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=500, blank=True, null=True)
    sender = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.subject
