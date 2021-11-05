from .models import Date
from celery import shared_task
from datetime import date, timedelta, datetime
from django.core.mail import send_mail
from relMan import settings


# @shared_task(bind=True)
# def test_func(self):
#     return 'done'


@shared_task(bind=True)
def two_days_prior(self):
    qs = Date.objects.all()
    for item in qs:
        date_title = item.title
        mail_subject = 'Important Date Reminder | Dudap'
        message = 'This is to remind you that your date for: ' + \
            str(date_title) + ' is due in 2 days'
        to_email = item.date_user.email
        if (item.date - datetime.now().date()).days == 2:
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
    return "Done"


@shared_task(bind=True)
def week_prior(self):
    qs = Date.objects.all()
    for item in qs:
        date_title = item.title
        mail_subject = 'Important Date Reminder | Dudap'
        message = 'This is to remind you that your date for: ' + \
            str(date_title) + ' is due in 7 days'
        to_email = item.date_user.email
        if (item.date - datetime.now().date()).days == 7:
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
    return "Done"


@shared_task(bind=True)
def month_prior(self):
    qs = Date.objects.all()
    for item in qs:
        date_title = item.title
        mail_subject = 'Important Date Reminder | Dudap'
        message = 'This is to remind you that your date for: ' + \
            str(date_title) + ' is due in 30 days'
        to_email = item.date_user.email
        if (item.date - datetime.now().date()).days == 30:
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
    return "Done"
