from django.urls import path
from .views import inicio, RegistroAlumno, RegistroProfesor, RegistroCurso, ListadoGeneral

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registro/alumno/', RegistroAlumno.as_view(), name='registro_alumno'),
    path('registro/profesor/', RegistroProfesor.as_view(), name='registro_profesor'),
    path('registro/curso/', RegistroCurso.as_view(), name='registro_curso'),
    path('listado/general/', ListadoGeneral.as_view(), name='listado_general'),
]
