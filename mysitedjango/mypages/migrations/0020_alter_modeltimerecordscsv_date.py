# Generated by Django 4.1.2 on 2022-10-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mypages", "0019_modeltimerecordscsv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modeltimerecordscsv",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
