from django import forms
from .models import Vehiculo

class FormularioVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('vin','patente', 'año_Fabricación', 'fecha_Recepción', 'marca', 'modelo', )