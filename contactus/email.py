from django.conf import settings
from django.core.mail import send_mail
from threading import Thread

from django.template.loader import render_to_string


class ContactUsEmail(Thread):

    def __init__(self, data):
        Thread.__init__(self)
        self.data = data

    def run(self) -> None:
        message = render_to_string('email/email_contacts.html', self.data)
        send_mail('Հետադարձ կապի նամակ', message, html_message=message, fail_silently=True,
                  recipient_list=[settings.EMAIL_HOST_USER], from_email=settings.EMAIL_HOST_USER)



