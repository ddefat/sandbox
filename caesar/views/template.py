"""
This view is used to manage Templates.
"""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from caesar.forms.template import SearchTemplateForm, TemplateForm, CreateTemplateForm
from caesar.models import Template


class ListTemplateView(ListView):
    """
    Displays the list of all templates created;
    """
    model = Template
    form_class = SearchTemplateForm
    template_name = 'caesar/template_list.html'

    def get_queryset(self):
        queryset = Template.objects.all()
        if self.request.GET.get('reference'):
            queryset = queryset.filter(subject__icontains=self.request.GET.get('reference'))
        if self.request.GET.get('subject'):
            queryset = queryset.filter(subject__icontains=self.request.GET.get('subject'))
        if self.request.GET.get('content'):
            queryset = queryset.filter(content__icontains=self.request.GET.get('content'))
        if self.request.GET.get('format'):
            queryset = queryset.filter(content__icontains=self.request.GET.get('format'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListTemplateView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(
            data={
                'subject': self.request.GET.get('subject'),
                'content': self.request.GET.get('content'),
                'sender': self.request.GET.get('sender')
            })
        get_copy = self.request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
        context['parameters'] = parameters
        return context


class DetailTemplateView(DetailView):
    """
    Displays the detail of the selected template.
    """
    model = Template
    permission_required = 'caesar.view_template'
    permission_denied_message = 'You do not have the permission to see this template.'
    raise_exception = True

    form_class = TemplateForm

    def get_form(self):
        form = self.form_class(instance=self.object)
        for field in form.fields:
            form.fields[field].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super(DetailTemplateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class AddTemplateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    This view enable the User to create a new Template.
    """
    model = Template
    template_name = "caesar/template_create.html"
    permission_required = 'caesar.add_template'
    permission_denied_message = 'You do not have the permission to add a new template'
    raise_exception = True

    form_class = CreateTemplateForm

    def get_success_url(self):
        return reverse('caesar:template_list')


class UpdateTemplateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    This view enable the User to update an existing Template.
    """
    model = Template
    template_name = 'caesar/template_form.html'
    permission_required = 'caesar.change_template'  # Look in database, the table auth.permission.
    permission_denied_message = 'You dont have the permission to change a template.'
    raise_exception = False  # Redirect to sign in page by default (login_url in settings)

    form_class = TemplateForm

    def get_success_url(self):
        return reverse('caesar:template_detail', kwargs={'pk': self.object.id})


class DeleteTemplateView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    This view enable the Artist to delete an existing Artwork.
    Permission to delete a Artwork for the related Artist only.
    """
    model = Template
    success_url = reverse_lazy('caesar:template_list')
    template_name = "caesar/template_confirm_delete.html"
    permission_required = 'caesar.delete_template'  # Look in database, the table auth.permission.
    permission_denied_message = 'You dont have the permission to delete a template.'
    raise_exception = False  # Redirect to sign in page by default (login_url in settings)
