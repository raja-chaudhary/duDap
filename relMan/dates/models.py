from django.db import models
import datetime
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


# Create your models here.
REMINDER_CHOICES = (
    ('one month', 'One Month Prior'),
    ('one week', 'One Week Prior'),
    ('two days', 'Two Days Prior'),
)


class Date(models.Model):
    title = encrypt(models.CharField(max_length=200))
    date = models.DateField(blank=True, default=datetime.date.today)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reminder = models.CharField(
        max_length=50, choices=REMINDER_CHOICES, default='one week')
    date_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='date_user', null=True, blank=True)

    def __str__(self):
        return self.title
