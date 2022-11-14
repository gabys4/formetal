from django.db import models

LISTA_SEXO =[
    ('masculino', 'masculino'),
    ('feminino', 'feminino'),
]

LISTA_CURSO =[
    ('informatica', 'informatica'),
    ('alimentos', 'alimentos'),
    ('apicultura', 'apicultura'),
]

LISTA_MINICURSO =[
    ('intodução a computação grafica', 'intodução a computação grafica'),
    ('introdução a construção de jogos', 'introdução a construção de jogos'),
    ('realidade virtual', 'realidade virtual'),
    ('computação nas nuvens', 'computação nas nuvens'),
]


class Inscricao (models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=150)
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO)
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)
    opcao1 = models.BooleanField(verbose_name='intodução a computação grafica')
    opcao2 = models.BooleanField(verbose_name='introdução a construção de jogos')
    opcao3 = models.BooleanField(verbose_name='realidade virtual')
    opcao4 = models.BooleanField(verbose_name='computação nas nuvens')
    


    def __str__(self):
        return self.nome
