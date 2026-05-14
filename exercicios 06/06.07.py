numeros = [0]*10
for i in range(10):
    numeros[i] = int(input('Insira um numero: '))
maior = numeros[0]
n = 0
posicao = 0
while n != 10:
    if numeros[n] > maior:
        maior = numeros[n]
        posicao = n
    n += 1
print(numeros)
print(maior)
print(posicao+1)