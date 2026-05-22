def media(x):
    numeros = []
    for i in range(x):
        numeros.append(int(input('Insira seu numero: ')))
    return(sum(numeros)/x)
def main():
    print(media(4))
main()