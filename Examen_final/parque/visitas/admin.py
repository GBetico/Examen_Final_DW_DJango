from django.contrib import admin

# Register your models here.
from visitas.models import origen 
from visitas.models import sexo
from visitas.models import RegistrarVisita 
from visitas.models import actividade 
from visitas.models import RegistrarActividade

class visitaAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Apellido", "Edad", "Sexo", "Origen", "Pais", "Documento", "Fecha", "Tarifa")
    list_filter=("Edad", "Sexo", "Origen", "Fecha",)
    date_hierarchy="Fecha"

class registroactividadAdmin(admin.ModelAdmin):
    list_display=("visitante", "actividad")
    list_filter=("actividad",)

admin.site.register(origen)
admin.site.register(sexo)
admin.site.register(RegistrarVisita, visitaAdmin)
admin.site.register(actividade)
admin.site.register(RegistrarActividade, registroactividadAdmin)