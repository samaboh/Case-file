# Generated by Django 3.2.21 on 2023-09-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0038_auto_20230928_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]