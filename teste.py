from imc import *


def getClientes():
    rows = ler_arquivo("pessoa1.json")
    tamanho_lista_clientes = len(rows['clients'])
    
    clients = []
    """
    for i in rows:
        print(rows['clients'][0]['nome'])
        print("tamanho da lista clients: ", len(rows['clients']))
    """ 
    for i in range(tamanho_lista_clientes):
        d = []
        d.append(rows['clients'][i]['id'])
        d.append(rows['clients'][i]['nome'])
        d.append(rows['clients'][i]['peso'])
        d.append(rows['clients'][i]['altura'])
        d.append(rows['clients'][i]['idade'])
        clients.append(d)
        
    return clients


def calcularIMC():
    rows = getClientes()
    tamanho_lista = len(rows)
    lista_imc = {}
    for i in range(tamanho_lista):
        lista_imc[rows[i][0]] = calculo_imc(rows[i][2], rows[i][3])
        
        
    return lista_imc

        



lista_pessoas = getClientes()
#print(lista_pessoas[1][4])
print(calcularIMC())

