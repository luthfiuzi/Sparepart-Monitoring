# Generated by Django 4.2.6 on 2023-12-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0009_alter_historybarangmasuk_tanggal'),
    ]

    operations = [
        migrations.AddField(
            model_name='historybarangmasuk',
            name='jumlah',
            field=models.IntegerField(default=0),
        ),
    ]
