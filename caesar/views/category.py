from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView

from caesar.models.category import Category


class ListCategoryView(LoginRequiredMixin, ListView):
    model = Category
    fields = "__all__"


class AddCategoryView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy('products:category_list')
    permission_required = 'caesar.add_category' #Look in database, the table auth.permission. ...
    permission_denied_message = 'You dont have the permission to add a new category'
    raise_exception = True #Dont redirect, send 403 Forbidden


class UpdateCategoryView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    fields = "__all__"
    permission_required = 'caesar.change_category' #Look in database, the table auth.permission. ...
    permission_denied_message = 'You dont have the permission to change a category'
    raise_exception = True #Dont redirect, send 403 Forbidden


class DeleteCategoryView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('products:category_list')
    permission_required = 'caesar.delete_category' #Look in database, the table auth.permission. ...
    permission_denied_message = 'You dont have the permission to delete a category'
    raise_exception = True #Dont redirect, send 403 Forbidden