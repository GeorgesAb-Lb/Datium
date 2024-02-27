# Generated by Django 4.2.4 on 2023-12-04 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="trail",
            field=models.ManyToManyField(
                blank=True, related_name="future", to="workflow.token"
            ),
        ),
        migrations.AlterField(
            model_name="workflow",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="parent_workflow",
                to="workflow.token",
            ),
        ),
    ]