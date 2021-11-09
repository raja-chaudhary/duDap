from django.db import models
import datetime
from django.contrib.auth.models import User
# from django_cryptography.fields import encrypt


# Create your models here.
TRAIT_CHOICES = (
    ('POSITIVE', 'Positive Trait'),
    ('NEGATIVE', 'Negative Trait')
)


class Trait(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    trait_type = models.CharField(
        max_length=20, choices=TRAIT_CHOICES, default='POSITIVE', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trait_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trait_user', null=True, blank=True)

    def __str__(self):
        return self.title
