from files import *

def calculo_imc(peso, altura):
    return peso / (altura * altura)

def gerar_lista_imc(dados):
    tamanho_lista = len(dados['pessoas'])
    lista_imc_pessoas = {}
    for i in range(tamanho_lista):
        aux = calculo_imc(dados['pessoas'][i]['peso'],dados['pessoas'][i]['altura'])
        lista_imc_pessoas[dados['pessoas'][i]['nome']] = aux

    return lista_imc_pessoas


