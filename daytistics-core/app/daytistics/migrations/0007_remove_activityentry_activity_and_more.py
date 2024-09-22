# Generated by Django 5.1.1 on 2024-09-21 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0002_activityentry_activitytype"),
        ("daytistics", "0006_daytistic_important"),
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activityentry",
            name="activity",
        ),
        migrations.RemoveField(
            model_name="activityentry",
            name="daytistic",
        ),
        migrations.RemoveField(
            model_name="daytistic",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="daytistic",
            name="important",
        ),
        migrations.RemoveField(
            model_name="daytistic",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="daytistic",
            name="activities",
            field=models.ManyToManyField(
                blank=True, related_name="daytistics", to="activities.activityentry"
            ),
        ),
        migrations.AddField(
            model_name="daytistic",
            name="diary",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="daytistic",
                to="diary.diaryentry",
            ),
        ),
    ]
