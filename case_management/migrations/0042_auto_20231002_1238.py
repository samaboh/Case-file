# Generated by Django 3.2.21 on 2023-10-02 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0041_auto_20231002_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['label']},
        ),
        migrations.AddField(
            model_name='client',
            name='home_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_language', to='case_management.language'),
        ),
        migrations.AddField(
            model_name='client',
            name='translator_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator_language', to='case_management.language'),
        ),
    ]