# Generated by Django 4.1.6 on 2023-03-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_documents', '0002_remove_patient_drawbacks_remove_patient_new_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='reported_drawbacks',
            field=models.BooleanField(),
        ),
    ]