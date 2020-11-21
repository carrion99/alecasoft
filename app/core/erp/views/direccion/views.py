from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Direccion
from core.erp.form import DireccionForm

class DireccionListView(ListView):
    model = Direccion
    template_name = 'direccion/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Direccion'
        context['create_url'] = reverse_lazy('erp:direccion_create')
        context['list_url'] = reverse_lazy('erp:direccion_list')
        context['entity'] = 'Direcciones'
        return context

class DireccionCreateView(CreateView):
    model = Direccion
    form_class = DireccionForm
    template_name = 'direccion/create.html'
    success_url = reverse_lazy('erp:direccion_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Direccion'
        context['entity'] = 'Direcciones'
        context['list_url'] = reverse_lazy('erp:direccion_list')
        context['action'] = 'add'
        return context

class DireccionUpdateView(UpdateView):
    model = Direccion
    form_class = DireccionForm
    template_name = 'direccion/create.html'
    success_url = reverse_lazy('erp:direccion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion de Direccion'
        context['entity'] = 'Direcciones'
        context['list_url'] = reverse_lazy('erp:direccion_list')
        context['action'] = 'edit'
        return context

class DireccionDeleteView(DeleteView):
    model = Direccion
    template_name = 'direccion/delete.html'
    success_url = reverse_lazy('erp:direccion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Direcciones'
        context['entity'] = 'Direcciones'
        context['list_url'] = reverse_lazy('erp:direccion_list')
        return context