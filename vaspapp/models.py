from django.conf import settings
from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    nome = models.CharField(max_length = 80)
    documento = models.PositiveIntegerField(null=True, blank=True, default=None)
    telefone = models.CharField(max_length = 15)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE )
    disciplinas = models.ManyToManyField('Disciplina', related_name='alunos', blank = True)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return ( self.nome)

    def get_absolute_url(self):
        return reverse('aluno-add', kwargs={'pk': self.pk})

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
        return reverse('curso', kwargs={'pk': self.pk})

class Instituicao(models.Model):
    nome = models.CharField(max_length = 80)
    
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome)


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



