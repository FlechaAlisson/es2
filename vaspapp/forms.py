from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [ 'nome', 'documento', 'telefone', 'curso', 'disciplinas' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))