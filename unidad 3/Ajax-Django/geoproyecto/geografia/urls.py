from django.urls import path
from . import views

urlpatterns = [
    path('', views.selector_view, name='selector'),
    
    path('ajax/cargar-municipios/', views.cargar_municipios_view, name='ajax_cargar_municipios'),
]