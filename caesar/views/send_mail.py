"""
"""
from django.shortcuts import redirect
from django.template import Context, Template as TemplateEngine
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.urls import reverse

from caesar.models import Template


def send_test_mail(request, pk):

    sender = request.user
    receiver = request.user
    template = Template.objects.get(pk=pk)

    if template.format == 'HTML':

        message = TemplateEngine(template.content).render(Context({
            'sender': sender,
            'receiver': receiver
        }))

        email = EmailMessage(template.subject, message, from_email=sender.email, to=[receiver.email])
        #email.content_subtype = 'html'

    else:

        message = render_to_string(template.content, {
            'sender': sender,
            'receiver': receiver
        })

        email = EmailMessage(template.subject, message, from_email=sender.email, to=[receiver.email])

    email.send()

    return redirect(reverse('caesar:template_list'))
