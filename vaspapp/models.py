from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Aluno(models.Model):
    nome = models.CharField(max_length = 80)
    rg = models.PositiveIntegerField(unique=True,null=True, blank=True, default=None)
    cpf = models.PositiveIntegerField(unique=True,null=True, blank=True, default=None) 
    telefone = models.CharField(max_length = 15)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE )
    disciplinas = models.ManyToManyField('Disciplina', related_name='alunos', blank = True, through= 'Matricula')

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return ( self.nome)

    def get_absolute_url(self):
        return reverse('alunos', kwargs={'pk': self.pk})

class Curso(models.Model):
    nome = models.CharField(max_length = 80)
    duracao = models.PositiveIntegerField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length = 20)
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
    nome = models.CharField(max_length = 80)
    serie = models.PositiveIntegerField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length = 20)
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
    disciplina = models.ForeignKey('Disciplina', on_delete = models.PROTECT)

    def publish(self):
        self.published_date = timezone.now
        self.save()

class Frequencia(models.Model):
    matricula = models.ForeignKey('Matricula', on_delete = models.PROTECT)
    data = models.DateField()
    presenca = models.BinaryField()

    def publish(self):
        self.published_date = timezone.now
        self.save()
        
    def __str__(self):
        return self.presenca

class Nota(models.Model):
    matricula = models.ForeignKey('Matricula', on_delete = models.PROTECT)
    nota =  models.FloatField(null=True, blank=True, default=None)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return ( self.nota)



class Professor(models.Model):
    nome = models.CharField(max_length = 80)
    rg = models.PositiveIntegerField(unique=True,null=True, blank=True, default=None)
    cpf = models.PositiveIntegerField(unique=True,null=True, blank=True, default=None) 
    telefone = models.CharField(max_length = 15)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE )
    disciplinas = models.ManyToManyField('Disciplina', related_name='professores', blank = True)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return ( self.nome)

