contagem = int(0)
for numero in range(101):
    if numero % 3 == 0 and numero % 5 != 0:
        contagem += 1
        print(numero)
print(f'são {contagem} numeros')