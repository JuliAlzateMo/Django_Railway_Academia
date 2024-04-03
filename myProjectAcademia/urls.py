"""
URL configuration for myProjectAcademia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myAppGestionAcademia.views import cursos, contactar, formulario, salir, iniciar, home, perfilEstudiante, perfilProfesor, editarEstudiante, editarProfesor, recuperarContraseña, cursosEstudiante, cursosProfesor, progresoEstudiante, progresoProfesor, detalleEstudianteAs,detalleEstudianteCa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfilEstudiante/<int:idEstudiante>/', perfilEstudiante, name='perfilEstudiante'),
    path('perfilProfesor/<int:idProfesor>/', perfilProfesor, name='perfilProfesor'),
    path('', home, name='home'),
    path('contactar/', contactar, name='contactar'),
    path('formulario/', formulario, name='formulario'),
    path('logout/', salir, name='salir'),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('login/', iniciar, name='login'),
    path('cursos/', cursos, name='cursos'),
    path('editarPerfilEstudiante/<int:idEstudiante>/', editarEstudiante, name='editarPerfilEstudiante'),
    path('editarPerfilProfesor/<int:idProfesor>/', editarProfesor, name='editarPerfilProfesor'),
    path('login/recuperarContraseña/', recuperarContraseña, name='recuperarContraseña'),
    path('cursosEstudiante/<int:idEstudiante>/', cursosEstudiante, name='cursosEstudiante'),
    path('cursosProfesor/<int:idProfesor>/', cursosProfesor, name='cursosProfesor'),
    path('progresoEstudiante/<int:idEstudiante>/<int:idCurso>/', progresoEstudiante, name='progresoEstudiante'),
    path('progresoProfesor/<int:idProfesor>/<int:idCurso>/', progresoProfesor, name='progresoProfesor'),
    path('detalleEstudianteAs/<int:idProfesor>/<int:idCurso>/<int:idEstudiante>/', detalleEstudianteAs, name='detalleEstudianteAs'),
    path('detalleEstudianteCa/<int:idProfesor>/<int:idCurso>/<int:idEstudiante>/', detalleEstudianteCa, name='detalleEstudianteCa'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

