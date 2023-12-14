from django import forms
from sparepart.models import SparePart, HistoryBarangMasuk
from crispy_forms.helper import FormHelper
from crispy_forms import layout
from crispy_forms.layout import Layout

class BarangMasukForm(forms.ModelForm):
    jumlah = forms.IntegerField()
    class Meta:
        model = HistoryBarangMasuk
        fields = ('tanggal', 'sparepart', 'karyawan', 'jumlah')
        widgets = {
            'tanggal': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # 'placeholder': 'Masukkan nama sparepart
            'sparepart': forms.Select(attrs={'class': 'form-control'}),
            'karyawan': forms.Select(attrs={'class': 'form-control'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}), # 'placeholder': 'Masukkan jumlah sparepart
        }
    # add inline form using formhelper
    def __init__(self, *args, **kwargs):
        super(BarangMasukForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            layout.Row(
                layout.Column('tanggal', css_class='form-group col-md-3 mb-0'),
                layout.Column('sparepart', css_class='form-group col-md-3 mb-0'),
                layout.Column('karyawan', css_class='form-group col-md-3 mb-0'),
                layout.Column('jumlah', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
        )
           
    def save(self, commit=True):
        instance = super().save(commit=False)
        sparepart = SparePart.objects.get(pk=self.cleaned_data['sparepart'].pk)
        sparepart.jumlah += self.cleaned_data['jumlah']
        sparepart.save()
        instance.save()
        return instance