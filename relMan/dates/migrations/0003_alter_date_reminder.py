# Generated by Django 3.2.6 on 2021-10-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_date_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='reminder',
            field=models.CharField(choices=[('one month', 'One Month Prior'), ('one week', 'One Week Prior'), ('two days', 'Two Days Prior')], default='one week', max_length=50),
        ),
    ]
