# Generated by Django 4.1.6 on 2023-02-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_d', '0002_project_class_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='class_attribute',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
