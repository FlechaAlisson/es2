from django.conf import settings
from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 80)
    documento = models.PositiveIntegerField()
    telefone = models.CharField(max_length = 15)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return ( self.nome,self.id)

class Curso(models.Model):
    curso_id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 80)
    duracao = models.PositiveIntegerField
    tipo = models.CharField(max_length = 20)
    cargaHoraria =  models.PositiveIntegerField
    instituicao = models.ForeignKey('Instituicao', on_delete = models.CASCADE)

    def publish(self):

        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome,  self.curso_id)

class Instituicao(models.Model):
    instituicao_id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 80)
    
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome, self.instituicao_id)


class Disciplina(models.Model):
    discplina_id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 80)
    serie = models.PositiveIntegerField
    tipo = models.CharField(max_length = 20)
    cargaHoraria =  models.PositiveIntegerField

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.nome, self.discplina_id)

class Disc_has_aluno(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete = models.CASCADE)    
    disc = models.ForeignKey('Disciplina', on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return (self.aluno,self.disc)

