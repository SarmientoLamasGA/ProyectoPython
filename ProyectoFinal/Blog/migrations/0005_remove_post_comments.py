# Generated by Django 4.1.2 on 2022-12-10 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_comments_body_comment_alter_comments_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
