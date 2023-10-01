from django.db import models

class craquesDoVasco(models.Model):  
  POSICOES = [
    ('G','goleiro'),
    ('Z','zagueiro'),
    ('L','lateral'),
    ('M','meio-campo'),
    ('A','atacante')
  ]
  TIPODECONT = [
    ('E','empréstimo'),
    ('T','tranferência')
  ]
  nome = models.CharField(max_length=80)
  posicao = models.CharField(max_length=1,choices=POSICOES)
  nGols = models.IntegerField()
  tpDeContrato = models.CharField(max_length=1,choices=TIPODECONT)

class contratacoesDoVasco(models.Model): 
  POSICOES = [
    ('G','goleiro'),
    ('Z','zagueiro'),
    ('L','lateral'),
    ('M','meio-campo'),
    ('A','atacante')
  ]
  nome = models.CharField(max_length=80)
  posicao = models.CharField(max_length=1,choices=POSICOES)        
  deOndeVeio = models.CharField(max_length=80)
  valor = models.IntegerField()
