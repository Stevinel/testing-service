# Generated by Django 3.2.6 on 2021-08-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0003_auto_20210812_1918"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="points",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="question",
            name="max_points",
            field=models.IntegerField(),
        ),
    ]