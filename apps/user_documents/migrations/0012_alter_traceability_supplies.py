# Generated by Django 4.1.6 on 2023-03-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_documents', '0011_alter_traceability_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traceability',
            name='supplies',
            field=models.CharField(max_length=50),
        ),
    ]