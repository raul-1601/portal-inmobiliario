from django.contrib import admin
from .models import Comuna, Region, Inmueble, SolicitudArriendo, PerfilUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    pass

@admin.register(SolicitudArriendo)
class SolicitudArriendoAdmin(admin.ModelAdmin):
    pass


## registrar el usuario, recordar importar from django.contrib.auth.admin import UserAdmin
@admin.register(PerfilUser)
class PerfilUserAdmin(UserAdmin):  ## hereda de User Admin 
    fieldsets = UserAdmin.fieldsets + (
        ("Información extra", {"fields": ("rut", "tipo_usuario")}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("rut", "tipo_usuario")}),
        )