
"""
This is our TemplateForm.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from caesar.models.template import Template


class TemplateForm(forms.ModelForm):
    """
    """
    class Meta:
        """
        """
        model = Template
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Make some fields required.
        :param args:
        :param kwargs:
        """
        super(TemplateForm, self).__init__(*args, **kwargs)
        self.fields['reference'].label = _("Reference")
        self.fields['subject'].label = _("Subject")
        self.fields['content'].label = _("Content")
        self.fields['format'].label = _("Template format")


class CreateTemplateForm(forms.ModelForm):
    """
    """
    class Meta:
        """
        """
        model = Template
        fields = ['reference', 'subject', 'content', 'format']

    def __init__(self, *args, **kwargs):
        """
        Make some fields required.
        :param args:
        :param kwargs:
        """
        super(CreateTemplateForm, self).__init__(*args, **kwargs)
        self.fields['reference'].required = True
        self.fields['subject'].required = True
        self.fields['content'].required = True
        self.fields['format'].required = True

        self.fields['reference'].label = _("Reference")
        self.fields['subject'].label = _("Subject")
        self.fields['content'].label = _("Content")
        self.fields['format'].label = _("Template format")


class SearchTemplateForm(forms.Form):
    reference = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("example_of_reference_html")}),
                                max_length=50, required=False)
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Subject")}),
                              max_length=100, required=False)
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Content")}),
                              max_length=255, required=False)
    format = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _("Template format")}),
                             max_length=50, required=False)
