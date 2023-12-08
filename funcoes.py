from files import *

# Método para calculo imc (fórmula retirada do google)
def calculo_imc(peso, altura):
    return peso / (altura * altura)

# Método para gerar lista IMC derivado de um dicionário JSON seguindo o padrão do arquivo 'pessoas.json' dentro desse diretório
def gerar_lista_imc(dados):
    tamanho_lista = len(dados['pessoas']) # Variável para armazenar a quantidade de 'pessoas' ou 'clientes'
    lista_imc_pessoas = {} 
    for i in range(tamanho_lista): 
        aux = calculo_imc(dados['pessoas'][i]['peso'],dados['pessoas'][i]['altura']) # Calcular o imc do iteravel
        lista_imc_pessoas[dados['pessoas'][i]['id']] = [dados['pessoas'][i]['nome'], aux] # Armazenar o imc calculado acima

    # Retorna a lista com IMC's calculados
    return lista_imc_pessoas




def selecao_acima_media(dados):
    aux = gerar_lista_imc(dados)
    
    avg = 0
    sum = 0
    tam_dados = len(aux)
    
    # Calcula a soma de IMC's
    for i in range(1, tam_dados + 1):
        sum = sum + aux[i][1]
    
    # Calcula a média de IMC's
    avg = sum / tam_dados
    
    # Se IMC[i] estiver abaixo da média, é removido da lista
    for i in range(1, tam_dados + 1):
        if aux[i][1] < avg:
            del aux[i]
            
    # Retorna nova lista com os IMC's acima da média
    return aux



def selecao_abaixo_media(dados):
    aux = gerar_lista_imc(dados)
    
    aux = gerar_lista_imc(dados)
    
    avg = 0
    sum = 0
    tam_dados = len(aux)
    
    # Calcula a soma de IMC's
    for i in range(1, tam_dados + 1):
        sum = sum + aux[i][1]
    
    # Calcula a média de IMC's
    avg = sum / tam_dados
    
    # Se IMC[i] estiver acima da média é removido
    for i in range(1, tam_dados + 1):
        if aux[i][1] > avg:
            del aux[i]
            
    # Retorna lista com IMC's abaixo da média
    return aux
            
            
            
    
# !!!! As funções abaixo ainda estão sendo desenvolvidas, para que possam retornar além da lista de IMC's, também informações importantes, como a média que foi estabelecida, quantidade de elementos que foram removidos, e dentre outros !!!!

def selecao_abaixo_media_informacoes(dados):
    aux = gerar_lista_imc(dados)
    
    aux = gerar_lista_imc(dados)
    
    avg = 0
    sum = 0
    tam_dados = len(aux)
    elem_removido = 0
    
    for i in range(1, tam_dados + 1):
        sum = sum + aux[i][1]
        
    avg = sum / tam_dados
    
    for i in range(1, tam_dados + 1):
        if aux[i][1] > avg:
            elem_removido = i + 1
            del aux[i]
            
    
    return elem_removido, avg, aux

def selecao_acima_media_informacoes(dados):
    aux = gerar_lista_imc(dados)
    
    avg = 0
    sum = 0
    tam_dados = len(aux)
    elem_removido = 0
    
    
    for i in range(1, tam_dados + 1):
        sum = sum + aux[i][1]
        
    avg = sum / tam_dados
    
    for i in range(1, tam_dados + 1):
        if aux[i][1] < avg:
            elem_removido = i
            del aux[i]
            
    
    return elem_removido, avg, aux
