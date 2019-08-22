from django.conf import settings
from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    nome = models.CharField(max_length = 80)
    documento = models.PositiveIntegerField()
    telefone = models.CharField(max_length = 15)
    instituicao = models.ForeignKey('Curso', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 80)
    duracao = models.PositiveIntegerField
    tipo = models.CharField(max_length = 20)
    cargaHoraria =  models.PositiveIntegerField
    instituicao = models.ForeignKey('Instituicao', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length = 80)
    
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length = 80)
    serie = models.PositiveIntegerField
    tipo = models.CharField(max_length = 20)
    cargaHoraria =  models.PositiveIntegerField

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.nome

class Disc_has_aluno(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete = models.CASCADE)    
    disc = models.ForeignKey('Disciplina', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.aluno,self.disc)

