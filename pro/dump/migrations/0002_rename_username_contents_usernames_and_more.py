# Generated by Django 4.1 on 2022-10-06 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dump", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contents", old_name="username", new_name="usernames",
        ),
        migrations.RenameField(
            model_name="login", old_name="table_name", new_name="username",
        ),
    ]
