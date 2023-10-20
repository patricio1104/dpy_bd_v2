from django.contrib import admin
from .models import *

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'decano')
    list_display_links = ('nombre', )
    search_fields = ('nombre', 'decano')

@admin.register(EscuelaProfesional)
class EscuelaProfesionalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'director', 'id_facultad')
    list_display_links = ('nombre', )
    search_fields = ('nombre', 'director')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'plan', 'id_escuela')
    list_display_links = ('nombre', )
    search_fields = ('nombre', 'codigo')

#admin.site.register(Aula)
#admin.site.register(Clase)
@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('anio', 'denominacion')
    list_display_links = ('anio', )
    search_fields = ('anio', 'denominacion')

@admin.register(TipoLugar)
class TipoLugarAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_lugar', 'nombre', 'piso', 'fecha_creacion', 'url_imagen')
    list_display_links = ('nombre', )
    search_fields = ('nombre', 'piso')

@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ('semana', 'fecha', 'id_seccion', 'tipo_clase', 'hora_inicio', 'hora_fin')
    list_display_links = ('tipo_clase', )
    search_fields = ('tipo_clase', 'semana', 'fecha')

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horario')
    list_display_links = ('nombre', )
    search_fields = ('nombre', 'horario')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombres', 'apellidos', 'correo')
    list_display_links = ('codigo', )
    search_fields = ('nombre', 'codigo', 'apellidos')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombres', 'apellidos', 'correo')
    list_display_links = ('codigo', )
    search_fields = ('nombre', 'codigo', 'apellidos')

admin.site.register(Matricula) # AlumnoSeccion
admin.site.register(Asignacion) # DocenteSeccion
admin.site.register(ReservaLaboratorio)
admin.site.register(ReservaEspacio)
admin.site.register(ReservaAula)
admin.site.register(Piso)
