contador = int(0)
par = int(0)
impar = int(0)
while contador != 10:
    numero = float(input('Insira um numero: '))
    contador += 1
    if numero%2 == 0:
        par = par+1
    else:
        impar = impar+1
print(f'vc inseriu {par} numeros pares e {impar} numeros impares')