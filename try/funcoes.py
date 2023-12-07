from files import *

def calculo_imc(peso, altura):
    return peso / (altura * altura)

# o que eu preciso fazer?
# preciso ler esse arquivo e armazenar em uma lista

nome_arquivo = 'try\pessoas.json'
data = readFile(nome_arquivo)

print(data['pessoas'][2]['peso'])


def lista_imc(dados):
    tamanho_lista = len(dados['pessoas'])
    lista_imc_pessoas = []
    for i in range(tamanho_lista):
        aux = calculo_imc(dados['pessoas'][i]['peso'],dados['pessoas'][i]['altura'])
        lista_imc_pessoas.append(aux)

    return lista_imc_pessoas


print(lista_imc(data))

createFile(lista_imc(data), "try\lista_imc.json")
