numeros = [0]*10
positivos = 0
negativos = 0
for i in range(10):
    numeros[i] = float(input('Insira um numero: '))
    if numeros[i] > 0:
        positivos += numeros[i]
    else:
        negativos += 1
print(f'Voce digitou {negativos} numeros negativos, e a soma de todos os numeros positivos q vc digitou é {positivos} ')