# Generated by Django 2.0.2 on 2018-02-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_article_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='static/upload/'),
        ),
    ]
