# Generated by Django 2.0.2 on 2018-02-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180224_0319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish_time']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_time']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='publish_date',
            new_name='publish_time',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='time',
            new_name='comment_time',
        ),
        migrations.AddField(
            model_name='article',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
