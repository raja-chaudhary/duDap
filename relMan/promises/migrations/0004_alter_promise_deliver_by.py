# Generated by Django 3.2.6 on 2021-10-02 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promises', '0003_alter_promise_deliver_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promise',
            name='deliver_by',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
