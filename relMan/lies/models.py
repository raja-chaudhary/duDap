from django.db import models
import datetime
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

# Create your models here.


class Lie(models.Model):
    title = encrypt(models.CharField(max_length=500))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    lie_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lie_user', null=True, blank=True)

    def __str__(self):
        return self.title
