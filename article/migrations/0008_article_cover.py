# Generated by Django 2.0.2 on 2018-02-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20180224_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
