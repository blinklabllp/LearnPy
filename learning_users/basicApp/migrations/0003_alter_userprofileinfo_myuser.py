# Generated by Django 3.2.8 on 2021-10-23 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicApp', '0002_rename_user_userprofileinfo_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='myUser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
