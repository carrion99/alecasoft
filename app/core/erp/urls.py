from django.urls import path
from core.erp.views.ciudad.views import *
from core.erp.views.dashboard.views import DashboardView
from core.erp.views.usuario.views import *
from core.erp.views.estado_civil.views import *
from core.erp.views.direccion.views import *
from core.erp.views.telefono.views import *
from core.erp.views.tipo.views import *
from core.erp.views.email.views import *
from core.erp.views.genero.views import *
from core.erp.views.persona.views import PersonaListView, PersonaCreateView, PersonaDeleteView, PersonaUpdateView

app_name = 'erp'

urlpatterns = [
    path('ciudad/list/', CiudadListView.as_view() , name='ciudad_list'),
    path('ciudad/add/', CiudadCreateView.as_view() , name='ciudad_create'),
    path('ciudad/edit/<int:pk>/', CiudadUpdateView.as_view() , name='ciudad_update'),
    path('ciudad/delete/<int:pk>/', CiudadDeleteView.as_view() , name='ciudad_delete'),
    #
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #
    path('usuario/list/', UsuarioListView.as_view() , name='usuario_list'),
    path('usuario/add/', UsuarioCreateView.as_view() , name='usuario_create'),
    path('usuario/edit/<int:pk>/', UsuarioUpdateView.as_view() , name='usuario_update'),
    path('usuario/delete/<int:pk>/', UsuarioDeleteView.as_view() , name='usuario_delete'),
    #
    path('estado-civil/list/', EstadoCivilListView.as_view() , name='estado_civil_list'),
    path('estado-civil/add/', EstadoCivilCreateView.as_view() , name='estado_civil_create'),
    path('estado-civil/edit/<int:pk>/', EstadoCivilUpdateView.as_view() , name='estado_civil_update'),
    path('estado-civil/delete/<int:pk>/', EstadoCivilDeleteView.as_view() , name='estado_civil_delete'),
    #
    path('direccion/list/', DireccionListView.as_view() , name='direccion_list'),
    path('direccion/add/', DireccionCreateView.as_view() , name='direccion_create'),
    path('direccion/edit/<int:pk>/', DireccionUpdateView.as_view() , name='direccion_update'),
    path('direccion/delete/<int:pk>/', DireccionDeleteView.as_view() , name='direccion_delete'),
    #
    path('telefono/list/', TelefonoListView.as_view() , name='telefono_list'),
    path('telefono/add/', TelefonoCreateView.as_view() , name='telefono_create'),
    path('telefono/edit/<int:pk>/', TelefonoUpdateView.as_view() , name='telefono_update'),
    path('telefono/delete/<int:pk>/', TelefonoDeleteView.as_view() , name='telefono_delete'),
    #
    path('tipo/list/', TipoListView.as_view() , name='tipo_list'),
    path('tipo/add/', TipoCreateView.as_view() , name='tipo_create'),
    path('tipo/edit/<int:pk>/', TipoUpdateView.as_view() , name='tipo_update'),
    path('tipo/delete/<int:pk>/', TipoDeleteView.as_view() , name='tipo_delete'),
    #
    path('email/list/', EmailListView.as_view() , name='email_list'),
    path('email/add/', EmailCreateView.as_view() , name='email_create'),
    path('email/edit/<int:pk>/', EmailUpdateView.as_view() , name='email_update'),
    path('email/delete/<int:pk>/', EmailDeleteView.as_view() , name='email_delete'),
    #
    path('genero/list/', GeneroListView.as_view() , name='genero_list'),
    path('genero/add/', GeneroCreateView.as_view() , name='genero_create'),
    path('genero/edit/<int:pk>/', GeneroUpdateView.as_view() , name='genero_update'),
    path('genero/delete/<int:pk>/', GeneroDeleteView.as_view() , name='genero_delete'),
    #
    path('persona/list/', PersonaListView.as_view() , name='persona_list'),
    path('persona/add/', PersonaCreateView.as_view() , name='persona_create'),
    path('persona/edit/<int:pk>/', PersonaUpdateView.as_view() , name='persona_update'),
    path('persona/delete/<int:pk>/', PersonaDeleteView.as_view() , name='persona_delete')
]
