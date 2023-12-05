from sparepart import views
from django.urls import path

app_name = "sparepart"

urlpatterns = [
    path("sparepart/", views.SparePartView.as_view(), name="home"),
    path("sparepart/ajax/", views.SparePartAjaxView.as_view(), name="sparepart_ajax"),
    path("user/", views.UserView.as_view(), name="user"),
    path("merk/", views.MerkView.as_view(), name="merk"),
    path("merk/ajax/", views.MerkAjaxView.as_view(), name="merk_ajax"),
    path("merk/create/", views.MerkCreateView.as_view(), name="merk_create"),
    path("sparepart/create/", views.SparePartCreateView.as_view(), name="sparepart_create"),
    path("merk/update/<int:pk>/", views.MerkUpdateView.as_view(), name="merk_update"),
    path("merk/delete/<int:pk>/", views.MerkDeleteView.as_view(), name="merk_delete"),
    path("sparepart/update/<int:pk>/", views.SparePartUpdateView.as_view(), name="sparepart_update"),
    path("sparepart/delete/<int:pk>/", views.SparePartDeleteView.as_view(), name="sparepart_delete"),
    path("input/", views.inputView.as_view(), name="input"),
]