"""
This is our ContactForm.
A Contact is contains information to send to a member by another member.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from caesar.models.contact import Contact


class ContactForm(forms.ModelForm):
    """
    """
    class Meta:
        """
        """
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Make some fields required.
        :param args:
        :param kwargs:
        """
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].label = _("Receiver username")
        self.fields['subject'].label = _("Subject")
        self.fields['content'].label = _("Content")
        self.fields['sender'].label = _("Sender username")


class CreateContactForm(forms.ModelForm):
    """
    """
    class Meta:
        """
        """
        model = Contact
        fields = ['receiver', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        """
        Make some fields required.
        :param args:
        :param kwargs:
        """
        super(CreateContactForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].required = True
        self.fields['subject'].required = True
        self.fields['content'].required = True

        self.fields['receiver'].label = _("Receiver username")
        self.fields['subject'].label = _("Subject")
        self.fields['content'].label = _("Content")


class SearchContactForm(forms.Form):
    receiver = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Receiver username")}),
                               max_length=50, required=False)
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Subject")}),
                              max_length=100, required=False)
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Content")}),
                              max_length=255, required=False)
    sender = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Sender username")}),
                             max_length=50, required=False)
