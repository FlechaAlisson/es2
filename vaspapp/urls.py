from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import AlunoList, AlunoCreate, AlunoUpdate, AlunoDelete
from .views import ProfessorList, ProfessorCreate, ProfessorUpdate, ProfessorDelete
from .views import CursoList, CursoCreate, CursoUpdate, CursoDelete
from .views import TurmaList, TurmaCreate, TurmaUpdate, TurmaDelete
from .views import InstituicaoList, InstituicaoCreate, InstituicaoUpdate, InstituicaoDelete
from .views import DisciplinaList, DisciplinaCreate, DisciplinaUpdate, DisciplinaDelete
from .views import FrequenciaList, FrequenciaCreate, FrequenciaUpdate, FrequenciaDelete
from .views import MatriculasAluno, NotasMatricula, FrequenciasMatricula



urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path("aluno/", AlunoList.as_view(), name='alunos'),
    path("aluno/disc/<int:disc>", AlunoList.as_view(), name='aluno-disciplina'),
    path("aluno/curso/<int:curso>", AlunoList.as_view(), name='aluno-curso'),
    path("aluno/add/", AlunoCreate.as_view(), name="aluno-add"),
    path("aluno/<int:pk>/edit", AlunoUpdate.as_view(), name="aluno-update"),
    path("aluno/<int:pk>/delete", AlunoDelete.as_view(), name="aluno-delete"),

    path("professor/", ProfessorList.as_view(), name='professores'),
    path("professor/disc/<int:disc>", ProfessorList.as_view(), name='professor-disciplina'),
    path("professor/curso/<int:curso>", ProfessorList.as_view(), name='professor-curso'),
    path("professor/add/", ProfessorCreate.as_view(), name="professor-add"),
    path("professor/<int:pk>/edit", ProfessorUpdate.as_view(), name="professor-update"),
    path("professor/<int:pk>/delete", ProfessorDelete.as_view(), name="professor-delete"),
    
    path("curso/", CursoList.as_view(), name='cursos'),
    path("curso/add/", CursoCreate.as_view(), name="curso-add"),
    path("curso/<int:pk>/edit", CursoUpdate.as_view(), name="curso-update"),
    path("curso/<int:pk>/delete", CursoDelete.as_view(), name="curso-delete"),

    path("turma/", TurmaList.as_view(), name='turmas'),
    path("turma/add/", TurmaCreate.as_view(), name="turma-add"),
    path("turma/<int:pk>/edit", TurmaUpdate.as_view(), name="turma-update"),
    path("turma/<int:pk>/delete", TurmaDelete.as_view(), name="turma-delete"),

    path("instituicao/", InstituicaoList.as_view(), name='instituicao'),
    path("instituicao/add/", InstituicaoCreate.as_view(), name="instituicao-add"),
    path("instituicao/<int:pk>/edit", InstituicaoUpdate.as_view(), name="instituicao-update"),
    path("instituicao/<int:pk>/delete", InstituicaoDelete.as_view(), name="instituicao-delete"),

    path("disciplina/", DisciplinaList.as_view(), name='disciplinas'),
    path("disciplina/curso/<int:curso>", DisciplinaList.as_view(), name='disciplina-curso'),
    path("disciplina/add/", DisciplinaCreate.as_view(), name="disciplina-add"),
    path("disciplina/<int:pk>/edit", DisciplinaUpdate.as_view(), name="disciplina-update"),
    path("disciplina/<int:pk>/delete", DisciplinaDelete.as_view(), name="disciplina-delete"),

    path("frequencia/", FrequenciaList.as_view(), name='frequencias'),
    path("frequencia/add/", FrequenciaCreate.as_view(), name="frequencia-add"),
    path("frequencia/<int:pk>/edit", FrequenciaUpdate.as_view(), name="frequencia-update"),
    path("frequencia/<int:pk>/delete", FrequenciaDelete.as_view(), name="frequencia-delete"),
     
    path("matriculas/<int:aluno>/", MatriculasAluno.as_view(), name="matriculas-aluno"),
    # path("nota/<int:matricula>/", NotasMatricula.as_view(), name="notas"),
    # path("frequencia/<int:matricula>/", FrequenciasMatricula.as_view(), name="frequencias"),
]