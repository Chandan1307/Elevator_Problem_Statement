# Generated by Django 4.2.2 on 2023-06-15 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("elevator", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="elevator",
            name="target_floor",
        ),
        migrations.AddField(
            model_name="elevator",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="elevator",
            name="direction",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="elevator",
            name="operational",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="elevator",
            name="status",
            field=models.CharField(
                choices=[("running", "Running"), ("stopped", "Stopped")],
                default="stopped",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="elevator",
            name="current_floor",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="UserRequest",
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
                ("requested_floor", models.IntegerField()),
                (
                    "elevator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elevator.elevator",
                    ),
                ),
            ],
        ),
    ]
