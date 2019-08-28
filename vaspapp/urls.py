from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import AlunoList, AlunoCreate, AlunoUpdate, AlunoDelete
from .views import CursoList, CursoCreate, CursoUpdate, CursoDelete
from .views import InstituicaoCreate, InstituicaoUpdate, InstituicaoDelete
from .views import DisciplinaList, DisciplinaCreate, DisciplinaUpdate, DisciplinaDelete



urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path("aluno/", AlunoList.as_view(), name='alunos'),
    path("aluno/disc/<int:disc>", AlunoList.as_view(), name='aluno-disciplina'),
    path("aluno/curso/<int:curso>", AlunoList.as_view(), name='aluno-curso'),
    path("aluno/add/", AlunoCreate.as_view(), name="aluno-add"),
    path("aluno/<int:pk>/", AlunoUpdate.as_view(), name="aluno-update"),
    path("aluno/<int:pk>/delete", AlunoDelete.as_view(), name="aluno-delete"),
    
    path("curso/", CursoList.as_view(), name='cursos'),
    path("curso/add/", CursoCreate.as_view(), name="curso-add"),
    path("curso/<int:pk>/", CursoUpdate.as_view(), name="curso-update"),
    path("curso/<int:pk>/delete", CursoDelete.as_view(), name="curso-delete"),

    path("instituicao/add/", InstituicaoCreate.as_view(), name="instituicao-add"),
    path("instituicao/<int:pk>/", InstituicaoUpdate.as_view(), name="instituicao-update"),
    path("instituicao/<int:pk>/delete", InstituicaoDelete.as_view(), name="instituicao-delete"),

    path("disciplina/", DisciplinaList.as_view(), name='disciplinas'),
    path("disciplina/curso/<int:curso>", DisciplinaList.as_view(), name='disciplina-curso'),
    path("disciplina/add/", DisciplinaCreate.as_view(), name="disciplina-add"),
    path("disciplina/<int:pk>/", DisciplinaUpdate.as_view(), name="disciplina-update"),
    path("disciplina/<int:pk>/delete", DisciplinaDelete.as_view(), name="disciplina-delete"),
]