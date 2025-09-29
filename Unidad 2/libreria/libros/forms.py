from django import forms
from .models import Libro

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'pdf']
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'pdf': 'Archivo PDF',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_pdf(self):
        pdf = self.cleaned_data.get('pdf')
        if pdf:
            if not pdf.name.endswith('.pdf'):
                raise forms.ValidationError("El archivo debe ser un PDF válido.")
        return pdf