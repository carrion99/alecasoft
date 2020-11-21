from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy

from core.erp.models import Ciudad
from core.erp.form import CiudadForm

class CiudadListView(ListView):
    model = Ciudad
    template_name = 'ciudad/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Ciudades'
        context['create_url'] = reverse_lazy('erp:ciudad_create')
        context['list_url'] = reverse_lazy('erp:ciudad_list')
        context['entity'] = 'Ciudades'
        return context

class CiudadCreateView(CreateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'ciudad/create.html'
    success_url = reverse_lazy('erp:ciudad_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Ciudad'
        context['entity'] = 'Ciudades'
        context['list_url'] = reverse_lazy('erp:ciudad_list')
        context['action'] = 'add'
        return context

class CiudadUpdateView(UpdateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'ciudad/create.html'
    success_url = reverse_lazy('erp:ciudad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Ciudad'
        context['entity'] = 'Ciudades'
        context['list_url'] = reverse_lazy('erp:ciudad_list')
        context['action'] = 'edit'
        return context

class CiudadDeleteView(DeleteView):
    model = Ciudad
    template_name = 'ciudad/delete.html'
    success_url = reverse_lazy('erp:ciudad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Ciudad'
        context['entity'] = 'Ciudades'
        context['list_url'] = reverse_lazy('erp:ciudad_list')
        return context