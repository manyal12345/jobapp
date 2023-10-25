# Generated by Django 4.2.6 on 2023-10-20 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_location_jobpost_location"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=200)),
                ("company", models.CharField(max_length=200)),
                ("designation", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="jobpost",
            name="author",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.author"
            ),
        ),
    ]
