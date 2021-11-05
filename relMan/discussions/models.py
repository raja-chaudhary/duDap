from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


# Create your models here.


class Discussion(models.Model):
    title = encrypt(models.CharField(max_length=200))
    content = encrypt(models.TextField())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)

    def __str__(self):
        return self.title
