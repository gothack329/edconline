# Generated by Django 2.0.2 on 2018-02-26 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20180226_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='mail',
        ),
    ]
