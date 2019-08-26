from rest_framework import serializers
from .models import Aluno, Curso, Instituicao, Disciplina



class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
        
# class Disc_has_alunoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Disc_has_aluno
#         fields = '__all__'