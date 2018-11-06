
from django.contrib import admin

from caesar.models import Template
from caesar.models.contact import Contact, ContactAdmin
from caesar.models.product import Product, ProductAdmin
from caesar.models.category import Category, CategoryAdmin
from caesar.models.template import TemplateAdmin

admin.site.register(Category,
                    CategoryAdmin)

admin.site.register(Contact,
                    ContactAdmin)

admin.site.register(Product,
                    ProductAdmin)

admin.site.register(Template,
                    TemplateAdmin)
