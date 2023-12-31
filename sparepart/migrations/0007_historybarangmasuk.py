# Generated by Django 4.2.6 on 2023-12-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0006_alter_sparepart_keterangan'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryBarangMasuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('jumlah', models.IntegerField()),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sparepart.karyawan')),
                ('sparepart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sparepart.sparepart')),
            ],
        ),
    ]
