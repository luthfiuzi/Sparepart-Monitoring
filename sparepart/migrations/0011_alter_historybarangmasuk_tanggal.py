# Generated by Django 4.2.6 on 2023-12-14 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0010_historybarangmasuk_jumlah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historybarangmasuk',
            name='tanggal',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
