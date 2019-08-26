from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Aluno, Disciplina, Curso, Instituicao
from .serializers import AlunoSerializer, DisciplinaSerializer, CursoSerializer, InstituicaoSerializer
from .forms import AlunoForm, CursoForm

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

def aluno_view(request, pk, template_name='aluno/aluno_view.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    context = {
        "aluno": aluno,
    }
    return render(request, template_name, context)

class AlunoCreate(CreateView):
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    # success_url = '/'

class AlunoUpdate(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'

class AlunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno-add')
    template_name = 'aluno/aluno_confirm_delete.html'

# ========== Curso CRUD ==========

class CursoCreate(CreateView):
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    # success_url = '/'

class CursoUpdate(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'

class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy('curso-add')
    template_name = 'curso/curso_confirm_delete.html'
