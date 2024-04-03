from django.contrib import admin
from .models import Cursos, Estudiantes, Profesores, Inscripciones, Asistencias, Calificaciones

class AdminCursos(admin.ModelAdmin):

    list_display = ('titulo', 'fechaInicio', 'fechaFin', 'fkProfesor', 'version')
    search_fields = ('titulo', 'fechaCreacion', 'fechaInicio', 'fechaFin')
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ('fechaCreacion',)
    list_filter = ('titulo', 'fechaInicio', 'fechaFin', 'version')

admin.site.register(Cursos, AdminCursos)

class AdminEstudiantes(admin.ModelAdmin):
    search_fields = ('nombre', 'cedula', 'contacto', 'email', 'ciudad')
    readonly_fields = ('fechaCreacion',)

admin.site.register(Estudiantes, AdminEstudiantes)

class AdminProfesores(admin.ModelAdmin):
    search_fields = ('nombre', 'cedula', 'contacto', 'email', 'especialidad1', 'ciudad')
    list_filter = ('especialidad1', 'especialidad2', 'especialidad3')

admin.site.register(Profesores, AdminProfesores)

class AdminInscripciones(admin.ModelAdmin):

    search_fields = ('fkCurso', 'fkEstudiante', 'idInscripcion')
    list_filter = ('fkCurso', 'fkEstudiante', 'disponible')
    list_display = ('fkCurso', 'fkEstudiante', 'disponible')
    readonly_fields = ('fechaCreacion',)

admin.site.register(Inscripciones, AdminInscripciones)

class AdminAsistencias(admin.ModelAdmin):

    search_fields = ('fkEstudiante', 'idAsistencia', 'fkCurso')
    list_filter = ('fkEstudiante', 'fkCurso')
    list_display = ('fkCurso', 'fkProfesor', 'fkEstudiante', 'asistencia1', 'asistencia2', 'asistencia3', 'asistencia4', 'porcentajeAsistencia')

admin.site.register(Asistencias, AdminAsistencias)

class AdminCalificaciones(admin.ModelAdmin):

    search_fields = ('fkEstudiante', 'idCalificacion', 'fkCurso')
    list_filter = ('fkCurso', 'fkEstudiante')
    list_display = ('fkCurso', 'fkEstudiante', 'calificacion1', 'calificacion2', 'calificacion3', 'promedio')

admin.site.register(Calificaciones, AdminCalificaciones)


