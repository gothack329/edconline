# Generated by Django 2.0.2 on 2018-03-04 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_comment_invalid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
