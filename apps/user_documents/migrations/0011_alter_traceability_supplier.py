# Generated by Django 4.1.6 on 2023-03-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_documents', '0010_alter_traceability_supplies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traceability',
            name='supplier',
            field=models.CharField(max_length=60),
        ),
    ]
