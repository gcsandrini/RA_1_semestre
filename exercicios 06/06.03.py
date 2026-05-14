numeros = [0]*10
numerosQuadrados = [0]*10
i = 0
while i != 10:
    numeros[i] = int(input('Insira um numero: '))
    numerosQuadrados[i] = numeros[i]**2
    i += 1
print(numeros)
print(numerosQuadrados)