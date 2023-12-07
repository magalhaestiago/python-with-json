from files import *
from funcoes import *



arquivo = 'pessoas.json'
# Ler arquivo .json
data = readFile(arquivo)

# Gerar lista de imc com os arquivos lidos
lista = gerar_lista_imc(data)

# Criar arquivo .json
nome = 'lista_imc.json'
createFile(lista,nome)

