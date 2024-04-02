from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Alumno, Profesor, Curso
from .forms import AlumnoForm, ProfesorForm, CursoForm

# Definición correcta de la vista de inicio fuera de cualquier clase
def inicio(request):
    return render(request, 'inicio.html')

class RegistroAlumno(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'registro_alumno.html'
    success_url = reverse_lazy('listado_general')

class RegistroProfesor(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'registro_profesor.html'
    success_url = reverse_lazy('listado_general')

class RegistroCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'registro_curso.html'
    success_url = reverse_lazy('listado_general')

class ListadoGeneral(ListView):
    template_name = 'listado_general.html'
    context_object_name = 'elementos'

    def get_queryset(self):
        return {
            'alumnos': Alumno.objects.all(),
            'profesores': Profesor.objects.all(),
            'cursos': Curso.objects.all()
        }