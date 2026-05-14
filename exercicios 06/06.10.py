valores = [0]*5
soma = 0
for i in range(5):
    valores[i] = float(input('Digite um valor: '))
    soma += valores[i]
maior = valores[0]
menor = valores[0]
for n in range(5):
    if valores[i] > maior:
        maior = valores[i]
    elif menor > valores[i]:
        menor = valores[i]
print(f'Esses foram os numeros digitados: {valores} \nEsse é o maior valor: {maior} \nEsse é o menor valor: {menor} \ne essa é a media entre eles: {soma/5} ')