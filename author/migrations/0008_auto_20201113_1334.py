# Generated by Django 3.1.3 on 2020-11-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0007_auto_20201104_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
    ]
