from django.core.exceptions import ValidationError
from django.db import models
from django.contrib import admin


def validate_first_letter(value):
    if not value[0].isalpha():
        raise ValidationError('The first caracter must be a letter')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'name', 'reference', 'price', 'created_date',)


class Product(models.Model):

    borrower = models.ForeignKey('auth.User', related_name='borrowed_products',
                                 blank=True, null=True, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', related_name='categories')
    name = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=25, blank=True, null=True,
                                 validators=[validate_first_letter])
    price = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    borrowed_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return  self.name
