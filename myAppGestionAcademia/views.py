from django.shortcuts import render, redirect, get_object_or_404
from .models import Cursos, Estudiantes, Profesores, User, Inscripciones, Asistencias, Calificaciones
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import FormularioEditarEstudiante, FormularioEditarProfesor, CalificacionForm, AsistenciaForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse
from django.db.models import Q

def home(request):

    profesor = Profesores.objects.all()

    estudiante = Estudiantes.objects.all()

    modulos = {'user': request.user, 'estudiante': estudiante, 'profesor': profesor}

    return render(request, 'home.html', modulos)

def cursos(request):

    estudiante = Estudiantes.objects.all()

    profesor = Profesores.objects.all()

    cursos = Cursos.objects.all()

    modulos = {'cursos': cursos, 'estudiante': estudiante, 'profesor': profesor }

    return render(request, 'cursos.html', modulos)

def contactar(request):

    if request.method == 'POST':

        asunto = request.POST['txtAsunto']

        mensaje = request.POST['txtMensaje'] + "\nNombre: " + request.POST['txtNombre'] + "\nContacto: " + request.POST['txtContacto'] + "\nEmail: " + request.POST['txtEmail'] + "\nCurso: " + request.POST['txtCurso']

        email_desde = settings.EMAIL_HOST_USER

        email_para = ["juliannal999@hotmail.com"]

        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)

        return render(request, 'contactoExitoso.html')
    
    return render(request, 'detalleCurso.html')

def formulario(request):

    return render (request, 'formulario.html')

def salir (request):

    logout (request)

    return redirect ('/')

def iniciar (request):
    
    if request.method=='POST':
        
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contra)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('/')
                
            else:
                pass
            
        else:
            
            pass
                

    form=AuthenticationForm()
    
    return render (request, 'registration/login.html', {'form':form})

def perfilEstudiante(request, idEstudiante):

    estudiante = Estudiantes.objects.get(idEstudiante=idEstudiante)

    modulos = {'estudiante': estudiante}

    return render(request, 'perfilEstudiante/perfilEstudiante.html', modulos)

def editarEstudiante (request, idEstudiante):

    estudiante = Estudiantes.objects.get(idEstudiante=idEstudiante)

    if request.method == 'POST':

        form = FormularioEditarEstudiante(request.POST, request.FILES)

        if form.is_valid():

            nom = form.cleaned_data.get('nombre')
            ape = form.cleaned_data.get('apellido')
            ced = form.cleaned_data.get('cedula')
            con = form.cleaned_data.get('contacto')
            em = form.cleaned_data.get('email')
            dir = form.cleaned_data.get('direccion')
            ciu = form.cleaned_data.get('ciudad')
            

            Estudiantes.objects.update(
                nombre = nom,
                apellido = ape,
                cedula = ced,
                contacto = con,
                email = em,
                direccion = dir,
                ciudad = ciu,
            )

            form = FormularioEditarEstudiante()
            
            return redirect('/')

    else:

        form = FormularioEditarEstudiante()
        

    modulos = {'form': form, 'estudiante': estudiante}
    
    return render(request, 'perfilEstudiante/editarEstudiante.html', modulos)

def cursosEstudiante (request, idEstudiante):

    estudiante = Estudiantes.objects.get(idEstudiante=idEstudiante)

    inscripciones = Inscripciones.objects.filter(fkEstudiante=idEstudiante)

    cursos = Cursos.objects.all()

    modulos = {'estudiante': estudiante, 'inscripciones': inscripciones, 'cursos': cursos}

    return render(request, 'perfilEstudiante/cursosEstudiante.html', modulos)

def progresoEstudiante (request, idEstudiante, idCurso):

    estudiante = Estudiantes.objects.get(idEstudiante=idEstudiante)

    asistencias = Asistencias.objects.filter(fkEstudiante=idEstudiante, fkCurso=idCurso)

    calificaciones = Calificaciones.objects.filter(fkEstudiante=idEstudiante, fkCurso=idCurso)

    modulos = {'estudiante': estudiante, 'asistencias': asistencias, 'calificaciones': calificaciones}

    return render(request, 'perfilEstudiante/progresoEstudiante.html', modulos)

def perfilProfesor(request, idProfesor):

    profesor = Profesores.objects.get(idProfesor=idProfesor)

    cursos = Cursos.objects.all()

    modulos = {'profesor': profesor, 'cursos': cursos}

    return render(request, 'perfilProfesor/perfilProfesor.html', modulos)

def editarProfesor (request, idProfesor):

    profesor = Profesores.objects.get(idProfesor=idProfesor)

    if request.method == 'POST':

        form = FormularioEditarProfesor(request.POST, request.FILES)

        if form.is_valid():

            nom = form.cleaned_data.get('nombre')
            ape = form.cleaned_data.get('apellido')
            ced = form.cleaned_data.get('cedula')
            con = form.cleaned_data.get('contacto')
            em = form.cleaned_data.get('email')
            dir = form.cleaned_data.get('direccion')
            ciu = form.cleaned_data.get('ciudad')
            

            Profesores.objects.update(
                nombre = nom,
                apellido = ape,
                cedula = ced,
                contacto = con,
                email = em,
                direccion = dir,
                ciudad = ciu,
            )

            form = FormularioEditarProfesor()
            
            return redirect('/')

    else:

        form = FormularioEditarProfesor()
        

    modulos = {'form': form, 'profesor': profesor}
    
    return render(request, 'perfilProfesor/editarProfesor.html', modulos)

def cursosProfesor (request, idProfesor):

    profesor = Profesores.objects.get(idProfesor=idProfesor)

    cursos = Cursos.objects.filter(fkProfesor=idProfesor)

    modulos = {'profesor': profesor, 'cursos': cursos}

    return render(request, 'perfilProfesor/cursosProfesor.html', modulos)

def progresoProfesor(request, idProfesor, idCurso):

    profesor = Profesores.objects.get(idProfesor=idProfesor)

    curso = Cursos.objects.get(idCurso=idCurso)
    
    inscripciones = Inscripciones.objects.filter(fkCurso=idCurso)

    estudiantes = Estudiantes.objects.all()

    modulos = {'profesor': profesor, 'curso': curso, 'inscripciones': inscripciones, 'estudiantes': estudiantes}
    
    return render(request, 'perfilProfesor/progresoProfesor.html', modulos)

def detalleEstudianteAs(request, idProfesor, idCurso, idEstudiante):

    profesor = Profesores.objects.get(idProfesor=idProfesor)

    curso = Cursos.objects.get(idCurso=idCurso)

    estudiante = Estudiantes.objects.get(idEstudiante=idEstudiante)

    asistencia, _ = Asistencias.objects.get_or_create(fkProfesor=profesor, fkCurso=curso, fkEstudiante=estudiante)


    if request.method == 'POST':

        asistencia_form = AsistenciaForm(request.POST, instance=asistencia)

        if asistencia_form.is_valid():
            asistencia_form.save()

    else:

        asistencia_form = AsistenciaForm(instance=asistencia)

    asistencias = Asistencias.objects.filter(fkEstudiante=estudiante)

    modulos = {
        'profesor': profesor,
        'curso': curso,
        'estudiante': estudiante,
        'asistencias': asistencias,
        'asistencia_form': asistencia_form,
    }
    
    return render(request, 'perfilProfesor/detalleEstudianteAs.html', modulos)

def detalleEstudianteCa(request, idProfesor, idCurso, idEstudiante):

    profesor = Profesores.objects.get(idProfesor=idProfesor)

    curso = Cursos.objects.get(idCurso=idCurso)

    estudiante = Estudiantes.objects.get(idEstudiante=idEstudiante)

    calificacion, _ = Calificaciones.objects.get_or_create(fkCurso=curso, fkEstudiante=estudiante)

    if request.method == 'POST':
        
        calificacion_form = CalificacionForm(request.POST, instance=calificacion)
        
        if calificacion_form.is_valid():
            calificacion_form.save()
      
    else:

        calificacion_form = CalificacionForm(instance=calificacion)


    calificaciones = Calificaciones.objects.filter(fkEstudiante=estudiante)
    

    modulos = {
        'profesor': profesor,
        'curso': curso,
        'estudiante': estudiante,
        'calificaciones': calificaciones,
        'calificacion_form': calificacion_form,
    }
    
    return render(request, 'perfilProfesor/detalleEstudianteCa.html', modulos)

def recuperarContraseña(request):

    if request.method == "POST":

        form = PasswordResetForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            # Generar token para el usuario
            user = User.objects.filter(email=email).first()

            if user:

                token = default_token_generator.make_token(user)

                uid = urlsafe_base64_encode(force_bytes(user.pk))

                # Crear el enlace para restablecer la contraseña
                reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))
                # Renderizar el cuerpo del correo electrónico
                email_body = render_to_string('emailRecuperarContraseña.html', {'reset_link': reset_link})
                # Enviar el correo electrónico
                send_mail(
                    'Restablecer contraseña',
                    email_body,
                    'tu_correo@gmail.com',  # Remitente del correo electrónico
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Se ha enviado un correo electrónico con instrucciones para restablecer tu contraseña.')

                return redirect('/')
            
            else:

                messages.error(request, 'No se encontró ninguna cuenta asociada a esta dirección de correo electrónico.')
    else:

        form = PasswordResetForm()

    return render(request, "recuperarContraseña.html", {"form": form})










