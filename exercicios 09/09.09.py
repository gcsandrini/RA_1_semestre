def maior_elemento(x):
    maior = x[0]
    for i in range(5):
        if maior < x[i]:
            maior = x[i]
    return(maior)
def main():
    numeros = []
    for i in range(5):
        numeros.append(int(input('Insira um numero: ')))
    print(maior_elemento(numeros))
main()