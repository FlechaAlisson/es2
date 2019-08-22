from django.contrib import admin
from .models import Aluno,Disciplina,Disc_has_aluno,Instituicao,Curso

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Disc_has_aluno)
admin.site.register(Instituicao)
admin.site.register(Curso)
# Register your models here.
