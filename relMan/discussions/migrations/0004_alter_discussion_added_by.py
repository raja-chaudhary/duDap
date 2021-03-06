# Generated by Django 3.2.6 on 2021-09-07 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussions', '0003_alter_discussion_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='added_by',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
