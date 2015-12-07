from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^alumnos/lista/$', listAlumnos.as_view(), name='listAlumnos'),
    url(r'^buscar/$', buscar.as_view(), name='buscar'),
    url(r'^proyectoAlumnos/lista/$', buscarProyectoAlumnosView.as_view(), name='listProyectosAlumnos'),

    ]