from django.db import models

# Create your models here.

class Facultad(models.Model):
    nombre = models.CharField(max_length=256, verbose_name="Nombre")
    decano = models.CharField(max_length=256, verbose_name="Datos del decano")
    codigo = models.CharField(max_length=50, verbose_name="Codigo")

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)

class EscuelaProfesional(models.Model):
    id_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256, verbose_name="Nombre")
    director = models.CharField(max_length=256, verbose_name="Datos del director")
    codigo = models.CharField(max_length = 50 ,verbose_name="Codigo")

    class Meta:
        verbose_name = "Escuela Profesional"
        verbose_name_plural = "Escuelas profesionales"

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.nombre, self.codigo)

class Curso(models.Model):
    id_escuela = models.ForeignKey(EscuelaProfesional ,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256, verbose_name="Nombre")
    codigo = models.CharField(max_length=50, blank=False ,verbose_name="Codigo")
    plan = models.CharField(max_length=10, verbose_name="Plan")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)


class Periodo(models.Model):
    anio = models.PositiveIntegerField(verbose_name="Año")
    denominacion = models.CharField(max_length=10, verbose_name="Denominacion")

    class Meta:
        verbose_name_plural = "Periodos"

class Seccion(models.Model):
    id_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    horario = models.CharField(max_length=100, verbose_name="Horario")

    class Meta:
        verbose_name = "Curso Sección"
        verbose_name_plural = "Cursos Sección"

class Docente(models.Model):
    nombres = models.CharField(max_length=256, verbose_name="Nombres")
    apellidos = models.CharField(max_length=256, verbose_name="Apellidos")
    codigo = models.CharField(max_length=8, blank=True, verbose_name="Codigo")
    correo = models.CharField(max_length=100,blank=True, verbose_name="Correo")
    tipo_documento = models.CharField(max_length=10, blank=True, verbose_name="Tipo de documento")
    tipo_documento = models.CharField(max_length=10, verbose_name="Tipo de documento")
    numero_documento = models.CharField(max_length=10,  blank=True,verbose_name="Numero de documento")

    class Meta:
        verbose_name_plural = "Docentes"

    def __str__(self):
        texto = "{0} - {1} ({2})"
        return texto.format(self.nombres, self.apellidos, self.codigo)

class Alumno(models.Model):
    nombres = models.CharField(max_length=256, verbose_name="Nombres")
    apellidos = models.CharField(max_length=256, verbose_name="Apellidos")
    codigo = models.CharField(max_length=8, verbose_name="Codigo")
    correo = models.CharField(max_length=100, blank=True, verbose_name="Correo")
    tipo_documento = models.CharField(max_length=10,verbose_name="Tipo de documento")
    numero_documento = models.CharField(max_length=10, verbose_name="Numero de documento")

    class Meta:
        verbose_name_plural = "Alumnos"

    def __str__(self):
        texto = "{0} - {1} ({2})"
        return texto.format(self.nombres, self.apellidos, self.codigo)


class Matricula(models.Model): # AlumnoSeccion
    id_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

    def __str__(self):
        texto = "{0} - {1}, {2}"
        return texto.format(self.id_seccion.nombre, self.id_alumno.nombres, self.id_alumno.apellidos)


class Asignacion(models.Model): # DocenteSeccion
    id_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asignación"
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        texto = "{0} - {1}, {2}"
        return texto.format(self.id_seccion.nombre, self.id_docente.nombres, self.id_docente.apellidos)

# Piso, tipo de lugar, lugar, reservas

class Piso(models.Model):
    name = models.CharField(max_length = 200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Piso"
        verbose_name_plural = "Pisos"

class TipoLugar(models.Model):
    name = models.CharField(max_length = 200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de lugar"
        verbose_name_plural = "Tipos de lugares"

class Lugar(models.Model):
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE) # Piso 1, piso 2, piso 3
    id_tipo_lugar = models.ForeignKey(TipoLugar, on_delete=models.CASCADE) # Aula, laboratorio, baño, etc...
    nombre = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    
    url_imagen = models.URLField(blank=True, null=True)
    url_imagen_360 = models.URLField(blank=True, null=True)

    coordinates = models.JSONField(blank=True, null=True)
    marker_url = models.URLField(blank=True, null=True)
    fill_color = models.CharField(max_length=200, blank=True, null=True)
    border_color = models.CharField(max_length=200, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre, self.piso, self.id_tipo_lugar)

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

class ReservaLaboratorio(models.Model):
    id_lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE) # Lugar que es reservado por el alumno
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE) # Alumno que reserva
    fecha_generacion = models.DateTimeField(auto_now_add=True) # Fecha y hora
    fecha_solicitada_inicio = models.DateTimeField(auto_now_add=True) # Fecha y hora
    fecha_solicitada_fin = models.DateTimeField(auto_now_add=True) # Fecha y hora
    asunto = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.id_lugar.nombre, self.id_alumno.codigo)

    class Meta:
        verbose_name = "Reserva de laboratorios"
        verbose_name_plural = "Reservas de laboratorios"

class ReservaEspacio(models.Model):
    id_lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE) # Lugar que es reservado por el alumno
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE) # Alumno que reserva
    fecha_generacion = models.DateTimeField(auto_now_add=True) # Fecha y hora
    fecha_solicitada_inicio = models.DateTimeField(auto_now_add=True) # Fecha y hora
    fecha_solicitada_fin = models.DateTimeField(auto_now_add=True) # Fecha y hora
    asunto = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.id_lugar.nombre, self.id_alumno.codigo)
    
    class Meta:
        verbose_name = "Reserva de espacios"
        verbose_name_plural = "Reservas de espacios"

class Sesion(models.Model): # Clase pero sin asignacion de aulas, las aulas se asignan a través de la ReservaAula
    id_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    tipo_clase = models.CharField(max_length=10, verbose_name="Tipo de clase")
    semana = models.PositiveIntegerField(verbose_name="Semana")
    fecha = models.DateField(verbose_name="Fecha")
    hora_inicio = models.DateTimeField(verbose_name="Hora de inicio")
    hora_fin = models.DateTimeField(verbose_name="Hora de fin")

    class Meta:
        verbose_name = "Sesión"
        verbose_name_plural = "Sesiones"

    def __str__(self):
        texto = "{0} - {1} ({2})"
        return texto.format(self.tipo_clase, self.id_seccion, self.semana)

class ReservaAula(models.Model): # Para sesiones de clases
    id_lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    id_sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    fecha_generacion = models.DateTimeField(auto_now_add=True) # Fecha y hora
    fecha_solicitada_inicio = models.DateTimeField(auto_now_add=True) # Fecha y hora
    fecha_solicitada_fin = models.DateTimeField(auto_now_add=True) # Fecha y hora
    asunto = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.id_lugar.nombre, self.id_sesion.semana)
    
    class Meta:
        verbose_name = "Reserva de aula"
        verbose_name_plural = "Reserva de aulas"



