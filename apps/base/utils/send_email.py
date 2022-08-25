import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

logger = logging.getLogger(__name__)


class Email:

    def __init__(self, body, subject, to, cc=None):
        self.body = body
        self.subject = subject
        self.to = to
        self.cc = cc

    def send_excel_on_email(self, file_list) -> None:
        # file_list must be list of dict
        """Send Email with one or more than one attached excel files"""
        try:
            from_email = settings.EMAIL_HOST_USER
            backend = EmailBackend(
                host='smtp.gmail.com',
                port='587',
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,               
                use_tls=True,
                fail_silently=False
            )
            msg = EmailMessage(
                subject=self.subject,
                body=self.body,
                from_email=f'Support Pelocal {from_email}',
                to=self.to,
                cc=self.cc,
                connection=backend
            )

            msg.content_subtype = 'html'
            for file in file_list:
                msg.attach(
                    filename=f"{file['name']}.xlsx",
                    content=file['file'].getvalue(),
                    mimetype='application/vnd.openxmlformats-'
                             'officedocument.spreadsheetml.sheet'
                )
            msg.send(fail_silently=False)
        except Exception as e:
            logger.info(f"Send email report error {e}")

    def send_template_email(self) -> None:
        # file_list must be list of dict
        """Send Email with one or more than one attached excel files"""
        try:
            from_email = settings.EMAIL_HOST_USER
            backend = EmailBackend(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                password=settings.EMAIL_HOST_PASSWORD,
                username=settings.EMAIL_HOST_USER,
                use_tls=True,
                fail_silently=False
            )
            msg = EmailMessage(
                subject=self.subject,
                body=self.body,
                from_email=f'Notification {from_email}',
                to=self.to,
                cc=self.cc,
                connection=backend
            )

            msg.content_subtype = 'html'
            msg.send(fail_silently=False)
        except Exception as e:
            logger.info(f"Send email report error {e}")

    def send_attachment_email(self, file_list) -> None:
        # file_list must be list of dict
        """Send Email with one or more than one attached excel files"""
        try:
            from_email = settings.EMAIL_HOST_USER
            backend = EmailBackend(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                password=settings.EMAIL_HOST_PASSWORD,
                username=settings.EMAIL_HOST_USER,
                use_tls=True,
                fail_silently=False
            )
            msg = EmailMessage(
                subject=self.subject,
                body=self.body,
                from_email=f'Notification {from_email}',
                to=self.to,
                cc=self.cc,
                connection=backend
            )

            msg.content_subtype = 'html'
            for file in file_list:
                msg.attach(
                    filename=f"{file['name']}.xlsx",
                    content=file['file'].getvalue(),
                    mimetype='application/vnd.openxmlformats-'
                             'officedocument.spreadsheetml.sheet'
                )
            msg.send(fail_silently=False)
        except Exception as e:
            logger.info(f"Send email report error {e}")
