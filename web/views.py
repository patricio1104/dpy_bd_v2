from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class FacultadViewSet (viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacultadSerializer

class EscuelaProfesionalViewSet (viewsets.ModelViewSet):
    queryset = EscuelaProfesional.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EscuelaProfesionalSerializer
    
class CursoViewSet (viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer

class PeriodoViewSet (viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeriodoSerializer

class SeccionViewSet (viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SeccionSerializer

class AlumnoViewSet (viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnoSerializer

class DocenteViewSet (viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DocenteSerializer

class MatriculaViewSet (viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MatriculaSerializer

class AsignacionViewSet (viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignacionSerializer

class LugarViewSet (viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LugarSerializer

class PisoViewSet (viewsets.ModelViewSet):
    queryset = Piso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PisoSerializer

class TipoLugarViewSet (viewsets.ModelViewSet):
    queryset = TipoLugar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoLugarSerializer

class ReservaAulaViewSet (viewsets.ModelViewSet):
    queryset = ReservaAula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReservaAulaSerializer

class ReservaLaboratorioViewSet (viewsets.ModelViewSet):
    queryset = ReservaLaboratorio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReservaLaboratorioSerializer

class ReservaEspacioViewSet (viewsets.ModelViewSet):
    queryset = ReservaEspacio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReservaEspacioSerializer

class SesionViewSet (viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SesionSerializer