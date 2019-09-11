from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Aluno, Curso, Instituicao, Disciplina, Nota, Frequencia

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [ 'nome', 'rg', 'cpf', 'telefone', 'curso', 'disciplinas' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [ 'nome', 'duracao', 'tipo', 'cargaHoraria', 'instituicao' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = [ 'nome' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = [ 'nome', 'serie', 'tipo', 'cargaHoraria', 'curso' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['data' , 'presenca']
    
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota', 'data']
    
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))