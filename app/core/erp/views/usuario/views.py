from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy

from core.erp.models import Usuario
from core.erp.form import UsuarioForm

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Usuarios'
        context['create_url'] = reverse_lazy('erp:usuario_create')
        context['list_url'] = reverse_lazy('erp:usuario_list')
        context['entity'] = 'Usuarios'
        return context

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/create.html'
    success_url = reverse_lazy('erp:usuario_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Usuarios'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('erp:usuario_list')
        context['action'] = 'add'
        return context

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/create.html'
    success_url = reverse_lazy('erp:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('erp:usuario_list')
        context['action'] = 'edit'
        return context

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario/delete.html'
    success_url = reverse_lazy('erp:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Usuarios'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('erp:usuario_list')
        return context