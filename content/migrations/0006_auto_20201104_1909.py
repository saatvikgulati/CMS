# Generated by Django 3.1.3 on 2020-11-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20201104_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='body',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='content',
            name='summary',
            field=models.TextField(max_length=60),
        ),
    ]