# Generated by Django 4.1 on 2023-01-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ballmungApp", "0003_alter_rankinfo_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rankinfo",
            name="regiDate",
            field=models.CharField(max_length=100),
        ),
    ]