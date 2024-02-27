# Generated by Django 4.2.4 on 2023-11-24 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("billing", "0001_initial"),
        ("checklists", "0001_initial"),
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="document",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice",
                to="documents.document",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="submissions",
            field=models.ManyToManyField(to="core.submission"),
        ),
        migrations.AddField(
            model_name="checklistpayment",
            name="checklists",
            field=models.ManyToManyField(to="checklists.checklist"),
        ),
        migrations.AddField(
            model_name="checklistpayment",
            name="document",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="checklist_payment",
                to="documents.document",
            ),
        ),
        migrations.AddField(
            model_name="checklistbillingstate",
            name="checklist",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="billing_state",
                to="checklists.checklist",
            ),
        ),
    ]