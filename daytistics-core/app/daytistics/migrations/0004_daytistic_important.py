# Generated by Django 5.1 on 2024-08-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daytistics', '0003_remove_activityentry_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='daytistic',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
