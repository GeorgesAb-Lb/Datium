# Generated by Django 4.2.4 on 2023-11-24 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Checklist",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("completed", "Completed"),
                            ("review_ok", "Review OK"),
                            ("review_fail", "Review Failed"),
                            ("dropped", "Dropped"),
                        ],
                        default="new",
                        max_length=15,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChecklistBlueprint",
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
                ("slug", models.CharField(db_index=True, max_length=50, unique=True)),
                ("multiple", models.BooleanField(default=False)),
                ("reviewer_is_anonymous", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ChecklistQuestion",
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
                ("number", models.CharField(db_index=True, max_length=5)),
                ("index", models.IntegerField(db_index=True)),
                ("text", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("link", models.CharField(blank=True, max_length=100, null=True)),
                ("is_inverted", models.BooleanField(default=False)),
                ("requires_comment", models.BooleanField(default=False)),
                (
                    "blueprint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="checklists.checklistblueprint",
                    ),
                ),
            ],
            options={
                "ordering": ("blueprint", "index"),
            },
        ),
        migrations.CreateModel(
            name="ChecklistAnswer",
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
                ("answer", models.BooleanField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "checklist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="checklists.checklist",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="checklists.checklistquestion",
                    ),
                ),
            ],
            options={
                "ordering": ("question__blueprint", "question__index"),
            },
        ),
        migrations.AddField(
            model_name="checklist",
            name="blueprint",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="checklists",
                to="checklists.checklistblueprint",
            ),
        ),
        migrations.AddField(
            model_name="checklist",
            name="last_edited_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="edited_checklists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
