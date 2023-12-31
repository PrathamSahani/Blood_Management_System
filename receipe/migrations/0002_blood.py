# Generated by Django 4.2.5 on 2023-10-23 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("receipe", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blood",
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
                ("blood_name", models.CharField(max_length=100)),
                ("blood_description", models.TextField()),
                ("blood_image", models.ImageField(upload_to="blood")),
                (
                    "user1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
