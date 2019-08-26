from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Aluno, Disciplina, Curso, Instituicao
from .serializers import AlunoSerializer, DisciplinaSerializer, CursoSerializer, InstituicaoSerializer
from .forms import AlunoForm

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

def aluno_create(request, template_name='aluno/aluno_form.html'):
    form = AlunoForm()
    if request.method == 'POST':
       form = AlunoForm(request.POST)
       if form.is_valid():
            form.save()
            # return redirect('')
    context = {
        "form": form
    }
    return render(request, template_name, context)

# def aluno_update(request, pk, template_name='aluno/aluno_form.html'):
#     book= get_object_or_404(Book, pk=pk)
#     form = BookForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return redirect('books_pc_multi_view2:home')
#     context = {}
#     context["form"] = form
#     context["book"] = book
#     return render(request, template_name, context)

# def aluno_delete(request, pk, template_name='aluno/aluno_confirm_delete.html'):
#     book= get_object_or_404(Book, pk=pk)    
#     if request.method=='POST':
#         book.delete()
#         return redirect('books_pc_multi_view2:home')
#     context = {}
#     context["object"] = book
#     context["book"] = book
#     return render(request, template_name, context)
