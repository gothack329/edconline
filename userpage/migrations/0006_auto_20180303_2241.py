# Generated by Django 2.0.2 on 2018-03-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0005_auto_20180302_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='static/avatar/default.png', null=True, upload_to='static/avatar/'),
        ),
    ]
