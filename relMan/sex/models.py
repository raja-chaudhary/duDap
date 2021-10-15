from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Sex(models.Model):
    sex_count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sex_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sex_user', null=True, blank=True)

    def __str__(self):
        return 'add sex'
