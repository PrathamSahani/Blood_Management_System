# Generated by Django 4.2.5 on 2023-10-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipe", "0003_remove_receipe_receipe_image_receipe_receipe_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipe",
            name="receipe_age",
            field=models.CharField(default="gfg", max_length=100),
        ),
    ]
