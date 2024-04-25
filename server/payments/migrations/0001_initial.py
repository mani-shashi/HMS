# Generated by Django 5.0 on 2024-01-10 09:08

import datetime
import payments.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bill",
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
                (
                    "bill_type",
                    models.CharField(
                        choices=[
                            ("electricity", "Electricity"),
                            ("water", "Water"),
                            ("groceries", "groceries"),
                            ("other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                ("amount", models.FloatField()),
                (
                    "bill_date",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 1, 10, 9, 8, 25, 893665, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "due_date",
                    models.DateField(default=payments.models.default_due_date),
                ),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("paid", "Paid")],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("items", models.JSONField(blank=True, default=list)),
            ],
        ),
    ]