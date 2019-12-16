from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Aluno, Disciplina, Curso, Instituicao, Professor, Matricula, Nota, Frequencia
from .serializers import AlunoSerializer, DisciplinaSerializer, CursoSerializer, InstituicaoSerializer
from .forms import AlunoForm, CursoForm, InstituicaoForm, DisciplinaForm, FrequenciaForm, NotaForm, MatriculaForm

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
    model = Matricula
    paginate_by = 20  # if pagination is desired
    template_name = 'frequencia/frequencia_list.html'

class FrequenciaCreate(LoginRequiredMixin, CreateView):
    form_class = FrequenciaForm
    template_name = 'frequencia/frequencia_form.html'
    def get_success_url(self):
        return reverse('frequencia-list', args={self.object.matricula.pk})

class FrequenciaUpdate(LoginRequiredMixin, UpdateView):
    model = Frequencia
    form_class = FrequenciaForm
    template_name = 'frequencia/frequencia_form.html'
    def get_success_url(self):
        return reverse('frequencia-list', args={self.object.matricula.pk})

class FrequenciaDelete(LoginRequiredMixin, DeleteView):
    model = Frequencia
    template_name = 'frequencia/frequencia_confirm_delete.html'
    def get_success_url(self):
        return reverse('frequencia-list', args={self.object.matricula.pk})

# ========== Nota CRUD ==========

class NotaList(LoginRequiredMixin, ListView):
    model = Matricula
    paginate_by = 20  # if pagination is desired
    template_name = 'nota/nota_list.html'

class NotaCreate(LoginRequiredMixin, CreateView):
    form_class = NotaForm
    template_name = 'nota/nota_form.html'
    def get_success_url(self):
        return reverse('nota-list', args={self.object.matricula.pk})

class NotaUpdate(LoginRequiredMixin, UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'nota/nota_form.html'
    def get_success_url(self):
        return reverse('nota-list', args={self.object.matricula.pk})

class NotaDelete(LoginRequiredMixin, DeleteView):
    model = Nota
    template_name = 'nota/nota_confirm_delete.html'
    def get_success_url(self):
        return reverse('nota-list', args={self.object.matricula.pk})

# ========== Matricula CRUD ==========

class MatriculaCreate(LoginRequiredMixin, CreateView):
    form_class = MatriculaForm
    template_name = 'matricula/matricula_form.html'
    def get_success_url(self):
        return reverse('matriculas-aluno', args={self.object.aluno.pk})

class MatriculaUpdate(LoginRequiredMixin, UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula/matricula_form.html'
    def get_success_url(self):
        return reverse('matriculas-aluno', args={self.object.aluno.pk})

class MatriculaDelete(LoginRequiredMixin, DeleteView):
    model = Matricula
    template_name = 'matricula/matricula_confirm_delete.html'
    def get_success_url(self):
        return reverse('matriculas-aluno', args={self.object.aluno.pk})

class MatriculasAluno(LoginRequiredMixin, ListView):
    model = Matricula
    template_name = 'matricula/matriculas_aluno.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('aluno'):
            context['aluno'] = Aluno.objects.get(pk=self.kwargs.get('aluno'))
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('aluno'):
            queryset = queryset.filter(aluno=self.kwargs['aluno'])
        return queryset

class NotasMatricula(LoginRequiredMixin, ListView):
    model = Nota
    template_name = 'nota/matricula_nota.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('matricula'):
            context['disciplina'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).disciplina
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
    template_name = 'frequencia/matricula_frequencia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.kwargs.get('matricula'):
            context['disciplina'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).disciplina
            context['aluno'] = Matricula.objects.get(pk=self.kwargs.get('matricula')).aluno
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('matricula'):
            queryset = queryset.filter(matricula=self.kwargs['matricula'])
        return queryset