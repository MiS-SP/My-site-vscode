# Generated by Django 3.2.7 on 2021-11-10 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_pf_projs_date_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='pf_projs',
            name='date_creation',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
