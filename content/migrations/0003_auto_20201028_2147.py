# Generated by Django 3.1.2 on 2020-10-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20201023_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
