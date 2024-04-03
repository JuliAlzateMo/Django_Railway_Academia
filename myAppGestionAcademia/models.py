from django.db import models
from django.contrib.auth.models import User


class Estudiantes(models.Model):
    idEstudiante = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=12, blank= False, null=False)
    nombre = models.CharField(max_length=100, blank= False, null=False)
    apellido = models.CharField(max_length=100, blank= False, null=False)
    contacto = models.CharField(max_length=10, blank= False, null=False)
    email = models.EmailField(blank= False, null=False)
    direccion = models.CharField(max_length=100, blank= False, null=False, default=None)
    ciudad = models.CharField(max_length=100, blank= False, null=False, default=None)
    foto = models.ImageField(upload_to='estudiantes', default=None, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        db_table = "Estudiantes"

    def __str__(self):

        return f"Es: {self.cedula}  {self.nombre} {self.apellido}"
    
class Profesores(models.Model):
    idProfesor = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=12, blank= False, null=False)
    nombre = models.CharField(max_length=100, blank= False, null=False)
    apellido = models.CharField(max_length=100, blank= False, null=False)
    contacto = models.CharField(max_length=10, blank= False, null=False)
    email = models.EmailField(blank= False, null=False)
    direccion = models.CharField(max_length=100, blank= False, null=False, default=None)
    ciudad = models.CharField(max_length=100, blank= False, null=False, default=None)
    foto = models.ImageField(upload_to='profesores', default=None, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    especialidad1 = models.CharField(max_length=100, blank= False, null=False)
    especialidad2 = models.CharField(max_length=100, blank= True, null=True)
    especialidad3 = models.CharField(max_length=100, blank= True, null=True)
    

    class Meta:

        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        db_table = "Profesores"

    def __str__(self):

        return  f'Ing. {self.nombre} {self.apellido} '


class Cursos(models.Model):

    idCurso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField()
    fechaInicio = models.DateField(blank=False, null=False, default = "2024-01-01", verbose_name="Inicio")
    fechaFin = models.DateField(blank=False, null=False, default = "2024-01-01", verbose_name="Fin")
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(blank=False, null=False)
    precio = models.CharField(max_length=50, blank=False, null=False, default=0)
    clases = models.IntegerField(blank=False, null=False, default=0)
    foto = models.ImageField(upload_to='foto', default=None, null=False)
    version = models.IntegerField(blank=False, null=False, default=1)
    fkProfesor = models.ForeignKey(Profesores, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="Profesor")


    class Meta:

        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        db_table = "Cursos"

    def __str__(self):

        return f"{self.titulo} ({str(self.fechaInicio)}) ({str(self.fechaFin)})"
    
class Inscripciones(models.Model):

    idInscripcion = models.AutoField(primary_key=True)
    fkCurso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Curso")
    fkEstudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Estudiante")
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    class Meta:

        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"
        db_table = "Inscripciones"

    def __str__(self):

        return str(self.fkCurso) + " - " + str(self.fkEstudiante)
    
class Asistencias(models.Model):

    idAsistencia = models.AutoField(primary_key=True)
    fkCurso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Curso")
    fkEstudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Estudiante")
    fkProfesor = models.ForeignKey(Profesores, on_delete=models.CASCADE, null=True, blank=True, default = None, verbose_name="Profesor")
    asistencia1 = models.BooleanField(default=False, verbose_name="A#1")
    asistencia2 = models.BooleanField(default=False, verbose_name="A#2")
    asistencia3 = models.BooleanField(default=False, verbose_name="A#3")
    asistencia4 = models.BooleanField(default=False, verbose_name="A#4")
    porcentajeAsistencia = models.IntegerField(null=True, blank=True, verbose_name = "%")
    
    
    class Meta:

        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        db_table = "Asistencias"

    def __str__(self):

        return str(self.fkEstudiante) + " " + str(self.fkCurso)
    
    def calcularPorcentaje(self):

        if self.asistencia1 == False and self.asistencia2 == False and self.asistencia3 == False and self.asistencia4 == False:

            return 0

        elif self.asistencia1 == True and self.asistencia2 == True and self.asistencia3 == True and self.asistencia4 == True:

            return 100
        
        elif self.asistencia1 == True and self.asistencia2 == False and self.asistencia3 == False and self.asistencia4 == False:

            return 25
        
        elif self.asistencia1 == True and self.asistencia2 == True and self.asistencia3 == False and self.asistencia4 == False:

            return 50
        
        elif self.asistencia1 == False and self.asistencia2 == True and self.asistencia3 == False and self.asistencia4 == False:

            return 25
        
        elif self.asistencia1 == True and self.asistencia2 == True and self.asistencia3 == True and self.asistencia4 == False:

            return 75
        
        elif self.asistencia1 == False and self.asistencia2 == True and self.asistencia3 == True and self.asistencia4 == False:

            return 50
        
        elif self.asistencia1 == False and self.asistencia2 == False and self.asistencia3 == True and self.asistencia4 == False:

            return 25
        
        elif self.asistencia1 == True and self.asistencia2 == False and self.asistencia3 == True and self.asistencia4 == False:

            return 50
        
        elif self.asistencia1 == False and self.asistencia2 == True and self.asistencia3 == True and self.asistencia4 == True:

            return 75
        
        elif self.asistencia1 == False and self.asistencia2 == False and self.asistencia3 == True and self.asistencia4 == True:

            return 50
        
        elif self.asistencia1 == False and self.asistencia2 == False and self.asistencia3 == False and self.asistencia4 == True:

            return 25
        
        elif self.asistencia1 == True and self.asistencia2 == False and self.asistencia3 == True and self.asistencia4 == True:

            return 75
        
        elif self.asistencia1 == True and self.asistencia2 == True and self.asistencia3 == False and self.asistencia4 == True:

            return 75
        
        elif self.asistencia1 == True and self.asistencia2 == False and self.asistencia3 == False and self.asistencia4 == True:

            return 50
        
        elif self.asistencia1 == False and self.asistencia2 == True and self.asistencia3 == False and self.asistencia4 == True:

            return 50
        
        

    def save(self, *args, **kwargs):

        if self.asistencia1 or self.asistencia2 or self.asistencia3 or self.asistencia4:

            self.porcentajeAsistencia = self.calcularPorcentaje()

        super().save(*args, **kwargs)
    

class Calificaciones(models.Model):

    idCalificacion = models.AutoField(primary_key=True)
    fkCurso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Curso")
    fkEstudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Estudiante")
    fkProfesor = models.ForeignKey(Profesores, on_delete=models.CASCADE, null=True, blank=True, default = None, verbose_name="Profesor")
    calificacion1 = models.DecimalField(null=True, blank=True, verbose_name = 'Nota 1', max_digits=3, decimal_places=1)
    calificacion2 = models.DecimalField(null=True, blank=True, verbose_name = 'Nota 2', max_digits=3, decimal_places=1)
    calificacion3 = models.DecimalField(null=True, blank=True, verbose_name = 'Nota 3', max_digits=3, decimal_places=1)
    promedio = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    class Meta:

        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"
        db_table = "Calificaciones"

    def __str__(self):

        return str(self.fkEstudiante) + " " + str(self.fkCurso) + " " + str(self.promedio)
    
    def calcularPromedio(self):

        notas = [self.calificacion1, self.calificacion2, self.calificacion3]

        validarNotas = [nota for nota in notas if nota is not None]

        if validarNotas:

            return sum(validarNotas) / len(validarNotas)
        
        else:

            None
    
    def save(self, *args, **kwargs):

        if self.calificacion1 or self.calificacion2 or self.calificacion3:

            self.promedio = self.calcularPromedio()

        super().save(*args, **kwargs)