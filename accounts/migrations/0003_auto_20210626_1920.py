# Generated by Django 2.2.5 on 2021-06-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_author_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
    ]
