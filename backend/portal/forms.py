from django import forms
from .models import Region, Comuna, SolicitudArriendo, PerfilUser, Inmueble


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nro_region', 'nombre']

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['region', 'nombre']

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre',
            'descripcion',
            'm2_construidos',
            'm2_totales',
            'estacionamientos',
            'habitaciones',
            'banos',
            'direccion',
            'precio_mensual',
            'comuna',
            'tipo_inmueble'
            ]
        

class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'mensaje']


class PerfilUserForm(forms.ModelForm):
    class Meta:
        model = PerfilUser
        fields = ['tipo_usuario', 'rut', 'password']