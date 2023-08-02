# Generated by Django 4.2 on 2023-08-01 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('depolar', '0019_alter_warehouseuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_warehouse', to=settings.AUTH_USER_MODEL),
        ),
    ]
