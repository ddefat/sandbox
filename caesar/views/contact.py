"""
This view is used to manage Contacts.
"""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView

from caesar.forms.contact import SearchContactForm, ContactForm, CreateContactForm
from caesar.models.contact import Contact


class ListContactView(ListView):
    """
    Displays the list of all contacts created for all visitors;
    which means that no login and no permissions are required.
    All contacts are presented with their related artist whom created the contact.
    """
    model = Contact
    form_class = SearchContactForm
    template_name = 'caesar/contact_list.html'

    def get_queryset(self):
        queryset = Contact.objects.all()
        if self.request.GET.get('receiver'):
            queryset = queryset.filter(subject__icontains=self.request.GET.get('receiver'))
        if self.request.GET.get('sender'):
            queryset = queryset.filter(subject__icontains=self.request.GET.get('sender'))
        if self.request.GET.get('content'):
            queryset = queryset.filter(content__icontains=self.request.GET.get('content'))
        if self.request.GET.get('subject'):
            queryset = queryset.filter(content__icontains=self.request.GET.get('subject'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListContactView, self).get_context_data(**kwargs)
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


class DetailContactView(DetailView):
    """
    Displays the detail of the selected contact.
    """
    model = Contact
    permission_required = 'caesar.view_contact'
    permission_denied_message = 'You do not have the permission to see this contact.'
    raise_exception = True

    form_class = ContactForm

    def get_form(self):
        form = self.form_class(instance=self.object)
        for field in form.fields:
            form.fields[field].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super(DetailContactView, self).get_context_data(**kwargs)
        return context


class AddContactView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    This view enable the Artist to create a new Contact.
    Permission to add a Contact for the related Artist only.
    """
    model = Contact
    template_name = "caesar/contact_create.html"
    permission_required = 'caesar.add_contact'
    permission_denied_message = 'You do not have the permission to add a new contact'
    raise_exception = True

    form_class = CreateContactForm

    def form_valid(self, form):
        """
        What to do with the valid form ?
          - Create the message (a.k.a Contact)
          - Send the email to the receiver
        :param form:
        :return: HttpResponse
        """
        contact = form.save(commit=False)
        contact.sender = self.request.user.username
        contact.save()
        subject = form.cleaned_data.get('subject')
        content = form.cleaned_data.get('content')
        receiver = User.objects.get(username=form.cleaned_data.get('receiver'))
        sender = self.request.user
        message = render_to_string('caesar/contact_email.html', {
            'sender': sender,
            'receiver': receiver,
            'content': content,
        })
        send_mail(subject=subject, message=message, from_email=sender.email, recipient_list=[receiver.email],
                  fail_silently=True)
        return super(AddContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse('caesar:contact_list')
