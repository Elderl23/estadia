from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Inicio (TemplateView):
	template_name='inicio/inicio.html'

###Alumnos###############################################################################

class Alumnos(CreateView):
	template_name = 'estadia/detalles.html'
	model = alumno
	fields = ['nombre', 'apellidos','tipo']
	success_url = reverse_lazy('u-app:listAlumnos')

class listAlumnos(ListView):
	template_name = 'estadia/alumnos.html'
	model = alumno

class EditAlumnos(UpdateView):
	template_name = 'estadia/detalles.html'
	model = alumno
	fields = ['nombre', 'apellidos','tipo']
	success_url = reverse_lazy('u-app:listAlumnos')

class ElimAlumnos(DeleteView):
	template_name='estadia/eliminar.html'
	model = alumno
	success_url = reverse_lazy('u-app:listAlumnos')

###Asesores###############################################################################

class Asesores(CreateView):
	template_name = 'estadia/detalles.html'
	model = asesor
	fields = ['nombre','apellidos','correo', 'tipo']
	success_url = reverse_lazy('u-app:listAsesores')

class listAsesores(ListView):
	template_name = 'estadia/asesores.html'
	model = asesor

class EditAsesores(UpdateView):
	template_name = 'estadia/detalles.html'
	model = asesor
	fields = ['nombre','apellidos','correo', 'tipo']
	success_url = reverse_lazy('u-app:listAsesores')

class ElimAsesores(DeleteView):
	template_name='estadia/eliminar.html'
	model = asesor
	success_url = reverse_lazy('u-app:listAsesores')

###Categorias###############################################################################

class Categoria(CreateView):
	template_name = 'estadia/detalles.html'
	model = categoria
	fields = ['tipo', 'descripcion']
	success_url = reverse_lazy('u-app:listCategorias')

class listCategoria(ListView):
	template_name = 'estadia/categoria.html'
	model = categoria

class EditCategoria(UpdateView):
	template_name = 'estadia/detalles.html'
	model = categoria
	fields = ['tipo','descripcion']
	success_url = reverse_lazy('u-app:listCategorias')

class ElimCategoria(DeleteView):
	template_name='estadia/eliminar.html'
	model = categoria
	success_url = reverse_lazy('u-app:listCategorias')

###Ciclo Escolar###############################################################################

class Ciclos(CreateView):
	template_name = 'estadia/detalles.html'
	model = ciclos
	fields = ['generacion','mes_ini','ano_ini','mes_fin','ano_fin']
	success_url = reverse_lazy('u-app:listCiclos')

class listCiclos(ListView):
	template_name = 'estadia/ciclos.html'
	model = ciclos

class EditCiclos(UpdateView):
	template_name = 'estadia/detalles.html'
	model = ciclos
	fields =['generacion','mes_ini','ano_ini','mes_fin','ano_fin']
	success_url = reverse_lazy('u-app:listCiclos')

class ElimCiclos(DeleteView):
	template_name='estadia/eliminar.html'
	model = ciclos
	success_url = reverse_lazy('u-app:listCiclos')


###Proyectos###############################################################################

class Proyectos(CreateView):
	template_name = 'estadia/detalles.html'
	model = proyecto
	fields = ['tipo', 'descripcion']
	success_url = reverse_lazy('u-app:listProyectos')

class listProyectos(ListView):
	template_name = 'estadia/proyectos.html'
	model = proyecto

class EditProyectos(UpdateView):
	template_name = 'estadia/detalles.html'
	model = proyecto
	fields = ['tipo','descripcion']
	success_url = reverse_lazy('u-app:listProyectos')

class ElimProyectos(DeleteView):
	template_name='estadia/eliminar.html'
	model = proyecto
	success_url = reverse_lazy('u-app:listProyectos')

