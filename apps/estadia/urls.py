from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'estadia/inicio.html'}, name='inicio'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='salir'),

    url(r'^alumnos/$', Alumnos.as_view(), name='alumnos'),
    url(r'^alumnos/lista$', listAlumnos.as_view(), name='listAlumnos'),
    url(r'^alumnos/editar/(?P<pk>\d+)$', EditAlumnos.as_view(), name='editAlumnos'),
    url(r'^alumnos/eliminar/(?P<pk>\d+)$', ElimAlumnos.as_view(), name='elimAlumnos'),

    url(r'^asesor/$', Asesores.as_view(), name='asesores'),
    url(r'^asesor/lista$', listAsesores.as_view(), name='listAsesores'),
    url(r'^asesor/editar/(?P<pk>\d+)$', EditAsesores.as_view(), name='editAsesores'),
    url(r'^asesor/eliminar/(?P<pk>\d+)$', ElimAsesores.as_view(), name='elimAsesores'),

    url(r'^categoria/$', Categoria.as_view(), name='categorias'),
    url(r'^categoria/lista$', listCategoria.as_view(), name='listCategorias'),
    url(r'^categoria/editar/(?P<pk>\d+)$', EditCategoria.as_view(), name='editCategorias'),
    url(r'^categoria/eliminar/(?P<pk>\d+)$', ElimCategoria.as_view(), name='elimCategorias'),

    url(r'^ciclos/$', Ciclos.as_view(), name='ciclos'),
    url(r'^ciclos/lista$', listCiclos.as_view(), name='listCiclos'),
    url(r'^ciclos/editar/(?P<pk>\d+)$', EditCiclos.as_view(), name='editCiclos'),
    url(r'^ciclos/eliminar/(?P<pk>\d+)$', ElimCiclos.as_view(), name='elimCiclos'),

    url(r'^proyectos/$', Proyectos.as_view(), name='proyectos'),
    url(r'^proyectos/lista$', listProyectos.as_view(), name='listProyectos'),
    url(r'^proyectos/editar/(?P<pk>\d+)$', EditProyectos.as_view(), name='editProyectos'),
    url(r'^proyectos/eliminar/(?P<pk>\d+)$', ElimProyectos.as_view(), name='elimProyectos'),

]
