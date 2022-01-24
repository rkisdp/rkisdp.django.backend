# Generated by Django 3.2.7 on 2021-09-26 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("common", "0003_auto_20210904_1846")]

    operations = [
        migrations.CreateModel(
            name="ActivityConfig",
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
                (
                    "activity_name",
                    models.CharField(
                        choices=[
                            ("ACCOUNTS_USER_REGISTER", "Accounts User Register"),
                            ("ACCOUNTS_USER_LOGIN", "Accounts User Login"),
                            ("ACCOUNTS_USER_FORGET_PASSWORD", "Accounts User Forget Password"),
                            ("ACCOUNTS_USER_UPDATE", "Accounts User Update"),
                            ("ACCOUNTS_USER_PHONE_UPDATE", "Accounts User Phone Update"),
                            ("ACCOUNT_USER_LOGIN_OTP", "Accounts User Login OTP"),
                        ],
                        max_length=64,
                        unique=True,
                        verbose_name="Activity Name",
                    ),
                ),
            ],
            options={"verbose_name": "Activity Config", "verbose_name_plural": "Activity Configs"},
        ),
        migrations.CreateModel(
            name="NotificationTemplate",
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
                (
                    "name",
                    models.CharField(max_length=64, verbose_name="Notification template name"),
                ),
                (
                    "notification_type",
                    models.CharField(
                        choices=[
                            ("EMAIL", "Email Notification"),
                            ("SMS", "SMS Notification"),
                            ("PUSH", "Push Notification"),
                        ],
                        max_length=8,
                        verbose_name="Notification Type",
                    ),
                ),
                ("subject", models.TextField(verbose_name="Notification Subject")),
                ("content", models.TextField(verbose_name="Notification Content")),
            ],
            options={
                "verbose_name": "Notification Template",
                "verbose_name_plural": "Notification Templates",
            },
        ),
        migrations.AlterField(
            model_name="notification",
            name="type",
            field=models.CharField(
                choices=[
                    ("EMAIL", "Email Notification"),
                    ("SMS", "SMS Notification"),
                    ("PUSH", "Push Notification"),
                ],
                default="PUSH",
                max_length=32,
                verbose_name="Type of notification",
            ),
        ),
        migrations.AddIndex(
            model_name="notificationtemplate",
            index=models.Index(fields=["notification_type"], name="common_noti_notific_d8c2df_idx"),
        ),
        migrations.AddField(
            model_name="activityconfig",
            name="email_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="email_template_activity_configs",
                to="common.notificationtemplate",
                verbose_name="Email Template",
            ),
        ),
        migrations.AddField(
            model_name="activityconfig",
            name="push_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="push_template_activity_configs",
                to="common.notificationtemplate",
                verbose_name="Push Template",
            ),
        ),
        migrations.AddField(
            model_name="activityconfig",
            name="sms_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sms_template_activity_configs",
                to="common.notificationtemplate",
                verbose_name="SMS Template",
            ),
        ),
    ]
