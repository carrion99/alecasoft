from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Telefono
from core.erp.form import TelefonoForm

class TelefonoListView(ListView):
    model = Telefono
    template_name = 'telefono/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Telefono'
        context['create_url'] = reverse_lazy('erp:telefono_create')
        context['list_url'] = reverse_lazy('erp:telefono_list')
        context['entity'] = 'Telefono'
        return context

class TelefonoCreateView(CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = 'telefono/create.html'
    success_url = reverse_lazy('erp:telefono_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Telefono'
        context['entity'] = 'Telefono'
        context['list_url'] = reverse_lazy('erp:telefono_list')
        context['action'] = 'add'
        return context

class TelefonoUpdateView(UpdateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = 'telefono/create.html'
    success_url = reverse_lazy('erp:telefono_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Telefono'
        context['entity'] = 'Telefono'
        context['list_url'] = reverse_lazy('erp:telefono_list')
        context['action'] = 'edit'
        return context

class TelefonoDeleteView(DeleteView):
    model = Telefono
    template_name = 'telefono/delete.html'
    success_url = reverse_lazy('erp:telefono_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Telefono'
        context['entity'] = 'Telefono'
        context['list_url'] = reverse_lazy('erp:telefono_list')
        return context