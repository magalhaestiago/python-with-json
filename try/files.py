import json

def readFile(file):
    with open (file, 'r') as arquivo:
        data_json = json.load(arquivo)
        
    return data_json



def createFile(data, nameFile):
    with open(nameFile, 'w') as arquivo:
        json.dump(data, arquivo, indent=2)