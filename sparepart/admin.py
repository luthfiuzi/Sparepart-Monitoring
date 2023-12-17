from django.contrib import admin
from sparepart.models import Merk, SparePart, Karyawan, HistoryBarangMasuk, HistoryBarangKeluar

admin.site.register(Merk)
admin.site.register(SparePart)
admin.site.register(Karyawan)

class SparePartInline(admin.TabularInline):
    model = SparePart
    extra = 1

class KaryawanInline(admin.TabularInline):
    model = Karyawan
    extra = 1

class HistoryBarangMasukAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'sparepart', 'karyawan')
    list_filter = ('tanggal', 'sparepart', 'karyawan')

admin.site.register(HistoryBarangMasuk, HistoryBarangMasukAdmin)

class HistoryBarangKeluarAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'sparepart', 'karyawan')
    list_filter = ('tanggal', 'sparepart', 'karyawan')

admin.site.register(HistoryBarangKeluar, HistoryBarangKeluarAdmin)

# Register your models here.
