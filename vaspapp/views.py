from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno, Disc_has_aluno, Disciplina, Curso,Instituicao
from .serializers import AlunoSerializer, Disc_has_alunoSerializer, DisciplinaSerializer, CursoSerializer, InstituicaoSerializer

class AlunoViewSet(viewsets.ModelViewSet):

    queryset = Aluno.objects
    serializer_class = AlunoSerializer

class Disc_has_alunoViewSet(viewsets.ModelViewSet):

    queryset = Disc_has_aluno.objects
    serializer_class = Disc_has_alunoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):

    queryset = Disciplina.objects
    serializer_class = DisciplinaSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects
    serializer_class = CursoSerializer

class InsituicaoViewSet(viewsets.ModelViewSet):

    queryset = Instituicao.objects
    serializer_class = InstituicaoSerializer
