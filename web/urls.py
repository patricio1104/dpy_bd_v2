from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
#Lugares
router.register(r'Facultad', FacultadViewSet)
router.register(r'EscuelaProfesional', EscuelaProfesionalViewSet)
router.register(r'Piso', PisoViewSet)
router.register(r'Lugar', LugarViewSet)
router.register(r'TipoLugar', TipoLugarViewSet)

#Matricula
router.register(r'Curso', CursoViewSet)
router.register(r'Seccion', SeccionViewSet)
router.register(r'Periodo', PeriodoViewSet)
router.register(r'Sesion', SesionViewSet)
router.register(r'Alumno', AlumnoViewSet)
router.register(r'Docente', DocenteViewSet)
router.register(r'Matricula', MatriculaViewSet)
router.register(r'Asignacion', AsignacionViewSet)

#Registros
router.register(r'ReservaAula', ReservaAulaViewSet)
router.register(r'ReservaEspacio', ReservaEspacioViewSet)
router.register(r'ReservaLaboratorio', ReservaLaboratorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]