# Generated by Django 3.2.7 on 2021-11-10 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_remove_pf_projs_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='pf_projs',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pf_projs',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pf_projs',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]