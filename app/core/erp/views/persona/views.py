from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Persona
from core.erp.form import PersonaForm

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de Personas'
        context['create_url'] = reverse_lazy('erp:persona_create')
        context['list_url'] = reverse_lazy('erp:persona_list')
        context['entity'] = 'Persona'
        return context

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/create.html'
    success_url = reverse_lazy('erp:persona_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar Persona'
        context['entity'] = 'Persona'
        context['list_url'] = reverse_lazy('erp:persona_list')
        context['action'] = 'add'
        return context

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/create.html'
    success_url = reverse_lazy('erp:persona_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion Persona'
        context['entity'] = 'Persona'
        context['list_url'] = reverse_lazy('erp:persona_list')
        context['action'] = 'edit'
        return context

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('erp:persona_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar Persona'
        context['entity'] = 'Persona'
        context['list_url'] = reverse_lazy('erp:persona_list')
        return context