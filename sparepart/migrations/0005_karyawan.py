# Generated by Django 4.2.6 on 2023-12-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0004_delete_karyawan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nik', models.IntegerField()),
            ],
        ),
    ]
