# Generated by Django 4.1.2 on 2022-10-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mypages", "0022_alter_modeltimerecordscsv_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modeltimerecordscsv",
            name="minutes",
            field=models.FloatField(),
        ),
    ]
