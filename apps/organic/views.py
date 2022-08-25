from django.http import HttpResponse
from django.shortcuts import render
import logging

from apps.base.utils.send_email import Email


logger = logging.getLogger(__name__)

# Create your views here.
def hello(request):
    return HttpResponse("Hello From Organic Grgeen")

def sendEmail(request):
    logger.info(f"send_alert_notification args: {locals()}")
    try:
        body="This is the test body"
        subject="Test Subject"
        email = Email(
            body=body,
            subject=subject,
            to=["prabhatandkiran@gmail.com"],
            cc=[]
        )
        email.send_template_email()
        return HttpResponse("Test Email send successfully")
    except Exception as e:
        logger.info(f'Email alert exeption {str(e)}')
    return None
