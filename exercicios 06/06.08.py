notas = [0]*15
soma = 0
for i in range(15):
    notas[i] = float(input('Insira a nota: '))
    soma += notas[i]
print(soma/15)