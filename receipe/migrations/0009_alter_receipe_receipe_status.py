# Generated by Django 4.2.5 on 2023-10-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipe", "0008_receipe_receipe_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="receipe_status",
            field=models.CharField(
                blank=True, default="Pending", max_length=100, null=True
            ),
        ),
    ]
