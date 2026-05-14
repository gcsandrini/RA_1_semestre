numeros = []
pares = []
for i in range(1,101):
    numeros.append(i)
for n in range(100):
    if numeros[n]%2 == 0:
        pares.append(numeros[n]) 
print(pares)