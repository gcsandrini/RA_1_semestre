valores = [0]*5
contadorMaior = 0
contadorMenor = 0
for i in range(5):
    valores[i] = int(input('Insira um valor: '))
maior = valores[0]
menor = valores[0]
for n in range(5):
    if valores[n] > maior:
        maior = valores[n]
        contadorMaior = n
    elif valores[n] < menor:
        menor = valores[n]
        contadorMenor = n
print(f'O maior valor se encontra na posição {contadorMaior+1}, e o menor se encontra na posição {contadorMenor+1}')