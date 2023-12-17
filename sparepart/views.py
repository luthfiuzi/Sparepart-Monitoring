from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from sparepart.models import Merk, SparePart, Karyawan, HistoryBarangMasuk, HistoryBarangKeluar
from ajax_datatable.views import AjaxDatatableView
from django.utils.html import format_html
from sparepart.forms import BarangMasukForm, BarangKeluarForm
class IndexView(TemplateView):
    template_name = "sparepart/index.html"

class SparePartView(TemplateView):
    template_name = "sparepart/sparepart_index.html"

class SparePartAjaxView(AjaxDatatableView):
    model = SparePart
    initial_order = [["nama", "asc"], ]
    title = "SparePart"
    max_display_length = 50
    search_values_separator = " "
    length_menu = [[10, 25, 50, -1], [10, 25, 50, "All"]]

    def get_column_defs(self, request):
        column_defs = [
        {'name': 'id', 'visible': False, },
        {'name': 'nama', 'visible': True, },
        {'name': 'merk', 'visible': True, 'foreign_field': 'merk__nama', },
        {'name': 'jumlah', 'visible': True, },
        {'name': 'rak', 'visible': True, },
        {"name": "status", "visible": True, "searchable": False, "orderable": False, "title": "Status"},
        {'name': 'Aksi', 'visible': True, 'searchable': False, 'orderable': False, 'title': 'Aksi' },
    ]
        return column_defs
    
    def customize_row(self, row, obj):
        row['Aksi'] = format_html(
            '<a href="/sparepart/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
            '<a href="/sparepart/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
            obj.pk
        )
        if obj.jumlah >= 2:
            row['status'] = format_html(
                '<span class="badge bg-success">Aman</span>'
            )
        elif obj.jumlah >= 1:
            row['status'] = format_html(
                '<span class="badge bg-warning">Hampir Habis</span>'
            )
        else:
            row['status'] = format_html(
                '<span class="badge bg-danger">Habis</span>'
            )
        return row
    
    def render_column(self, row, column):
        if column == 'aksi':
            return format_html(
                '<a href="/sparepart/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
                '<a href="/sparepart/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
                row.pk
            )
        else:
            return super(SparePartAjaxView, self).render_column(row, column)

class MerkView(TemplateView):
    template_name = "sparepart/merk.html"

class MerkAjaxView(AjaxDatatableView):
    model = Merk
    initial_order = [["nama", "asc"], ]
    title = "Merk"
    max_display_length = 50
    search_values_separator = " "
    length_menu = [[10, 25, 50, -1], [10, 25, 50, "All"]]   

    def get_column_defs(self, request):
        column_defs = [
        {'name': 'id', 'visible': False, },
        {'name': 'nama', 'visible': True, },
        {'name': 'Aksi', 'visible': True, 'searchable': False, 'orderable': False, 'title': 'Aksi' },
    ]
        return column_defs
    
    def customize_row(self, row, obj):
        row['Aksi'] = format_html(
            '<a href="/merk/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
            '<a href="/merk/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
            obj.pk
        )
        return row

    def render_column(self, row, column):
        if column == 'aksi':
            return format_html(
                '<a href="/merk/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
                '<a href="/merk/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
                row.pk
            )
        else:
            return super(MerkAjaxView, self).render_column(row, column)
        
class KaryawanView(TemplateView):
    template_name = "sparepart/karyawan.html"

class KaryawanAjaxView(AjaxDatatableView):
    model = Karyawan
    initial_order = [["nama", "asc"], ]
    title = "Karyawan"
    max_display_length = 50
    search_values_separator = " "
    length_menu = [[10, 25, 50, -1], [10, 25, 50, "All"]]

    def get_column_defs(self, request):
        column_defs = [
        {'name': 'nama', 'visible': True, },
        {'name': 'nik', 'visible': True, },
        {'name': 'Aksi', 'visible': True, 'searchable': False, 'orderable': False, 'title': 'Aksi' },
    ]
        return column_defs
    
    def customize_row(self, row, obj):
        row['Aksi'] = format_html(
            '<a href="/karyawan/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
            '<a href="/karyawan/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
            obj.pk
        )
        return row

    def render_column(self, row, column):
        if column == 'aksi':
            return format_html(
                '<a href="/karyawan/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
                '<a href="/karyawan/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
                row.pk
            )
        else:
            return super(KaryawanAjaxView, self).render_column(row, column)

class CriticalStokView(TemplateView):
    template_name = "sparepart/critical_stok.html"        

class CriticalStokAjaxView(AjaxDatatableView):
    model = SparePart
    initial_order = [["nama", "asc"], ]
    title = "Critical Stok"
    max_display_length = 50
    search_values_separator = " "
    length_menu = [[10, 25, 50, -1], [10, 25, 50, "All"]]

    def get_initial_queryset(self, request):
        # lte = less than or equal
        # gte = greater than or equal
        return SparePart.objects.filter(jumlah__lte=2)

    def get_column_defs(self, request):
        column_defs = [
        {'name': 'nama', 'visible': True, },
        {'name': 'merk', 'visible': True, 'foreign_field': 'merk__nama', },
        {'name': 'jumlah', 'visible': True, },
        {'name': 'status', 'visible': True, 'searchable': False, 'orderable': False, 'title': 'Status' },
        {'name': 'rak', 'visible': True, },
        ]
        return column_defs
    
    def customize_row(self, row, obj):        
        if obj.jumlah >= 2:
            row['status'] = format_html(
                '<span class="badge bg-success">Aman</span>'
            )
        elif obj.jumlah >= 1:
            row['status'] = format_html(
                '<span class="badge bg-warning">Hampir Habis</span>'
            )
        else:
            row['status'] = format_html(
                '<span class="badge bg-danger">Habis</span>'
            )
        return row
    
class BarangMasukView(TemplateView):
    template_name = "sparepart/barang_masuk.html"

class BarangMasukAjaxView(AjaxDatatableView):
    model = HistoryBarangMasuk
    initial_order = [["created_at", "desc"], ]
    title = "Barang Masuk"
    max_display_length = 50
    search_values_separator = " "
    length_menu = [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]]

    def get_column_defs(self, request):
        column_defs = [
        {'name': 'tanggal', 'visible': True, },
        {'name': 'sparepart', 'visible': True, 'foreign_field': 'sparepart__nama',},
        {'name': 'jumlah', 'visible': True,},
        {"name": "Total", "visible": True, "foreign_field": "sparepart__jumlah"},
        {'name': 'karyawan', 'visible': True, 'foreign_field': 'karyawan__nama',},
        {"name": "created_at", "visible": True, "title": "created_at"}
    ]
        return column_defs

    def customize_row(self, row, obj):
        row['created_at'] = obj.created_at.strftime("%H:%M:%S")

class BarangKeluarView(TemplateView):
    template_name = "sparepart/barang_keluar.html"

class BarangKeluarAjaxView(AjaxDatatableView):
    model = HistoryBarangKeluar
    initial_order = [["created_at", "desc"], ]
    title = "Barang Keluar"
    max_display_length = 50
    search_values_separator = " "
    length_menu = [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]]

    def get_column_defs(self, request):
        column_defs = [
        {'name': 'tanggal', 'visible': True, },
        {'name': 'sparepart', 'visible': True, 'foreign_field': 'sparepart__nama',},
        {'name': 'jumlah', 'visible': True,},
        {"name": "Total", "visible": True, "foreign_field": "sparepart__jumlah"},
        {'name': 'karyawan', 'visible': True, 'foreign_field': 'karyawan__nama',},
        {"name": "created_at", "visible": True, "title": "created_at"}
    ]
        return column_defs

    def customize_row(self, row, obj):
        row['created_at'] = obj.created_at.strftime("%H:%M:%S")

class SparePartCreateView(CreateView):
    template_name = "sparepart/sparepart_create.html"
    model = SparePart
    fields = "__all__"
    success_url = "/sparepart/"

class SparePartUpdateView(UpdateView):
    template_name = "sparepart/sparepart_update.html"
    model = SparePart
    fields = "__all__"
    success_url = "/sparepart/"

class SparePartDeleteView(DeleteView):
    template_name = "sparepart/sparepart_delete.html"
    model = SparePart
    success_url = "/sparepart/"

class MerkCreateView(CreateView):
    template_name = "sparepart/merk_create.html"
    model = Merk
    fields = "__all__"
    success_url = "/merk/"
    
class MerkUpdateView(UpdateView):
    template_name = "sparepart/merk_update.html"
    model = Merk
    fields = "__all__"
    success_url = "/merk/"

class MerkDeleteView(DeleteView):
    template_name = "sparepart/merk_delete.html"
    model = Merk
    success_url = "/merk/"

class KaryawanCreateView(CreateView):
    template_name = "sparepart/karyawan_create.html"
    model = Karyawan
    fields = "__all__"
    success_url = "/karyawan/"

class KaryawanUpdateView(UpdateView):
    template_name = "sparepart/karyawan_update.html"
    model = Karyawan
    fields = "__all__"
    success_url = "/karyawan/"

class KaryawanDeleteView(DeleteView):
    template_name = "sparepart/karyawan_delete.html"
    model = Karyawan
    success_url = "/karyawan/"

class BarangMasukCreateView(CreateView):
    template_name = "sparepart/barang_masuk_create.html"
    model = HistoryBarangMasuk
    success_url = "/barang_masuk/"
    form_class = BarangMasukForm

class BarangKeluarCreateView(CreateView):
    template_name = "sparepart/barang_keluar_create.html"
    model = HistoryBarangKeluar
    success_url = "/barang_keluar/"
    form_class = BarangKeluarForm
