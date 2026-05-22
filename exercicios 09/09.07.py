def soma_elementos(x):
    return(sum(x))
def main():
    numeros = []
    for i in range(5):
        numero = int(input('Insira um numero: '))
        numeros.append(numero)
    print(soma_elementos(numeros))
main()