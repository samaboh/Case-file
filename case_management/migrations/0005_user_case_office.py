# Generated by Django 3.2.4 on 2021-08-17 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0004_auto_20210817_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='case_office',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='users',
                to='case_management.caseoffice',
            ),
        ),
    ]