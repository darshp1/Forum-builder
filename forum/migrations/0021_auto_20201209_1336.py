# Generated by Django 3.1.4 on 2020-12-09 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0020_reply_is_deleted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-is_pinned', '-published_date']},
        ),
    ]
