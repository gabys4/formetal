from django import forms
from .models import Inscricao

class EtalForm (forms.ModelForm):
    LISTA_SEXO =[
    ('masculino', 'masculino'),
    ('feminino', 'feminino'),
]

    sexo = forms.ChoiceField(choices=LISTA_SEXO, widget=forms.RadioSelect)
    class Meta:
        model = Inscricao
        fields = '__all__'