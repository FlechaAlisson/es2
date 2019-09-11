from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Aluno, Disciplina, Curso, Instituicao
from .serializers import AlunoSerializer, DisciplinaSerializer, CursoSerializer, InstituicaoSerializer
from .forms import AlunoForm, CursoForm, InstituicaoForm, DisciplinaForm

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
    success_url = reverse_lazy('instituicaos')

class InstituicaoUpdate(LoginRequiredMixin, UpdateView):
    model = Instituicao
    form_class = InstituicaoForm
    template_name = 'instituicao/instituicao_form.html'
    success_url = reverse_lazy('instituicaos')

class InstituicaoDelete(LoginRequiredMixin, DeleteView):
    model = Instituicao
    success_url = reverse_lazy('instituicaos')
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

