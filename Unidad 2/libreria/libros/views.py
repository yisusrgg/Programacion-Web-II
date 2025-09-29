from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from .forms import FormularioLibro

class ListaLibros(ListView):
    model = Libro
    template_name = 'libros/lista_libros.html'
    context_object_name = 'libros'

class CrearLibro(CreateView):
    model = Libro
    form_class = FormularioLibro
    template_name = 'libros/formulario_libro.html'
    success_url = reverse_lazy('lista_libros')

class EditarLibro(UpdateView):
    model = Libro
    form_class = FormularioLibro
    template_name = 'libros/formulario_libro.html'
    success_url = reverse_lazy('lista_libros')

class EliminarLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('lista_libros')