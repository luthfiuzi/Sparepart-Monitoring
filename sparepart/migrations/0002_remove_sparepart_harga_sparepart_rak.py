# Generated by Django 4.2.6 on 2023-11-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparepart',
            name='harga',
        ),
        migrations.AddField(
            model_name='sparepart',
            name='rak',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
