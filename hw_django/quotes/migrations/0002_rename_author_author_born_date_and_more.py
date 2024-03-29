# Generated by Django 5.0.3 on 2024-03-21 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="author",
            new_name="born_date",
        ),
        migrations.RenameField(
            model_name="author",
            old_name="tags",
            new_name="born_location",
        ),
        migrations.RenameField(
            model_name="author",
            old_name="text",
            new_name="description",
        ),
        migrations.AddField(
            model_name="author",
            name="fullname",
            field=models.CharField(
                default=datetime.datetime(
                    2024, 3, 21, 20, 51, 11, 412518, tzinfo=datetime.timezone.utc
                ),
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
