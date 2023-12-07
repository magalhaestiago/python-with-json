import json

file = 'pessoa.json'
with open (file, 'r') as arquivo:
    data_json = json.load(arquivo)
        
    
print(data_json)
