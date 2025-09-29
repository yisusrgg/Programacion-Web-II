from django.db import models
from django.core.validators import FileExtensionValidator

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    pdf = models.FileField(
        upload_to='libros/pdfs/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name="PDF"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo