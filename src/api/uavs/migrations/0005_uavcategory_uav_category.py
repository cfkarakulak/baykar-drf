# Generated by Django 4.1.3 on 2022-11-03 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("uavs", "0004_uav_brand"),
    ]

    operations = [
        migrations.CreateModel(
            name="UavCategory",
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
            ],
        ),
        migrations.AddField(
            model_name="uav",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="uav_category",
                to="uavs.uavcategory",
            ),
        ),
    ]
