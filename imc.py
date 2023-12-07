#import biblioteca collections

import collections

# Importa biblioteca Json
import json

# Armazena diretório do arquivo, aqui será selecionado qual arquivo .json será lido
nome_arquivo = 'pessoa2.json'

# Função para ler arquivo .json
def ler_arquivo(arquivo_a_ser_lido):
    # Ocorre a leitura do arquivo e é armazenado em uma variável
    with open(arquivo_a_ser_lido, 'r') as arquivo:
        data_json = json.load(arquivo)
        
    return data_json

# Função para gerar novo arquivo .json
def gerar_novo_arquivo(dados):
# Criação do novo arquivo .json
    nome_novo_arquivo = 'imc2.json'
    with open(nome_novo_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)


# Função que calcula o IMC
def calculo_imc(peso, altura):
    return peso / (altura * altura)

"""
# Criação de um dicionário que será responsavel por armazenar os dados que irão ser convertidos para .json
dados={
    "imc": calculo_imc(data_json['peso'], data_json['altura'])
}
"""

# Criação de um dicionário que será responsavel por armazenar os dados que irão ser convertidos para .json
dados={
    "imc": calculo_imc(ler_arquivo(nome_arquivo)['peso'], ler_arquivo(nome_arquivo)['altura'])
}

gerar_novo_arquivo(dados)





