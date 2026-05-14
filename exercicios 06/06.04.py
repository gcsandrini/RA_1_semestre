numeros = [0]*8
i = 0
while i != 8:
    numeros[i] = int(input('Insira um numero: '))
    i += 1
escolha1 = int(input('Escolha um dos 8 numeros q vc inseriu: '))
escolha2 = int(input('Escolha um segundo numero dentre esses 8: '))
print(f'{numeros[escolha1-1]+numeros[escolha2-1]}')