# Importa biblioteca Json
import json

# Armazena diretório do arquivo, aqui será selecionado qual arquivo .json será lido
nome_arquivo = 'pessoa2.json'

# Ocorre a leitura do arquivo e é armazenado em uma variável
with open(nome_arquivo, 'r') as arquivo:
    data_json = json.load(arquivo)

# Função que calcula o IMC
def calculo_imc(peso, altura):
    return peso / (altura * altura)
    
# Criação de um dicionário que será responsavel por armazenar os dados que irão ser convertidos para .json
dados={
    "imc": calculo_imc(data_json['peso'], data_json['altura'])
}

# Criação do novo arquivo .json
nome_novo_arquivo = 'imc2.json'
with open(nome_novo_arquivo, 'w') as arquivo:
    json.dump(dados, arquivo, indent=2)