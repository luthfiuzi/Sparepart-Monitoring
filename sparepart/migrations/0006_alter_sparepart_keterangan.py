# Generated by Django 4.2.6 on 2023-12-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0005_karyawan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='keterangan',
            field=models.TextField(blank=True, null=True),
        ),
    ]
