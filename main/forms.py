from django import forms
from .models import Inscricao

class EtalForm (forms.ModelForm):
    LISTA_SEXO =[
    ('masculino', 'masculino'),
    ('feminino', 'feminino'),
]
    LISTA_MINICURSO =[
        ('1', 'intodução a computação grafica'),
        ('2', 'introdução a construção de jogos'),
        ('3', 'realidade virtual'),
        ('4', 'computação nas nuvens'),
]
    sexo = forms.ChoiceField(choices=LISTA_SEXO, widget=forms.RadioSelect)
    minicurso = forms.MultipleChoiceField(choices=LISTA_MINICURSO, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Inscricao
        fields = '__all__'