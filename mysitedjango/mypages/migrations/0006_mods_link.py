# Generated by Django 4.0.5 on 2022-07-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mypages", "0005_mods"),
    ]

    operations = [
        migrations.AddField(
            model_name="mods",
            name="link",
            field=models.URLField(default="admin/mypages/mods/"),
        ),
    ]
