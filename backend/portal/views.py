from django.shortcuts import render
from .models import Region, Comuna, SolicitudArriendo, PerfilUser, Inmueble
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import RegionForm, ComunaForm, InmuebleForm, SolicitudArriendoForm, PerfilUserForm
from django.urls import reverse_lazy


### CRUD PARA REGIONES ###

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'inmueble/region_form.html'
    success_url = reverse_lazy('region_list')


class RegionListView(ListView):
    model = Region
    template_name = 'inmueble/region_list.html'
    context_object_name = 'regiones'


class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'inmueble/region_form.html'
    success_url = reverse_lazy('region_list')


class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'inmueble/region_confirm_delete.html'
    success_url = reverse_lazy('region_list')


###########################################################################

### CRUD COMUNAS ###

class ComunaCreateView(CreateView):
    model = Comuna
    form_class = ComunaForm
    template_name = 'inmueble/comuna_form.html'
    success_url = reverse_lazy('comuna_list')


class ComunaListView(ListView):
    model = Comuna
    template_name = 'inmueble/comuna_list.html'
    context_object_name = 'comunas'

class ComunaUpdateView(UpdateView):
    model = Comuna
    form_class = ComunaForm
    template_name = 'inmueble/comuna_form.html'
    success_url = reverse_lazy('comuna_list')

class ComunaDeleteView(DeleteView):
    model = Comuna
    template_name = 'inmueble/comuna_confirm_delete.html'
    success_url = reverse_lazy('comuna_list')


###########################################################################

### CRUD INMUEBLE ###

class InmuebleCreateView(CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'inmueble/inmueble_form.html'
    success_url = reverse_lazy('inmueble_list')


class InmuebleListView(ListView):
    model = Inmueble
    template_name = 'inmueble/inmueble_list.html'
    context_object_name = 'inmuebles'

class InmuebleUpdateView(UpdateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'inmueble/inmueble_form.html'
    success_url = reverse_lazy('inmueble_list')


class InmuebleDeleteView(DeleteView):
    model = Inmueble
    template_name = 'inmueble/inmueble_confirm_delete.html'
    success_url = reverse_lazy('inmueble_list')

###########################################################################

### CRUD SOLICITUD ARRIENDO ###

class SolicitudArriendoCreateView(CreateView):
    model = SolicitudArriendo
    form_class = SolicitudArriendoForm
    template_name = 'inmueble/solicitud_form.html'
    success_url = reverse_lazy('solicitud_list')


class SolicitudArriendoListView(ListView):
    model = SolicitudArriendo
    template_name = 'inmueble/solicitud_list.html'
    context_object_name = 'solicitudes'

class SolicitudArriendoUpdateView(UpdateView):
    model = SolicitudArriendo
    form_class = SolicitudArriendoForm
    template_name = 'inmueble/solicitud_form.html'
    success_url = reverse_lazy('solicitud_list')


class SolicitudArriendoDeleteView(DeleteView):
    model = SolicitudArriendo
    template_name = 'inmueble/solicitud_confirm_delete.html'
    success_url = reverse_lazy('solicitud_list')


###########################################################################

### CRUD PERFIL_USER ###

class PerfilUserCreateView(CreateView):
    model = PerfilUser
    form_class = PerfilUserForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('region_list')

class PerfilUserUpdateView(UpdateView):
    model = PerfilUser
    form_class = PerfilUserForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('region_list')

