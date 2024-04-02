from django import forms
from .models import Alumno, Profesor, Curso
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'  # Aquí puedes especificar campos específicos si es necesario

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'  # Ajusta los campos según necesites

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'  # Ajusta los campos según necesites