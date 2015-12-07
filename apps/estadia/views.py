from django.db.models import Q
from django.shortcuts import render, render_to_response
from django.http import request, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *
# from .forms import registroProeyecto


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

	def get_queryset(self):
		buscador = self.request.GET.get('search')
		queryset = alumno.objects.all()
		if buscador:
			queryset = queryset.filter(
				Q(nombre__icontains=buscador) |
				Q(apellidos__icontains=buscador)
			)
		return queryset

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

	def get_queryset(self):
		buscador = self.request.GET.get('search')
		queryset = asesor.objects.all()
		if buscador:
			queryset = queryset.filter(
				Q(nombre__icontains=buscador) |
				Q(apellidos__icontains=buscador) |
				Q(tipo__icontains=buscador)
			)
		return queryset

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

	def get_queryset(self):
		buscador = self.request.GET.get('search')
		queryset = categoria.objects.all()
		if buscador:
			queryset = queryset.filter(
				Q(tipo__icontains=buscador)
			)
		return queryset
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

	def get_queryset(self):
		buscador = self.request.GET.get('search')
		queryset = ciclos.objects.all()
		if buscador:
			queryset = queryset.filter(
				Q(generacion__icontains=buscador) |
				Q(ano_ini__icontains=buscador) |
				Q(ano_fin__icontains=buscador)
			)
		return queryset

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

def upload_file(request):
	if request.method == 'POST':
		form = registroProeyecto(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/success/url/')
	else:
		form = UploadFileForm()
	return render_to_response('upload.html', {'form': form})


class Proyectos(CreateView):
	template_name = 'estadia/detalles.html'
	model = proyecto
	#fields = ['titulo','alumnos', 'asesores', 'categoria', 'generacion', 'asignatura', 'estatus', 'resumenes', 'archivo']
	success_url = reverse_lazy('u-app:listProyectos')


class listProyectos(ListView):
	template_name = 'estadia/proyectos.html'
	model = proyecto

	def get_queryset(self):
		buscador = self.request.GET.get('search')
		queryset = proyecto.objects.all()
		if buscador:
			queryset = queryset.filter(
				Q(titulo__icontains=buscador)
			)
		return queryset

class EditProyectos(UpdateView):
	template_name = 'estadia/detalles.html'
	model = proyecto
	success_url = reverse_lazy('u-app:listProyectos')

class ElimProyectos(DeleteView):
	template_name='estadia/eliminar.html'
	model = proyecto
	success_url = reverse_lazy('u-app:listProyectos')

