# Generated by Django 4.2 on 2023-07-03 09:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WareHouseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_warehouse_admin', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_warehouse', to=settings.AUTH_USER_MODEL)),
                ('ware_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='depolar.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='WareHouseInputData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ort_rulot_doluluğu', models.DecimalField(decimal_places=3, max_digits=10)),
                ('ms_rulot_doluluk', models.DecimalField(decimal_places=3, max_digits=10)),
                ('taze_rulot_doluluk', models.DecimalField(decimal_places=3, max_digits=10)),
                ('koli_rulot_doluluk', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_sayisi_toplam', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_sayisi_koli', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_sayisi_taze', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_sayisi_ms', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_sayisi_sehirici', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_sayisi_sehirdısı', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sefer_sayisi_toplam', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sefer_sayisi_sehirici', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sefer_sayisi_sehirdısı', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gerceklesen_km_toplam', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gerceklesen_km_sehirici', models.DecimalField(decimal_places=3, max_digits=10)),
                ('gerceklesen_km_sehidısı', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_maaliyeti_ort', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_maaliyeti_sehirici', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rulot_maaliyeti_sehirdısı', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sefer_maaliyeti_ort', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sefer_maaliyeti_sehirici', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sefer_maaliyeti_sehirdısı', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mazot_litre_fiyat', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tarih', models.DateField(default=datetime.date.today)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_warehouseinputdata', to=settings.AUTH_USER_MODEL)),
                ('ware_house', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='depolar.warehouse')),
            ],
        ),
    ]