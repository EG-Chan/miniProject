# Generated by Django 4.1 on 2023-01-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("puzzleApp", "0002_alter_puzzle_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileUpload",
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
                ("imgfile", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]