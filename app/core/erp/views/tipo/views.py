from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Tipo
from core.erp.form import TipoForm

class TipoListView(ListView):
    model = Tipo
    template_name = 'tipo/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Profesion'
        context['create_url'] = reverse_lazy('erp:tipo_create')
        context['list_url'] = reverse_lazy('erp:tipo_list')
        context['entity'] = 'Profesion'
        return context

class TipoCreateView(CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/create.html'
    success_url = reverse_lazy('erp:tipo_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Profesion'
        context['entity'] = 'Profesion'
        context['list_url'] = reverse_lazy('erp:tipo_list')
        context['action'] = 'add'
        return context

class TipoUpdateView(UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/create.html'
    success_url = reverse_lazy('erp:tipo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Profesion'
        context['entity'] = 'Profesion'
        context['list_url'] = reverse_lazy('erp:tipo_list')
        context['action'] = 'edit'
        return context

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = 'tipo/delete.html'
    success_url = reverse_lazy('erp:tipo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Profesion'
        context['entity'] = 'Profesion'
        context['list_url'] = reverse_lazy('erp:tipo_list')
        return context