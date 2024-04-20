from django.urls import path
from .views import inicio, RegistroAlumno, RegistroProfesor, RegistroCurso, ListadoGeneral
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('registro/alumno/', RegistroAlumno.as_view(), name='registro_alumno'),
    path('registro/profesor/', RegistroProfesor.as_view(), name='registro_profesor'),
    path('registro/curso/', RegistroCurso.as_view(), name='registro_curso'),
    path('listado/general/', ListadoGeneral.as_view(), name='listado_general'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

