# Generated by Django 2.0.2 on 2018-03-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20180228_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
