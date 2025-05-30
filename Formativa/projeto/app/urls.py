from django.urls import path
from .views import LoginView, UsuarioListCreate, UsuarioRestrieveUpdateDestroy, ReservaAmbienteListCreate, ReservaAmbienteRetrieveUpdateDestroy, ReservaAmbienteProfessorList, DisciplinaListCreate, DisciplinaRetrieveUpdateDestroy, DisciplinaProfessorList

urlpatterns = [
    #Login
    path('login/', LoginView.as_view()),

    #Usuario
    path('usuario/', UsuarioListCreate.as_view()),
    path('usuario/<int:pk>/', UsuarioRestrieveUpdateDestroy.as_view()),
    
    #Reserva
    path('reservas/', ReservaAmbienteListCreate.as_view()),
    path('reservas/<int:pk>/', ReservaAmbienteRetrieveUpdateDestroy.as_view()),
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    #Disciplina
    path('disciplinas/', DisciplinaListCreate.as_view()),
    path('disciplinas/<int:pk>', DisciplinaRetrieveUpdateDestroy.as_view()),
    path('professor/disciplinas/', DisciplinaProfessorList.as_view()),
]