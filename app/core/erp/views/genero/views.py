from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Sexo
from core.erp.form import GeneroForm

class GeneroListView(ListView):
    model = Sexo
    template_name = 'genero/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Genero'
        context['create_url'] = reverse_lazy('erp:genero_create')
        context['list_url'] = reverse_lazy('erp:genero_list')
        context['entity'] = 'Genero'
        return context

class GeneroCreateView(CreateView):
    model = Sexo
    form_class = GeneroForm
    template_name = 'genero/create.html'
    success_url = reverse_lazy('erp:genero_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Genero'
        context['entity'] = 'Genero'
        context['list_url'] = reverse_lazy('erp:genero_list')
        context['action'] = 'add'
        return context

class GeneroUpdateView(UpdateView):
    model = Sexo
    form_class = GeneroForm
    template_name = 'genero/create.html'
    success_url = reverse_lazy('erp:genero_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Genero'
        context['entity'] = 'Genero'
        context['list_url'] = reverse_lazy('erp:genero_list')
        context['action'] = 'edit'
        return context

class GeneroDeleteView(DeleteView):
    model = Sexo
    template_name = 'genero/delete.html'
    success_url = reverse_lazy('erp:genero_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Genero'
        context['entity'] = 'Genero'
        context['list_url'] = reverse_lazy('erp:genero_list')
        return context