# Generated by Django 4.2.3 on 2023-07-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("customer_first_name", models.CharField(max_length=255)),
                ("customer_last_name", models.CharField(max_length=255)),
                ("customer_address", models.TextField()),
                ("customer_contact_number", models.CharField(max_length=255)),
                ("shop_name", models.CharField(max_length=255)),
                ("shop_address", models.CharField(max_length=255)),
                ("schedule", models.DateTimeField()),
            ],
        ),
    ]
