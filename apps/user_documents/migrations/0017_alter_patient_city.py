# Generated by Django 4.1.6 on 2023-04-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_documents', '0016_alter_patient_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(max_length=30),
        ),
    ]
