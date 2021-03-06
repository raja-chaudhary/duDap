# Generated by Django 3.2.6 on 2021-11-09 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0003_auto_20211105_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trait',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trait',
            name='trait_type',
            field=models.CharField(choices=[('POSITIVE', 'Positive Trait'), ('NEGATIVE', 'Negative Trait')], default='POSITIVE', max_length=20),
        ),
    ]
