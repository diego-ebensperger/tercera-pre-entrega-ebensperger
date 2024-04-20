from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Alumno, Profesor, Curso
from .forms import AlumnoForm, ProfesorForm, CursoForm, SearchForm

def inicio(request):
    return render(request, 'padre.html')

class RegistroAlumno(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'registro_alumno.html'
    success_url = reverse_lazy('listado_general')

class UpdateAlumno(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'update_alumno.html'
    success_url = reverse_lazy('listado_general')

class DeleteAlumno(DeleteView):
    model = Alumno
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('listado_general')

class RegistroProfesor(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'registro_profesor.html'
    success_url = reverse_lazy('listado_general')

class UpdateProfesor(UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'update_profesor.html'
    success_url = reverse_lazy('listado_general')

class DeleteProfesor(DeleteView):
    model = Profesor
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('listado_general')

class RegistroCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'registro_curso.html'
    success_url = reverse_lazy('listado_general')

class UpdateCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'update_curso.html'
    success_url = reverse_lazy('listado_general')

class DeleteCurso(DeleteView):
    model = Curso
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('listado_general')

class ListadoGeneral(ListView):
    template_name = 'listado_general.html'
    context_object_name = 'elementos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return {
                'alumnos': Alumno.objects.filter(nombre__icontains=query),
                'profesores': Profesor.objects.filter(nombre__icontains=query),
                'cursos': Curso.objects.filter(nombre__icontains=query)
            }
        return {
            'alumnos': Alumno.objects.all(),
            'profesores': Profesor.objects.all(),
            'cursos': Curso.objects.all()
        }