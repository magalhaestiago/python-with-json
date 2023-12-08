from files import *
from funcoes import *



arquivo = 'pessoas.json'
# Ler arquivo .json
data = readFile(arquivo)

# Gerar lista de imc com os arquivos lidos
lista = gerar_lista_imc(data)
lista_acima_media = selecao_acima_media(data)
lista_abaixo_media = selecao_abaixo_media(data)

print("Lista completa: ", lista)
print("Lista de IMC's acima da média: ", lista_acima_media)
print("Lista de IMC's abaixo da média: ", lista_abaixo_media)

# Criar arquivos .json
nome = 'lista_imc.json'
createFile(lista, nome)

# Acima da média
nome = 'lista_imc_acima_media.json'
createFile(lista_acima_media,nome)

# Abaixo da média
nome = 'lista_imc_abaixo_media.json'
createFile(lista_abaixo_media, nome)

nome = ''