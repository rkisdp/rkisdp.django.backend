# Generated by Django 3.2.7 on 2021-10-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("portfolio", "0003_skill")]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("create_date", models.DateTimeField(auto_now_add=True, verbose_name="Created At")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="Modified At")),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Is Instance marked deleted"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Instance marked Active"),
                ),
                ("name", models.CharField(max_length=64, verbose_name="Role name")),
            ],
            options={"verbose_name": "Role", "verbose_name_plural": "Roles"},
        )
    ]
