from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Aluno, Disciplina, Curso, Instituicao, Professor, Matricula, Nota, Frequencia, Turma
from .serializers import AlunoSerializer, DisciplinaSerializer, CursoSerializer, InstituicaoSerializer
from .forms import AlunoForm, CursoForm, InstituicaoForm, DisciplinaForm, FrequenciaForm, ProfessorForm, TurmaForm

class AlunoViewSet(viewsets.ModelViewSet):

    queryset = Aluno.objects
    serializer_class = AlunoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):

    queryset = Disciplina.objects
    serializer_class = DisciplinaSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects
    serializer_class = CursoSerializer

class InsituicaoViewSet(viewsets.ModelViewSet):

    queryset = Instituicao.objects
    serializer_class = InstituicaoSerializer

# ========== Aluno CRUD ==========

class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    paginate_by = 20  # if pagination is desired
    template_name = 'aluno/aluno_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('disc'):
            context['disc'] = Disciplina.objects.get(pk=self.kwargs.get('disc'))
        if self.kwargs.get('curso'):
            context['curso'] = Curso.objects.get(pk=self.kwargs.get('curso'))
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        curso = self.request.GET.get('curso')
        if curso is not None:
            queryset = queryset.filter(curso=curso)
        if self.kwargs.get('disc'):
            queryset = queryset.filter(disciplinas__id=self.kwargs.get('disc'))
        if self.kwargs.get('curso'):
            queryset = queryset.filter(curso=self.kwargs.get('curso'))
        return queryset

class AlunoCreate(LoginRequiredMixin, CreateView):
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('alunos')

class AlunoUpdate(LoginRequiredMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('alunos')

class AlunoDelete(LoginRequiredMixin, DeleteView):
    model = Aluno
    success_url = reverse_lazy('alunos')
    template_name = 'aluno/aluno_confirm_delete.html'

# ========== Professor CRUD ==========

class ProfessorList(LoginRequiredMixin, ListView):
    model = Professor
    paginate_by = 20  # if pagination is desired
    template_name = 'professor/professor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('disc'):
            context['disc'] = Disciplina.objects.get(pk=self.kwargs.get('disc'))
        if self.kwargs.get('curso'):
            context['curso'] = Curso.objects.get(pk=self.kwargs.get('curso'))
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        curso = self.request.GET.get('curso')
        if curso is not None:
            queryset = queryset.filter(curso=curso)
        if self.kwargs.get('disc'):
            queryset = queryset.filter(disciplinas__id=self.kwargs.get('disc'))
        if self.kwargs.get('curso'):
            queryset = queryset.filter(curso=self.kwargs.get('curso'))
        return queryset

class ProfessorCreate(LoginRequiredMixin, CreateView):
    form_class = ProfessorForm
    template_name = 'professor/professor_form.html'
    success_url = reverse_lazy('professores')

class ProfessorUpdate(LoginRequiredMixin, UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor/professor_form.html'
    success_url = reverse_lazy('professores')

class ProfessorDelete(LoginRequiredMixin, DeleteView):
    model = Professor
    success_url = reverse_lazy('professores')
    template_name = 'professor/professor_confirm_delete.html'

# ========== Curso CRUD ==========

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    paginate_by = 20  # if pagination is desired
    template_name = 'curso/curso_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CursoCreate(LoginRequiredMixin, CreateView):
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('cursos')

class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('cursos')

class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')
    template_name = 'curso/curso_confirm_delete.html'

# ========== Instituição CRUD ==========

class InstituicaoList(LoginRequiredMixin, ListView):
    model = Instituicao
    paginate_by = 20  # if pagination is desired
    template_name = 'instituicao/instituicao_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class InstituicaoCreate(LoginRequiredMixin, CreateView):
    form_class = InstituicaoForm
    template_name = 'instituicao/instituicao_form.html'
    success_url = reverse_lazy('instituicao')

class InstituicaoUpdate(LoginRequiredMixin, UpdateView):
    model = Instituicao
    form_class = InstituicaoForm
    template_name = 'instituicao/instituicao_form.html'
    success_url = reverse_lazy('instituicao')

class InstituicaoDelete(LoginRequiredMixin, DeleteView):
    model = Instituicao
    success_url = reverse_lazy('instituicao')
    template_name = 'instituicao/instituicao_confirm_delete.html'

# ========== Disciplina CRUD ==========

class DisciplinaList(LoginRequiredMixin, ListView):
    model = Disciplina
    paginate_by = 20  # if pagination is desired
    template_name = 'disciplina/disciplina_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('curso'):
            context['curso'] = Curso.objects.get(pk=self.kwargs.get('curso'))
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('curso'):
            queryset = queryset.filter(curso=self.kwargs.get('curso'))
        return queryset

class DisciplinaCreate(LoginRequiredMixin, CreateView):
    form_class = DisciplinaForm
    template_name = 'disciplina/disciplina_form.html'
    success_url = reverse_lazy('disciplinas')

class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina/disciplina_form.html'
    success_url = reverse_lazy('disciplinas')

class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    model = Disciplina
    success_url = reverse_lazy('disciplinas')
    template_name = 'disciplina/disciplina_confirm_delete.html'

# ========== Frequencia CRUD ==========

class FrequenciaList(LoginRequiredMixin, ListView):
    model = Disciplina
    paginate_by = 20  # if pagination is desired
    template_name = 'frequencia/frequencia_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('curso'):
            context['curso'] = Curso.objects.get(pk=self.kwargs.get('curso'))
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('curso'):
            queryset = queryset.filter(curso=self.kwargs.get('curso'))
        return queryset

class FrequenciaCreate(LoginRequiredMixin, CreateView):
    form_class = FrequenciaForm
    template_name = 'frequencia/frequencia_form.html'
    success_url = reverse_lazy('frequencias')

class FrequenciaUpdate(LoginRequiredMixin, UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'frequencia/frequencia_form.html'
    success_url = reverse_lazy('frequencias')

class FrequenciaDelete(LoginRequiredMixin, DeleteView):
    model = Disciplina
    success_url = reverse_lazy('frequencias')
    template_name = 'frequencia/frequencia_confirm_delete.html'


# ========== Matricula CRUD ==========

class MatriculasAluno(LoginRequiredMixin, ListView):
    model = Matricula
    template_name = 'matricula/matriculas_aluno.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('aluno'):
            context['aluno'] = Aluno.objects.get(pk=self.kwargs.get('aluno'))
        # context['frequencias'] = Frequencia.objects.get(matricula=self.object_list)
        # context['notas'] = Nota.objects.get(matricula=self.object_list)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('aluno'):
            queryset = queryset.filter(aluno=self.kwargs['aluno'])
        return queryset

class NotasMatricula(LoginRequiredMixin, ListView):
    model = Nota
    template_name = 'nota/nota_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('matricula'):
            context['disciplina'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).turma.disciplina
            context['aluno'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).aluno
        # context['frequencias'] = Frequencia.objects.get(matricula=self.object_list)
        # context['notas'] = Nota.objects.get(matricula=self.object_list)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('matricula'):
            queryset = queryset.filter(matricula=self.kwargs['matricula'])
        return queryset

class FrequenciasMatricula(LoginRequiredMixin, ListView):
    model = Frequencia
    template_name = 'frequencia/frequencia_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('matricula'):
            context['disciplina'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).turma.disciplina
            context['aluno'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).aluno
        # context['frequencias'] = Frequencia.objects.get(matricula=self.object_list)
        # context['notas'] = Nota.objects.get(matricula=self.object_list)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('matricula'):
            queryset = queryset.filter(matricula=self.kwargs['matricula'])
        return queryset

# ========== Instituição CRUD ==========

class TurmaList(LoginRequiredMixin, ListView):
    model = Turma
    paginate_by = 20  # if pagination is desired
    template_name = 'turma/turma_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TurmaCreate(LoginRequiredMixin, CreateView):
    form_class = TurmaForm
    template_name = 'turma/turma_form.html'
    success_url = reverse_lazy('turmas')

class TurmaUpdate(LoginRequiredMixin, UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma/turma_form.html'
    success_url = reverse_lazy('turmas')

class TurmaDelete(LoginRequiredMixin, DeleteView):
    model = Turma
    success_url = reverse_lazy('turmas')
    template_name = 'turma/turma_confirm_delete.html'