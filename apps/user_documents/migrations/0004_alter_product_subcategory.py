# Generated by Django 4.1.6 on 2023-05-16 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_documents', '0003_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Resortada', 'OTP Resortada'), ('Corta', 'OTP Corta'), ('Larga', 'OTP Larga'), ('Deportivas', 'Plantillas Deportivas'), ('Ortopédicas', 'Plantillas Ortopédicas'), ('Diabéticas', 'Plantillas Diabéticas')], max_length=50, null=True),
        ),
    ]
