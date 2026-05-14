numeros = [0]*10
for i in range(10):
    numeros[i] = int(input('Insira um numero: '))
maior = numeros[0]
menor = numeros[0]
n = 0
print(numeros)
while n != 10:
    if numeros[n] > maior:
        maior = numeros[n]
    elif menor < numeros[n]:
        menor = numeros[n]
    n += 1
print(maior)
print(menor)
print(numeros)