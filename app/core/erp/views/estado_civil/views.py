from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Estado_Civil
from core.erp.form import Estado_CivilForm

class EstadoCivilListView(ListView):
    model = Estado_Civil
    template_name = 'estado-civil/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Estado Civil'
        context['create_url'] = reverse_lazy('erp:estado_civil_create')
        context['list_url'] = reverse_lazy('erp:estado_civil_list')
        context['entity'] = 'Ciudades'
        return context

class EstadoCivilCreateView(CreateView):
    model = Estado_Civil
    form_class = Estado_CivilForm
    template_name = 'estado-civil/create.html'
    success_url = reverse_lazy('erp:estado_civil_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Estado Civil'
        context['entity'] = 'Estado Civil'
        context['list_url'] = reverse_lazy('erp:estado_civil_list')
        context['action'] = 'add'
        return context

class EstadoCivilUpdateView(UpdateView):
    model = Estado_Civil
    form_class = Estado_CivilForm
    template_name = 'estado-civil/create.html'
    success_url = reverse_lazy('erp:estado_civil_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Estado Civil'
        context['entity'] = 'Estado civil'
        context['list_url'] = reverse_lazy('erp:estado_civil_list')
        context['action'] = 'edit'
        return context

class EstadoCivilDeleteView(DeleteView):
    model = Estado_Civil
    template_name = 'estado-civil/delete.html'
    success_url = reverse_lazy('erp:estado_civil_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Estado Civil'
        context['entity'] = 'Estado Civil'
        context['list_url'] = reverse_lazy('erp:estado_civil_list')
        return context