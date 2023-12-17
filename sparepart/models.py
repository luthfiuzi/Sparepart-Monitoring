from django.db import models
from django.utils import timezone

# Create your models here.

class Merk(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
    
class SparePart(models.Model):
    nama = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    merk = models.ForeignKey(Merk, on_delete=models.PROTECT, blank=True, null=True)
    rak = models.CharField(max_length=255)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        # show id, name
        return "{} - {}".format(self.id, self.nama)

class Karyawan(models.Model):
    nama = models.CharField(max_length=255)
    nik = models.IntegerField()
    
    def __str__(self):
        return self.nama
    
class HistoryBarangMasuk(models.Model):
    tanggal = models.DateField(default=timezone.now)
    sparepart = models.ForeignKey(SparePart, on_delete=models.PROTECT)
    karyawan = models.ForeignKey(Karyawan, on_delete=models.PROTECT)
    jumlah = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class HistoryBarangKeluar(models.Model):
    tanggal = models.DateField(default=timezone.now)
    sparepart = models.ForeignKey(SparePart, on_delete=models.PROTECT)
    karyawan = models.ForeignKey(Karyawan, on_delete=models.PROTECT)
    jumlah = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)