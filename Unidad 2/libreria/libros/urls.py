from django.urls import path
from .views import ListaLibros, CrearLibro, EditarLibro, EliminarLibro

urlpatterns = [
    path('', ListaLibros.as_view(), name='lista_libros'),
    path('crear/', CrearLibro.as_view(), name='crear_libro'),
    path('editar/<int:pk>/', EditarLibro.as_view(), name='editar_libro'),
    path('eliminar/<int:pk>/', EliminarLibro.as_view(), name='eliminar_libro'),
]