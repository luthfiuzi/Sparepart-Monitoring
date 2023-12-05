from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from sparepart.models import Merk, SparePart
from ajax_datatable.views import AjaxDatatableView
from django.utils.html import format_html

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
        {'name': 'Aksi', 'visible': True, 'searchable': False, 'orderable': False, 'title': 'Aksi' },
    ]
        return column_defs
    
    def customize_row(self, row, obj):
        row['Aksi'] = format_html(
            '<a href="/sparepart/update/{0}" class="btn btn-primary btn-sm">Update</a>&nbsp;'
            '<a href="/sparepart/delete/{0}" class="btn btn-danger btn-sm">Delete</a>',
            obj.pk
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


class UserView(TemplateView):
    template_name = "sparepart/user.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["nama"] = "Luthfi"
        context["umur"] = 18
        return context
    
class MerkView(TemplateView):
    template_name = "sparepart/merk.html"

class inputView(TemplateView):
    template_name = "sparepart/input.html"

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
    
class MerkCreateView(CreateView):
    template_name = "sparepart/merk_create.html"
    model = Merk
    fields = "__all__"
    success_url = "/merk/"

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
    
class MerkUpdateView(UpdateView):
    template_name = "sparepart/merk_update.html"
    model = Merk
    fields = "__all__"
    success_url = "/merk/"

class MerkDeleteView(DeleteView):
    template_name = "sparepart/merk_delete.html"
    model = Merk
    success_url = "/merk/"

# Create your views here.
