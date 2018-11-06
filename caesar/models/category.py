
from django.db import models
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class Category(models.Model):

    name = models.CharField(max_length=100, default='none')

    def __str__(self):
        return self.name
