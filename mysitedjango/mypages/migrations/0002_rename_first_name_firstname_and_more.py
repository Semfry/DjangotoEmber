# Generated by Django 4.0.5 on 2022-07-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mypages", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="First_name",
            new_name="Firstname",
        ),
        migrations.RenameModel(
            old_name="Last_name",
            new_name="Lastname",
        ),
    ]
