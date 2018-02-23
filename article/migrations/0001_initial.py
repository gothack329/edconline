# Generated by Django 2.0.2 on 2018-02-23 14:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='小志', max_length=128)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=1024)),
                ('detail', tinymce.models.HTMLField()),
                ('tag', models.CharField(blank=True, max_length=128, null=True)),
                ('readtime', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'articles',
                'ordering': ['-publish_date'],
            },
        ),
    ]
