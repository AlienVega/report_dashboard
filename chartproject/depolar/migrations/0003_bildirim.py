# Generated by Django 4.2 on 2023-07-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depolar', '0002_alter_warehouseuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bildirim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metin', models.CharField(max_length=200)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
