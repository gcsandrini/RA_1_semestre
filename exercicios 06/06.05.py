numeros = [0]*10
contadorPar = 0
for i in range(10):
    numeros[i] = int(input('Insira um numero: '))
    if numeros[i]%2 == 0:
        contadorPar += 1
print(contadorPar)