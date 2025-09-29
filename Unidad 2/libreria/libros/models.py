from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    pdf = models.FileField(
        upload_to='libros/archivos/',  
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'gif'])],  
        verbose_name="Archivo (PDF o Imagen)"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo

@receiver(post_delete, sender=Libro)
def eliminar_archivo(sender, instance, **kwargs):

    if instance.pdf:
        if os.path.isfile(instance.pdf.path):
            os.remove(instance.pdf.path)