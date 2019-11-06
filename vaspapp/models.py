from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from enum import Enum

# class Periodo(models.Model):   # A subclass of Enum
#     periodo = models.CharField(max_length = 10)

# class TipoDisciplina(models.Model):
#     tipo = models.CharField(max_length = 10)

class Aluno(models.Model):
    nome = models.CharField(max_length = 80)
    rg = models.PositiveIntegerField(unique=True, null=True, blank=True, default=None)
    cpf = models.PositiveIntegerField(unique=True, blank=False, default=None) 
    telefone = models.CharField(max_length = 15)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE )
    turmas = models.ManyToManyField('Turma', related_name='alunos', blank = True, through='Matricula')

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return ( self.nome)

    def get_absolute_url(self):
        return reverse('alunos', kwargs={'pk': self.pk})

class Curso(models.Model):
    PERIODO = (
        ('INTEGRAL', 'Integral'),
        ('MATUTINO', 'Matutino'),
        ('VESPERTINO', 'Vespertino'),
        ('NOTURNO', 'Noturno'), 
    )
    nome = models.CharField(max_length = 80)
    duracao = models.PositiveIntegerField(null=True, blank=True, default=None)
    periodo = models.CharField(
        max_length = 10,
        choices = PERIODO,
    )
    cargaHoraria =  models.PositiveIntegerField(null=True, blank=True, default=None)
    instituicao = models.ForeignKey('Instituicao', on_delete = models.CASCADE)

    def publish(self):

        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome)

    def get_absolute_url(self):
        return reverse('cursos', kwargs={'pk': self.pk})

class Instituicao(models.Model):
    nome = models.CharField(max_length = 80)
    
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome)

    def get_absolute_url(self):
        return reverse('instituicaos', kwargs={'pk': self.pk})


class Disciplina(models.Model):
    TIPO = (
        ('ANUAL', 'Anual'),
        ('SEMESTRAL', 'Semestral'),
    )
    nome = models.CharField(max_length = 80)
    serie = models.PositiveIntegerField(null=True, blank=True, default=None)
    tipo = models.CharField(
        max_length = 10,
        choices = TIPO,
    )
    cargaHoraria =  models.PositiveIntegerField(null=True, blank=True, default=None)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome)
    
    def get_absolute_url(self):
        return reverse('disciplinas', kwargs={'pk': self.pk})


class Matricula(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete = models.PROTECT)
    turma = models.ForeignKey('Turma', on_delete = models.PROTECT)

    def publish(self):
        self.published_date = timezone.now
        self.save()

class Turma(models.Model):
    nome = models.CharField(max_length = 100, blank=False, default='%(professor.nome) - %(disciplina.nome)')
    professor = models.ForeignKey('Professor', on_delete = models.PROTECT)
    disciplina = models.ForeignKey('Disciplina', on_delete = models.PROTECT)

class Frequencia(models.Model):
    matricula = models.ForeignKey('Matricula', on_delete = models.PROTECT)
    data = models.DateField()
    presenca = models.BooleanField(blank=True, null=True, default=None)

    def publish(self):
        self.published_date = timezone.now
        self.save()
        
    def __str__(self):
        return self.presenca

class Nota(models.Model):
    matricula = models.ForeignKey('Matricula', on_delete = models.PROTECT)
    nota = models.FloatField(blank=True, null=True, default=None)
    avaliacao = models.ForeignKey('Avaliacao', on_delete = models.PROTECT)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nota)

class Avaliacao(models.Model):
    TIPO = (
        (1, 'Prova'),
        (2, 'Trabalho'),
    )
    avaliacao = models.CharField(max_length = 20, blank=False)
    peso = models.PositiveIntegerField(null=False, blank=False, default=1)
    tipo = models.PositiveIntegerField(choices = TIPO)
    data = models.DateField()
    dataPublicacao = models.DateField()
    turma = models.ForeignKey('Turma', on_delete = models.PROTECT)

class Professor(models.Model):
    nome = models.CharField(max_length = 80, blank=False)
    rg = models.PositiveIntegerField(unique=True, null=True, blank=True, default=None)
    cpf = models.PositiveIntegerField(unique=True, blank=False, default=None) 
    telefone = models.CharField(max_length = 15)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE )

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome)

