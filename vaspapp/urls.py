from django.urls import path
from . import views
from .views import AlunoCreate, AlunoUpdate, AlunoDelete, CursoCreate, CursoUpdate, CursoDelete

urlpatterns = [
    # path("", views.home, name="home"),
    # path("aluno/", views.aluno_view, name="aluno-list"),
    # path("aluno/<int:pk>/", views.aluno_view, name="aluno_view"),
    path("aluno/add/", AlunoCreate.as_view(), name="aluno-add"),
    path("aluno/<int:pk>/", AlunoUpdate.as_view(), name="aluno-update"),
    path("aluno/<int:pk>/delete", AlunoDelete.as_view(), name="aluno-delete"),
    
    path("curso/add/", CursoCreate.as_view(), name="curso-add"),
    path("curso/<int:pk>/", CursoUpdate.as_view(), name="curso-update"),
    path("curso/<int:pk>/delete", CursoDelete.as_view(), name="curso-delete"),
]