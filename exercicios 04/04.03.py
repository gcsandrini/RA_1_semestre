numeros = float(input('Insira um numero: '))
numerosLista = []
while numeros != -1:
    numerosLista.append(numeros)
    numeros = float(input('Insira um numero: '))
print(f'{sum(numerosLista)/len(numerosLista)}')