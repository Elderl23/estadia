from django.db.models import Q
from django.http import request
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.http.request import *
from django.core.urlresolvers import reverse_lazy
from apps.estadia.models import *


class listAlumnos(ListView):
    template_name = 'busqueda/alumnos.html'
    model = alumno

    def get_queryset(self):
        buscador = self.request.GET.get('search')
        queryset = alumno.objects.all()
        if buscador:
            queryset = queryset.filter(
                Q(nombre__icontains=buscador)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(listAlumnos, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class buscar(TemplateView):
    template_name = 'busqueda/buscar.html'


class buscarProyectoAlumnosView(TemplateView):
    template_name = 'busqueda/proyectos_alumnos.html'

    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscar']
        proyectos = proyecto.objects.filter(titulo__contains=buscar)
        if proyectos:
            datosPro =[]
            for proyectol in proyectos:
                alumnos = proyectol.alumno.all()
                datosPro.append(dict([(proyectol, alumnos)]))
            return render(request, 'busqueda/proyectos_alumnos.html',
                          {'datosPro': datosPro})
        else:
            alumnos = alumno.objects.filter(nombre__contains=buscar)
        return render(request, 'busqueda/proyectos_alumnos.html',
                      {'alumnos':alumnos, 'alumno':True})
