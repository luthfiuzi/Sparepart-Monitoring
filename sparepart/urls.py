from sparepart import views
from django.urls import path

app_name = "sparepart"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("sparepart/", views.SparePartView.as_view(), name="home"),
    path("sparepart/ajax/", views.SparePartAjaxView.as_view(), name="sparepart_ajax"),
    path("sparepart/create/", views.SparePartCreateView.as_view(), name="sparepart_create"),
    path("sparepart/update/<int:pk>/", views.SparePartUpdateView.as_view(), name="sparepart_update"),
    path("sparepart/delete/<int:pk>/", views.SparePartDeleteView.as_view(), name="sparepart_delete"),

    path("merk/", views.MerkView.as_view(), name="merk"),
    path("merk/ajax/", views.MerkAjaxView.as_view(), name="merk_ajax"),
    path("merk/create/", views.MerkCreateView.as_view(), name="merk_create"),
    path("merk/update/<int:pk>/", views.MerkUpdateView.as_view(), name="merk_update"),
    path("merk/delete/<int:pk>/", views.MerkDeleteView.as_view(), name="merk_delete"),

    path("karyawan/", views.KaryawanView.as_view(), name="karyawan"),
    path("karyawan/ajax/", views.KaryawanAjaxView.as_view(), name="karyawan_ajax"),
    path("karyawan/create/", views.KaryawanCreateView.as_view(), name="karyawan_create"),
    path("karyawan/update/<int:pk>/", views.KaryawanUpdateView.as_view(), name="karyawan_update"),
    path("karyawan/delete/<int:pk>/", views.KaryawanDeleteView.as_view(), name="karyawan_delete"),

    path("critical_stok/", views.CriticalStokView.as_view(), name="critical_stok"),
    path("critical_stok/ajax/", views.CriticalStokAjaxView.as_view(), name="critical_stok_ajax"),
  
    path("barang_masuk/", views.BarangMasukView.as_view(), name="barang_masuk"),
    path("barang_masuk/ajax/", views.BarangMasukAjaxView.as_view(), name="barang_masuk_ajax"),
    path("barang_masuk/create/", views.BarangMasukCreateView.as_view(), name="barang_masuk_create"),
    
    path("barang_keluar/", views.BarangMasukView.as_view(), name="barang_keluar"),
    path("barang_keluar/ajax/", views.BarangMasukAjaxView.as_view(), name="barang_keluar_ajax"),
    path("barang_keluar/create/", views.BarangMasukCreateView.as_view(), name="barang_keluar_create"),
]