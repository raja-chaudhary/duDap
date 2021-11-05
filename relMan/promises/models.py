from django.db import models
import datetime
from django.contrib.auth.models import User
from datetime import date
from django_cryptography.fields import encrypt


# Create your models here.


class Promise(models.Model):
    title = encrypt(models.CharField(max_length=200))
    content = encrypt(models.TextField())
    deliver_by = models.DateField(
        blank=True, default=datetime.date.today)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    promise_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='promise_user', null=True, blank=True)

    def __str__(self):
        return self.title

    # Adding the property to pass the context in the template to check if the date is overdue or not
    @property
    def is_past_due(self):
        return date.today() > self.deliver_by
