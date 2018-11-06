"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from caesar.views import products, send_mail
from caesar.views import category
from caesar.views import contact
from caesar.views import template

urlpatterns = [

    url(r'^add$', products.product_add, name='product_add'),
    url(r'^update/(?P<pk>\d+)$', products.product_update, name='product_update'),
    url(r'^delete/(?P<pk>\d+)$', products.product_delete, name='product_delete'),
    url(r'^list$', products.products_page, name='products_list'),
    url(r'^detail/(?P<pk>\d+)$', products.product_detail, name='product_detail'),

    url(r'^category/add$', category.AddCategoryView.as_view(), name='category_add'),
    url(r'^category/update/(?P<pk>\d+)$', category.UpdateCategoryView.as_view(), name='category_update'),
    url(r'^category/delete/(?P<pk>\d+)$', category.DeleteCategoryView.as_view(), name='category_delete'),
    url(r'^category/list$', category.ListCategoryView.as_view(), name='category_list'),

    url(r'^contact/add$', contact.AddContactView.as_view(), name='contact_add'),
    url(r'^contact/list$', contact.ListContactView.as_view(), name='contact_list'),

    url(r'^template/add$', template.AddTemplateView.as_view(), name='template_add'),
    url(r'^template/detail/(?P<pk>\d+)$', template.DetailTemplateView.as_view(), name='template_detail'),
    url(r'^template/update/(?P<pk>\d+)$', template.UpdateTemplateView.as_view(), name='template_update'),
    url(r'^template/delete/(?P<pk>\d+)$', template.DeleteTemplateView.as_view(), name='template_delete'),
    url(r'^template/list$', template.ListTemplateView.as_view(), name='template_list'),

    url(r'^send_mail/test/(?P<pk>\d+)$', send_mail.send_test_mail, name='send_test_mail'),

]
