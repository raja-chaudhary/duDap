from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Promise(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deliver_by = models.DateField(null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    promise_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='promise_user', null=True, blank=True)

    def __str__(self):
        return self.title
