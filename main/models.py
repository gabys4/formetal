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
    ('1', 'intodução a computação grafica'),
    ('2', 'introdução a construção de jogos'),
    ('3', 'realidade virtual'),
    ('4', 'computação nas nuvens'),
]


class Inscricao (models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=150)
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO)
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)
    minicurso = models.CharField(max_length=150, choices=LISTA_MINICURSO)


    def __str__(self):
        return self.nome
