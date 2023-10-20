from rest_framework import serializers
from .models import *

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class EscuelaProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscuelaProfesional
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'

class PisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piso
        fields = '__all__'

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class TipoLugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLugar
        fields = '__all__'

class ReservaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAula
        fields = '__all__'

class ReservaLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaLaboratorio
        fields = '__all__'

class ReservaEspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaEspacio
        fields = '__all__'

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = '__all__'