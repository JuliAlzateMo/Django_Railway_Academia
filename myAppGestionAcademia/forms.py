from django import forms
from .models import Estudiantes, Profesores, Asistencias, Calificaciones

class FormularioEditarEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellido', 'cedula', 'contacto', 'email', 'direccion', 'ciudad']

class FormularioEditarProfesor(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre', 'apellido', 'cedula', 'contacto', 'email', 'direccion', 'ciudad']

class FormularioAsistencias(forms.ModelForm):
    class Meta:
        model = Asistencias
        fields = ['fkCurso', 'fkEstudiante', 'fkProfesor', 'asistencia1', 'asistencia2', 'asistencia3', 'asistencia4']

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = ['calificacion1', 'calificacion2', 'calificacion3']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencias
        fields = ['asistencia1', 'asistencia2', 'asistencia3', 'asistencia4']