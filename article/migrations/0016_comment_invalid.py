# Generated by Django 2.0.2 on 2018-03-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_article_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='invalid',
            field=models.CharField(choices=[('Y', '是'), ('N', '否')], default='N', max_length=64),
        ),
    ]
