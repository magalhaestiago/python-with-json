from files import *
from funcoes import calculo_imc



arquivo = 'try\pessoa.json'

data = readFile(arquivo)

print(data['altura'])

imc = calculo_imc(data['peso'], data['altura'])
dados = {'imc': imc}
createFile(dados, 'try\oi.json')