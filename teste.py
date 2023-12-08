dados = {1: ['tiago', 21], 2: ['babi', 20], 3: ['josias', 30]}

tam_dados = len(dados)
avg = 0
sum = 0

print(dados[1][1])

for i in range(1, tam_dados + 1):
    print(i," idade: ", dados[i][1])

for i in range(1, tam_dados + 1):
    sum = sum + dados[i][1]
    
print(sum) 