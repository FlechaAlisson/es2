from django.contrib import admin
from .models import Aluno, Disciplina, Instituicao, Curso, Matricula, Turma, Frequencia, Nota, Professor, Avaliacao

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Instituicao)
admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Frequencia)
admin.site.register(Nota)
admin.site.register(Professor)
admin.site.register(Avaliacao)
# Register your models here.
