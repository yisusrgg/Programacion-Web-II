from django import forms
from .models import Libro

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'pdf']
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'pdf': 'Archivo (PDF o Imagen)',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_pdf(self):
        archivo = self.cleaned_data.get('pdf')
        if archivo:
            extension = archivo.name.split('.')[-1].lower()
            extensiones_permitidas = ['pdf', 'jpg', 'jpeg', 'png', 'gif']
            if extension not in extensiones_permitidas:
                raise forms.ValidationError("El archivo debe ser un PDF o una imagen (JPG, JPEG, PNG, GIF).")
        return archivo