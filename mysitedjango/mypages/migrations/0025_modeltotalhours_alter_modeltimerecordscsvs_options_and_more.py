# Generated by Django 4.1.2 on 2022-10-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mypages", "0024_rename_modeltimerecordscsv_modeltimerecordscsvs"),
    ]

    operations = [
        migrations.CreateModel(
            name="modeltotalhours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=200)),
                ("totalminutes", models.FloatField()),
                ("totalhours", models.FloatField()),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.AlterModelOptions(
            name="modeltimerecordscsvs",
            options={"ordering": ("id",)},
        ),
        migrations.AlterField(
            model_name="modeltimerecordscsvs",
            name="billable",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="modeltimerecordscsvs",
            name="code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="modeltimerecordscsvs",
            name="user",
            field=models.CharField(max_length=100),
        ),
    ]
