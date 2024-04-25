# Generated by Django 5.0 on 2024-01-10 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cleaners",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("aadhar_number", models.CharField(max_length=100)),
                ("cast", models.CharField(max_length=20)),
                ("emergency_contact", models.CharField(max_length=20)),
                ("salary", models.FloatField()),
                ("acc_number", models.CharField(blank=True, max_length=20)),
                ("ifsc_code", models.CharField(blank=True, max_length=20)),
                ("acc_holder_name", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Cooks",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("aadhar_number", models.CharField(max_length=100)),
                ("cast", models.CharField(max_length=20)),
                ("emergency_contact", models.CharField(max_length=20)),
                ("salary", models.FloatField()),
                ("experience", models.TextField(max_length=20)),
                ("acc_number", models.CharField(blank=True, max_length=20)),
                ("ifsc_code", models.CharField(blank=True, max_length=20)),
                ("acc_holder_name", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Guards",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("aadhar_number", models.CharField(max_length=100)),
                ("cast", models.CharField(max_length=20)),
                ("emergency_contact", models.CharField(max_length=20)),
                ("salary", models.FloatField()),
                ("experience", models.TextField(max_length=20)),
                ("shift_start", models.TimeField()),
                ("shift_end", models.TimeField()),
                ("acc_number", models.CharField(blank=True, max_length=20)),
                ("ifsc_code", models.CharField(blank=True, max_length=20)),
                ("acc_holder_name", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Students",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("aadhar_number", models.CharField(max_length=100)),
                ("cast", models.CharField(max_length=20)),
                ("emergency_contact", models.CharField(max_length=20)),
                ("blood_group", models.CharField(max_length=10)),
                ("allergies", models.JSONField(default=list)),
                ("fees_payment_details", models.JSONField(default=list)),
                (
                    "hostel_room_number",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="rooms.room",
                        to_field="room_number",
                    ),
                ),
            ],
        ),
    ]
