from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.erp.models import Email
from core.erp.form import EmailForm

class EmailListView(ListView):
    model = Email
    template_name = 'email/list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Listado de E-mail'
        context['create_url'] = reverse_lazy('erp:email_create')
        context['list_url'] = reverse_lazy('erp:email_list')
        context['entity'] = 'E-mail'
        return context

class EmailCreateView(CreateView):
    model = Email
    form_class = EmailForm
    template_name = 'email/create.html'
    success_url = reverse_lazy('erp:email_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = ' Ingresar E-mail'
        context['entity'] = 'E-mail'
        context['list_url'] = reverse_lazy('erp:email_list')
        context['action'] = 'add'
        return context

class EmailUpdateView(UpdateView):
    model = Email
    form_class = EmailForm
    template_name = 'email/create.html'
    success_url = reverse_lazy('erp:email_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Edicion de E-mail'
        context['entity'] = 'E-mail'
        context['list_url'] = reverse_lazy('erp:email_list')
        context['action'] = 'edit'
        return context

class EmailDeleteView(DeleteView):
    model = Email
    template_name = 'email/delete.html'
    success_url = reverse_lazy('erp:email_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Eliminar E-mail'
        context['entity'] = 'E-mail'
        context['list_url'] = reverse_lazy('erp:email_list')
        return context