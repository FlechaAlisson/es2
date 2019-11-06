from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from bootstrap_datepicker_plus import DatePickerInput
from .models import Aluno, Curso, Instituicao, Disciplina, Frequencia, Professor, Turma

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [ 'nome', 'rg', 'cpf', 'telefone', 'curso', 'turmas' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [ 'nome', 'duracao', 'periodo', 'cargaHoraria', 'instituicao' ]
    
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
        fields = [ 'data', 'presenca' ]
        widgets = {
            'data': DatePickerInput(
                options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": False,
                    "showClear": True,
                    "showTodayButton": False,
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = [ 'nome', 'rg', 'cpf', 'telefone', 'curso' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = [ 'professor', 'disciplina' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))