from django.db import models

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
    keterangan = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.nama, self.jumlah)
    
