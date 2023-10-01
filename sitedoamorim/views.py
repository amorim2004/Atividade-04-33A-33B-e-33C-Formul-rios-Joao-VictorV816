from django.shortcuts import render,redirect
from .models import craquesDoVasco,contratacoesDoVasco

# Create your views here.
def meuApp(request):
  craques = craquesDoVasco.objects.all()
  contratacoes = contratacoesDoVasco.objects.all()
  return render(request, 'meuApp.html',context={'craquesDoVasco': craques, 'contratacoesDoVasco':contratacoes})

def create_craque(request):
  if request.method=='POST':
    print(request.POST)
    craquesDoVasco.objects.create(
      nome= request.POST['nome'],
      posicao=request.POST['posicao'],
      nGols=request.POST['nGols'],
      tpDeContrato=request.POST['tpDeContrato']
    )

    return redirect ('meuApp')

  options_tpDeContrato = craquesDoVasco.tpDeContrato.field.choices
  options_posicao = craquesDoVasco.posicao.field.choices
  return render(request, 'forms_craques.html',context={
    'type': 'Adicionar',
    'options_posicao': options_posicao,
    'options_tpDeContrato':options_tpDeContrato
  })

def update_craque(request,id):
  craque= craquesDoVasco.objects.get(id=id)
  if request.method=='POST':
      craque.nome= request.POST['nome']
      craque.posicao=request.POST['posicao']
      craque.nGols=request.POST['nGols']
      craque.tpDeContrato=request.POST['tpDeContrato']
      craque.save()
    
      return redirect ('meuApp')
  options_tpDeContrato = craquesDoVasco.tpDeContrato.field.choices
  options_posicao = craquesDoVasco.posicao.field.choices
  return render(request, 'forms_craques.html', context={
    'type': 'Atualizar',
    'craque': craque,
    'options_posicao': options_posicao,
    'options_tpDeContrato':options_tpDeContrato
  })

def delete_craque(request,id):
  craque= craquesDoVasco.objects.get(id=id)
  if request.method=='POST':
    if request.POST['confirm']:
      craque.delete()
    
      return redirect ('meuApp')   
  return render(request, 'are_you_sure_craques.html', context={'craque': craque})


def create_cont(request):
  if request.method=='POST':
    contratacoesDoVasco.objects.create(
      nome= request.POST['nome'],
      posicao=request.POST['posicao'],
      deOndeVeio=request.POST['deOndeVeio'],
      valor=request.POST['valor']
    )

    return redirect ('meuApp')
  options_posicao = craquesDoVasco.posicao.field.choices
  return render(request, 'forms_contratações.html',context={
    'type': 'Adicionar',
    'options_posicao': options_posicao,
  })

def update_cont(request,id):
  cont= contratacoesDoVasco.objects.get(id=id)
  if request.method=='POST':
      cont.nome= request.POST['nome']
      cont.posicao=request.POST['posicao']
      cont.deOndeVeio=request.POST['deOndeVeio']
      cont.valor=request.POST['valor']
      cont.save()

      return redirect ('meuApp')
  options_posicao = craquesDoVasco.posicao.field.choices
  return render(request, 'forms_contratações.html', context={
    'type': 'Atualizar',
    'cont': cont,
    'options_posicao': options_posicao,
  })

def delete_cont(request,id):
  cont= contratacoesDoVasco.objects.get(id=id)
  if request.method=='POST':
    if request.POST['confirm']:
      cont.delete()
    
      return redirect ('meuApp')   
  return render(request, 'are_you_sure_cont.html', context={'cont': cont})